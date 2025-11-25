from load_image import load_image
from vegetation_mask import vegetation_mask
from water_mask import water_mask
from soil_mask import soil_mask
from burnt_mask import burnt_mask
from shadow_mask import shadow_mask
from classification import classification_map
from patch_extraction import extract_patches

# Load image
img = load_image()

# Run vegetation mask
vegetation_mask(img)

# Run water mask
water_mask(img)

# Run soil mask
soil_mask(img)

# Run burnt mask
burnt_mask(img)

# Run shadow/cloud mask
shadow_mask(img)

# Run final classification map
classification_map(img)

# Extract patches
extract_patches()

print("ALL TASKS COMPLETED SUCCESSFULLY!")
