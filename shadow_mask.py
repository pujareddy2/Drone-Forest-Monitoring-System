import cv2
import numpy as np

def shadow_mask(img):
    # Convert to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Shadow / cloud areas
    # Shadows = very dark (low V)
    # Clouds = very bright, but low saturation

    lower_shadow = np.array([0, 0, 0])
    upper_shadow = np.array([180, 255, 60])   # dark areas

    lower_cloud = np.array([0, 0, 200])
    upper_cloud = np.array([180, 30, 255])    # bright, low saturation

    # Create masks
    shadow_mask_img = cv2.inRange(img_hsv, lower_shadow, upper_shadow)
    cloud_mask_img = cv2.inRange(img_hsv, lower_cloud, upper_cloud)

    # Combine both masks
    combined_mask = cv2.bitwise_or(shadow_mask_img, cloud_mask_img)

    # Save the combined mask
    cv2.imwrite("shadow_mask.png", combined_mask)

    return combined_mask
