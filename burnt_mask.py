import cv2
import numpy as np

def burnt_mask(img):
    # Convert to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Burnt / dark areas (low brightness, low saturation)
    lower_burnt = np.array([0, 0, 0])      # black-ish
    upper_burnt = np.array([180, 255, 80]) # dark regions

    # Create burnt area mask
    burnt_mask_img = cv2.inRange(img_hsv, lower_burnt, upper_burnt)

    # Save the mask
    cv2.imwrite("burnt_mask.png", burnt_mask_img)

    return burnt_mask_img
