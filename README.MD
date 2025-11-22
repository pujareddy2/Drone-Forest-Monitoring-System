
***

# Forest Monitoring & Risk Detection - Project Workflow

## **Overview**

This repository implements an image-based GIS forest land monitoring pipeline. It automates fire/burn detection, change analysis, risk mapping, illegal activity search, ownership overlay, and documentation/reporting.

***

## **Dependencies**

All major modules require:
```
pip install numpy opencv-python scikit-image shapely rasterio geopandas scikit-learn matplotlib
```
Or, with:
```
pip install -r requirements.txt
```
(Extras like `scikit-image`, `shapely`, `rasterio`, `geopandas`, and `scikit-learn` are only needed for extensions—core modules run with just `numpy`, `opencv-python`, `matplotlib`.)

***

## **Tasks & Modules**

| Task Number | Task Name                        | Description                                                                 |
| ----------- | -------------------------------- | --------------------------------------------------------------------------- |
| 1           | Data Acquisition & Preprocessing | Collect “before”/“after” images; resize, normalize, mask.                   |
| 2           | Fire/Burn Area Detection         | Segment fire-affected zones using pixel thresholding or vegetation indices. |
| 3           | Burn Severity & Recovery Scoring | Classify severity; analyze regrowth; score recovery potential.              |
| 4           | Change Detection                 | Compare images to identify land cover change/clearings.                     |
| 5           | Illegal Activity Pattern Search  | Find mining pits (rectangles), logging, bulldozer paths via shape analysis. |
| 6           | Path/Trail Detection             | Use edge detection, Hough line, skeletonization to map paths/trails.        |
| 7           | Risk Layer Generation            | Compile all detections into GIS-ready risk maps/layers for output.          |
| 8           | Ownership Check                  | Mark risk on govt/private parcels using overlay mask or vector GIS data.    |
| 9           | Documentation & Reporting        | Generate summary, CSV, and annotated images for dashboard/final review.     |

***

## **Quickstart Guide**

1. **Activate your virtual environment**
   ```bash
   .venv\Scripts\Activate  # Windows
   source .venv/bin/activate  # Mac/Linux
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run each module (edit folder paths to match your structure):**

```bash
cd "C:\Users\ujasv\OneDrive\Desktop\forest mem3\Data Acquisition & Preprocessing"
python preprocess.py
python view_images.py

cd "C:\Users\ujasv\OneDrive\Desktop\forest mem3\Fire/Burn Area Detection"
python fire_detection.py

cd "C:\Users\ujasv\OneDrive\Desktop\forest mem3\Burn Severity & Recovery Scoring"
python burn_severity_recovery.py

cd "C:\Users\ujasv\OneDrive\Desktop\forest mem3\Change Detection"
python change_detection.py

cd "C:\Users\ujasv\OneDrive\Desktop\forest mem3\Illegal Activity Pattern Search"
python illegal_activity_detection.py

cd "C:\Users\ujasv\OneDrive\Desktop\forest mem3\Path Trail Detection"
python trail_detection.py

cd "C:\Users\ujasv\OneDrive\Desktop\forest mem3\Risk Layer Generation"
python risk_layer_generation.py

cd "C:\Users\ujasv\OneDrive\Desktop\forest mem3\Ownership Check"
python ownership_check.py

cd "C:\Users\ujasv\OneDrive\Desktop\forest mem3\Z Documentation & Reporting"
python project_reporting.py
```
*Update folder locations as per your system structure!*

***

## **Notes**

- Output files (images, CSVs, reports) are generated in each module directory
- Use summary/project_report.md for final documentation
- Review all images and CSVs before submission

***

## **Contact & Support**
For folder/path or additional integration help, review comments in each script or reach out to your supervising mentor/teammate.

***

This README makes your project plug-and-play for evaluators, team, or future users!