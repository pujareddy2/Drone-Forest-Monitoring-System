import cv2
import numpy as np

def soil_mask(img):
    # Convert to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Soil / Empty land HSV range (brown/yellow-ish)
    lower_soil = np.array([10, 20, 20])
    upper_soil = np.array([25, 255, 255])

    # Create soil mask
    soil_mask_img = cv2.inRange(img_hsv, lower_soil, upper_soil)

    # Save the mask
    cv2.imwrite("soil_mask.png", soil_mask_img)

    return soil_mask_img
