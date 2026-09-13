import os
import requests
import torch
import gradio as gr
import rasterio
import matplotlib.pyplot as plt
import pandas as pd

from rasterio.plot import plotting_extent
from samgeo.detectree2 import TreeCrownDelineator


# -----------------------------
# Setup
# -----------------------------

os.makedirs("data", exist_ok=True)

MODEL_URL = "https://zenodo.org/records/15863800/files/250312_flexi.pth"
MODEL_PATH = "250312_flexi.pth"


# Download model if it is not already present
if not os.path.exists(MODEL_PATH):
    r = requests.get(MODEL_URL, allow_redirects=True)
    r.raise_for_status()

    with open(MODEL_PATH, "wb") as f:
        f.write(r.content)


# PyTorch compatibility
_original_torch_load = torch.load

def torch_load_compat(*args, **kwargs):
    kwargs.setdefault("weights_only", False)
    return _original_torch_load(*args, **kwargs)

torch.load = torch_load_compat


# Load Detectree2 model
delineator = TreeCrownDelineator(
    model_path=MODEL_PATH,
    device="cuda" if torch.cuda.is_available() else "cpu",
    confidence_threshold=0.5,
    nms_threshold=0.3
)


# -----------------------------
# Analysis function
# -----------------------------

def analyze(image_path):

    output_path = "data/app_crowns.gpkg"

    crowns = delineator.predict(
        image_path=image_path,
        output_path=output_path,
        tile_width=20,
        tile_height=20,
        buffer=30,
        simplify_tolerance=0.2,
        min_confidence=0.3,
        iou_threshold=0.6,
    )

    # Calculate crown area
    crowns["area_m2"] = crowns.geometry.area

    # Create result table
    results = crowns[["Confidence_score", "area_m2"]].copy()

    results.insert(
        0,
        "tree_id",
        range(1, len(results) + 1)
    )

    results = results.rename(
        columns={"Confidence_score": "confidence"}
    )

    # Save CSV
    csv_path = "data/tree_detections.csv"
    results.to_csv(csv_path, index=False)

    # Read image for visualization
    with rasterio.open(image_path) as src:

        rgb = src.read([1, 2, 3]).transpose(1, 2, 0)

        extent = plotting_extent(src)

    # Plot detected crowns
    fig, ax = plt.subplots(figsize=(12, 8))

    ax.imshow(
        rgb,
        extent=extent
    )

    crowns.boundary.plot(
        ax=ax,
        linewidth=1
    )

    ax.set_title(
        f"Tree Crown Detection | {len(crowns)} Trees"
    )

    ax.set_axis_off()

    plt.tight_layout()

    # Summary
    summary = (
        f"🌳 Trees detected: {len(crowns)}\n\n"
        f"🌿 Total crown area: "
        f"{crowns.area_m2.sum():,.2f} m²\n\n"
        f"📏 Mean crown area: "
        f"{crowns.area_m2.mean():,.2f} m²\n\n"
        f"📊 Median crown area: "
        f"{crowns.area_m2.median():,.2f} m²"
    )

    return fig, summary, results, csv_path


# -----------------------------
# Gradio application
# -----------------------------

app = gr.Interface(
    fn=analyze,

    inputs=gr.File(
        label="Upload high-resolution GeoTIFF",
        file_types=[".tif", ".tiff"],
        type="filepath"
    ),

    outputs=[
        gr.Plot(label="Detected Tree Crowns"),
        gr.Textbox(label="Results"),
        gr.Dataframe(label="Individual Trees"),
        gr.File(label="Download CSV")
    ],

    title="🌳 COUNT THE TREES AI",

    description=(
        "Upload high-resolution forest imagery to detect "
        "and count individual tree crowns and estimate "
        "their crown footprint area."
    ),

    flagging_mode="never"
)


app.launch(
    share=True
)
