# 🌳 COUNT THE TREES AI

### AI-Based Individual Tree Crown Detection and Canopy Footprint Estimation

**Live Demo:**  
https://325efbc22da8f2a983.gradio.live

**Demo availability:**
The current public Gradio demo is hosted through a Google Colab runtime. The demo link requires the associated runtime to be active. The repository contains the complete application code and installation requirements for reproducing the tool.

> **Note:** The live demo is currently hosted through a temporary Gradio share link and requires the underlying Google Colab runtime to remain active.

---

## 🌲 Overview

**COUNT THE TREES AI** is a computer-vision application for detecting and counting individual tree crowns from high-resolution aerial imagery.

The application accepts a high-resolution RGB GeoTIFF and automatically:

- Detects individual tree crowns
- Counts detected trees
- Delineates crown boundaries
- Estimates crown/canopy footprint area
- Reports model confidence scores
- Provides individual-tree results
- Generates a downloadable CSV file

The project focuses on providing a practical and usable workflow for rapid tree-crown analysis while clearly communicating the limitations of image-derived estimates.

---

## 🎯 Project Objective

The objective of COUNT THE TREES AI is to demonstrate a working AI-based workflow that can:

1. Detect individual tree crowns
2. Count detected trees
3. Estimate visible crown/canopy footprint area
4. Visualize detected crown boundaries
5. Provide structured results that can be inspected and downloaded

The application is designed as a demonstration of automated tree-crown analysis rather than a complete forest inventory system.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌳 Tree Crown Detection | Detects individual tree crowns from RGB aerial imagery |
| 🔢 Tree Counting | Reports the number of detected tree instances |
| 🟢 Crown Delineation | Displays detected crown boundaries over the input image |
| 📐 Crown Area | Estimates crown/canopy footprint area in square metres |
| 📊 Confidence Scores | Reports the model confidence for each detection |
| 📋 Individual Tree Table | Displays tree-level detection results |
| 📥 CSV Export | Allows users to download the detection results |
| 🖥️ Interactive Interface | Provides a simple Gradio-based web interface |

---

## 🚀 Live Demo

Try the application using the live demo:

https://325efbc22da8f2a983.gradio.live

### Basic workflow

```text
Upload GeoTIFF
      ↓
Image processing
      ↓
Tree crown detection
      ↓
Crown polygon generation
      ↓
Crown area calculation
      ↓
Tree count + visualization
      ↓
Individual tree results
      ↓
CSV download
```

---

## 🖼️ Input Data

The current application accepts:

- `.tif`
- `.tiff`

The expected input is a **high-resolution RGB GeoTIFF**.

GeoTIFF is used because the imagery contains spatial information required for calculating crown footprint areas in square metres.

JPG and PNG inputs are not currently enabled because ordinary image files do not necessarily contain the spatial reference and pixel-scale information required for reliable area calculation in square metres.

---

## 🧠 Model

The application uses a pretrained **Detectree2** model based on **Detectron2** for individual tree crown delineation.

### Model checkpoint

```text
250312_flexi.pth
```

The model checkpoint is downloaded from Zenodo when required and is not stored directly inside this repository.

The application uses GPU acceleration when CUDA is available.

---

## 🔬 Processing Method

### 1. Input

A high-resolution RGB GeoTIFF is uploaded through the Gradio interface.

### 2. Tiled inference

The input image is processed using tiled inference so that larger images can be analysed in manageable sections.

### 3. Tree crown detection

Detectree2 identifies individual tree instances and generates spatial crown polygons.

### 4. Crown area calculation

The area of each detected crown polygon is calculated from its spatial geometry.

The result is reported as:

```text
area_m2
```

representing the estimated visible crown/canopy footprint area in square metres.

### 5. Results

The application returns:

- Total detected trees
- Total estimated crown area
- Mean crown area
- Median crown area
- Individual tree confidence scores
- Individual tree crown areas
- Crown boundary visualization
- Downloadable CSV results

---

## 📊 Output

For every detected tree, the application produces the following information:

| Variable | Description |
|---|---|
| `tree_id` | Unique identifier assigned to the detected tree |
| `confidence` | Model confidence score for the detection |
| `area_m2` | Estimated crown/canopy footprint area in square metres |

### Summary statistics

The application reports:

```text
Trees detected
Total crown area
Mean crown area
Median crown area
```

---

## 🌿 Example Results

The model was successfully tested on high-resolution RGB GeoTIFF imagery.

One test image produced:

```text
Trees detected: 137
Total crown area: 9421.33 m²
Mean crown area: 68.77 m²
Median crown area: 55.32 m²
```

A separate GeoTIFF test image produced:

```text
Trees detected: 10
Total crown area: 235.12 m²
Mean crown area: 23.51 m²
Median crown area: 17.69 m²
```

These values are examples of the application's output and are dependent on the input imagery.

---

## 🛠️ Technology Stack

The project uses:

- **Python**
- **PyTorch**
- **Detectree2**
- **Detectron2**
- **Rasterio**
- **GeoPandas**
- **Shapely**
- **PyProj**
- **Fiona**
- **Pandas**
- **Matplotlib**
- **OpenCV**
- **Gradio**
- **Google Colab GPU**

---

## 📁 Repository Structure

```text
count-the-trees-ai/
│
├── README.md
│
├── app.py
│
├── requirements.txt
│
├── forestry.ipynb
│
├── LICENSE
│
└── docs/
    │
    ├── reports.docx
    ├── example_images/
    │      ├── test.tif
    │      └── 0060A59MGW_chipid141.tiff
    │    
    └── methodology.md
        
```

---

## ⚙️ Installation

The project was developed and tested in **Google Colab using a T4 GPU**.

Install the Python dependencies using:

```bash
pip install -r requirements.txt
```

The repository includes the Detectree2 and Detectron2 dependencies required by the application.

---

## ▶️ Running the Application

The application can be started with:

```bash
python app.py
```

The application launches a Gradio interface.

For GPU-enabled execution, a CUDA-compatible PyTorch environment is recommended.

The development workflow used Google Colab with GPU acceleration because the tree-crown detection model is computationally demanding.

---

## 📥 Using the Application

### Step 1

Open the live demo.

### Step 2

Upload a high-resolution RGB GeoTIFF file.

Supported extensions:

```text
.tif
.tiff
```

### Step 3

Wait for the tree-crown detection process to complete.

### Step 4

Inspect the generated crown-boundary visualization.

### Step 5

Review the summary statistics and individual tree table.

### Step 6

Download the CSV containing the individual tree results.

---

## 📄 CSV Output

The generated CSV contains:

```text
tree_id
confidence
area_m2
```

Example:

```text
tree_id,confidence,area_m2
1,0.846943,39.004995
2,0.957606,102.126222
...
```

The CSV can be used for further analysis or visualization.

---

## ⚠️ Limitations

The reported crown area is an **image-derived estimate of visible crown/canopy footprint area**.

Detection performance can vary depending on:

- Image resolution
- Image quality
- Tree visibility
- Shadows
- Crown overlap
- Forest structure
- Seasonal conditions
- Image acquisition conditions
- Similarity between the input imagery and the model's training domain

Crowns that are heavily occluded, overlapping, poorly visible or outside the model's effective domain may be missed or inaccurately delineated.

The detected tree count should therefore be interpreted as the **number of detected tree instances**, rather than an absolute census of all trees present in the imagery.

Similarly, crown area represents an image-derived estimate of visible crown/canopy footprint and should not be interpreted as a direct measurement of total tree size.

---

## 🚫 What the System Does Not Estimate

The current application does **not** estimate:

- Tree height
- Biomass
- Carbon stock
- Carbon offsets
- Tree species
- Tree age
- Timber volume

These quantities require additional data and modelling and are outside the scope of the current system.

---

## 🔐 Model and Data Considerations

The pretrained model checkpoint is downloaded when required rather than stored in the repository.

The repository therefore contains the application code and workflow, but not the large model checkpoint file.

Users should ensure that their input imagery is suitable for analysis and that they have the necessary rights to use the imagery.

---

## 📚 Documentation

Additional methodology information is available in:

```text
docs/methodology.md
```

A separate project explanation describing the methodology, implementation and limitations is provided as part of the challenge documentation.

---

## 🧪 Development Environment

The successful development and testing workflow used:

```text
Platform: Google Colab
GPU: NVIDIA T4
Input: High-resolution RGB GeoTIFF
Model: Detectree2 / Detectron2
Interface: Gradio
```

The model was successfully initialized and used for tree-crown inference in the development environment.

---

## 🏆 Tree Crown AI Challenge

This project was developed for the **Tree Crown AI Challenge** by FLORACARBON.AI 

The solution focuses on the core requirements of:

1. Individual tree crown detection
2. Tree counting
3. Crown/canopy area estimation
4. Usable presentation of results
5. Clear communication of system limitations

The project intentionally avoids making unsupported claims about biomass, carbon, height, species or other forest attributes that are not calculated by the current system.

---

## 🌳 Project Summary

COUNT THE TREES AI provides a practical computer-vision workflow for converting high-resolution RGB aerial imagery into structured tree-crown information.

The system combines:

```text
High-resolution imagery
        +
Detectree2 / Detectron2
        +
Spatial crown polygons
        +
Geometric area calculation
        ↓
Tree detection results
```

The final output allows a user to inspect detected tree crowns, review tree counts and crown areas, and download the corresponding individual-tree results.

---

## 📌 Current Status

**Status: Working prototype / challenge submission**

The interactive application has been tested successfully with GeoTIFF imagery and produces tree-crown detections, crown-area estimates, visualizations and CSV output.

The current live demo is hosted through a temporary Gradio share link backed by a Google Colab runtime.

---

## 👤 Project Repository

This repository contains the complete development notebook, standalone application, dependency specification and supporting documentation required to understand 
the project.

---
 ## 🔗 CONNECT

[![GitHub](https://img.shields.io/badge/GitHub-AbhilashaxData-black?logo=github)](https://github.com/AbhilashaxData)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abhilasha%20Das-blue?logo=linkedin)](https://www.linkedin.com/in/abhilasha-das1/)
