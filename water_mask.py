import cv2
import numpy as np

def water_mask(img):
    # Convert to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Water (blue) HSV range
    lower_blue = np.array([90, 50, 20])
    upper_blue = np.array([130, 255, 255])

    # Create water mask
    water_mask_img = cv2.inRange(img_hsv, lower_blue, upper_blue)

    # Save mask
    cv2.imwrite("water_mask.png", water_mask_img)

    return water_mask_img
