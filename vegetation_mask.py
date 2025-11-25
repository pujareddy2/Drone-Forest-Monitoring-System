import cv2
import numpy as np

def vegetation_mask(img):
    # Convert to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Green vegetation HSV range
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([90, 255, 255])

    # Create vegetation mask
    veg_mask = cv2.inRange(img_hsv, lower_green, upper_green)

    # Save mask
    cv2.imwrite("vegetation_mask.png", veg_mask)

    # Return mask
    return veg_mask
