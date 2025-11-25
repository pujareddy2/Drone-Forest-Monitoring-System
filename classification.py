import cv2
import numpy as np

def classification_map(img):
    # Import all mask images (already saved earlier)
    veg = cv2.imread("vegetation_mask.png", cv2.IMREAD_GRAYSCALE)
    water = cv2.imread("water_mask.png", cv2.IMREAD_GRAYSCALE)
    soil = cv2.imread("soil_mask.png", cv2.IMREAD_GRAYSCALE)
    burnt = cv2.imread("burnt_mask.png", cv2.IMREAD_GRAYSCALE)
    shadow = cv2.imread("shadow_mask.png", cv2.IMREAD_GRAYSCALE)

    # Create empty 3-channel color output
    h, w = veg.shape
    color_map = np.zeros((h, w, 3), dtype=np.uint8)

    # Assign colors
    # Vegetation = Green
    color_map[veg > 0] = [0, 255, 0]

    # Water = Blue
    color_map[water > 0] = [255, 0, 0]

    # Soil = Yellow
    color_map[soil > 0] = [0, 255, 255]

    # Burnt = Red
    color_map[burnt > 0] = [0, 0, 255]

    # Shadow/Cloud = White
    color_map[shadow > 0] = [255, 255, 255]

    # Save classification map
    cv2.imwrite("classification_map.png", color_map)

    return color_map
