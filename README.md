📘 README — Member 1: Core Image Processing & Land Segmentation
👤 Member 1 Responsibilities

This module performs all image processing and segmentation tasks for the Drone-Forest Monitoring System.
It generates masks, classification maps, and patch-level analysis used by all other members.

🟩 MODULE 1 — LAND COVER EXTRACTION
1. Vegetation Detection (HSV Thresholding)

Converted image from BGR → HSV

Applied calibrated green color thresholds

Output: vegetation_mask.png

2. Water Detection

Identified blue-tinted regions

Output: water_mask.png

3. Soil / Empty Land Detection

Detected brown/yellow regions

Output: soil_mask.png

4. Burnt Area Detection (Dark Pixel Mask)

Identified charred/dark regions

Output: burnt_mask.png

5. Shadow / Cloud Removal

Identified dark shadows and clouded soft areas

Output: shadow_mask.png

🟦 MODULE 2 — PIXEL-WISE CLASSIFICATION

Combined all masks to produce final classification:

Class	Label	Meaning
0	Background	Unknown
1	Vegetation	Green areas
2	Water	Lakes, ponds
3	Soil	Empty land
4	Burnt	Burnt patches
5	Shadow	Shadows/clouds

Output: classification_map.png

🟧 MODULE 3 — PATCH EXTRACTION & ANALYSIS
✔ Connected Components
✔ Patch Boundaries
✔ Patch-wise Area
✔ Vegetation Percentage per Patch

All results saved in:

➡ patch_data.txt

Includes:

Patch ID

Area

Vegetation %

Bounding box coordinates

🟪 MODULE 4 — COLLABORATION OUTPUTS

Member 1 generates all preprocessing required for:

Member 2 → GIS, Soil, Elevation

Member 3 → Illegal activity & Fire detection

Member 4 → Dashboard, Scoring

Outputs provided:

All masks

Classification map

Patch dataset

Base cleaned image

🟫 TOOLS USED

Python

OpenCV

NumPy

🟩 STATUS: COMPLETE

All Member-1 tasks completed:

✔ Vegetation Mask
✔ Water Mask
✔ Soil Mask
✔ Burnt Mask
✔ Shadow Mask
✔ Classification Map
✔ Patch Extraction
✔ Vegetation % Per Patch
✔ GitHub Upload (Branch: member1)

⭐ End of README