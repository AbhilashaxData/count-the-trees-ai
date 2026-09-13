# Methodology

## Input

The application accepts high-resolution RGB GeoTIFF imagery.

## Tree Crown Detection

Individual tree crowns are delineated using a pretrained Detectree2 model based on Detectron2.

The image is processed using tiled inference. Detected crown instances are converted into spatial polygons.

## Crown Area

For each detected crown polygon, the polygon area is calculated in square metres using the spatial reference system of the input imagery.

The resulting value represents an estimated visible crown/canopy footprint.

## Outputs

The application produces:

1. Detected tree count
2. Crown boundary visualization
3. Individual tree confidence scores
4. Estimated crown area for each detected tree
5. Total, mean and median crown area
6. CSV export of individual tree results

## Limitations

Detection quality depends on image resolution, image quality, tree visibility, crown overlap, shadows, seasonal conditions and similarity to the model's training domain.

The system does not estimate tree height, biomass, carbon stock, species or age.
