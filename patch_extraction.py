import cv2
import numpy as np

def extract_patches():
    # Load classification map (BGR)
    class_map = cv2.imread("classification_map.png")

    # Load vegetation mask
    veg_mask = cv2.imread("vegetation_mask.png", cv2.IMREAD_GRAYSCALE)

    # Convert classification to grayscale
    gray = cv2.cvtColor(class_map, cv2.COLOR_BGR2GRAY)

    # Binary for connected components
    _, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    # Connected components
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)

    patch_info = []

    for i in range(1, num_labels):  # skip background
        x, y, w, h, area = stats[i]

        # Create mask for current patch
        patch_mask = (labels == i).astype("uint8") * 255

        # Compute vegetation pixels inside this patch
        veg_inside_patch = cv2.bitwise_and(veg_mask, veg_mask, mask=patch_mask)

        veg_pixels = np.count_nonzero(veg_inside_patch)
        total_pixels = area

        if total_pixels > 0:
            veg_percent = (veg_pixels / total_pixels) * 100
        else:
            veg_percent = 0

        patch_info.append({
            "patch_id": i,
            "x": int(x),
            "y": int(y),
            "width": int(w),
            "height": int(h),
            "area_pixels": int(area),
            "vegetation_pixels": int(veg_pixels),
            "vegetation_percentage": float(round(veg_percent, 2))
        })

    # Save output
    with open("patch_data.txt", "w") as f:
        for p in patch_info:
            f.write(str(p) + "\n")

    print(f"Extracted {len(patch_info)} patches with vegetation percentages.")
    return patch_info
