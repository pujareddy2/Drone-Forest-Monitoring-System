# FIRE/BURN AREA DETECTION - Step-by-step code
import cv2
import numpy as np

# Step 1: Load and Resize Image
image = cv2.imread('after_preprocessed.png')
if image is None:
    raise ValueError("File 'after_preprocessed.png' not found in the folder!")

fixed_size = (512, 512)
image = cv2.resize(image, fixed_size)

# Step 2: Convert to HSV Color Space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Step 3: Define HSV Ranges for Fire/Burnt Area
# Fire color range (orange/yellow)
fire_lower = np.array([18, 50, 50])
fire_upper = np.array([35, 255, 255])
# Burnt/dark area range (brown/dark area)
burn_lower = np.array([0, 0, 0])
burn_upper = np.array([30, 255, 80])

# Step 4: Create Masks for Fire and Burnt Areas
fire_mask = cv2.inRange(hsv, fire_lower, fire_upper)
burn_mask = cv2.inRange(hsv, burn_lower, burn_upper)

# Step 5: Morphological Cleaning (Optional, but recommended)
kernel = np.ones((5, 5), np.uint8)
fire_mask_clean = cv2.morphologyEx(fire_mask, cv2.MORPH_OPEN, kernel)
burn_mask_clean = cv2.morphologyEx(burn_mask, cv2.MORPH_OPEN, kernel)

# Step 6: Overlay Mask on Original Image
fire_detected = cv2.bitwise_and(image, image, mask=fire_mask_clean)
burn_detected = cv2.bitwise_and(image, image, mask=burn_mask_clean)

# For easy visualization: color output
overlay = image.copy()
overlay[fire_mask_clean > 0] = [0, 0, 255]      # Red for fire
overlay[burn_mask_clean > 0] = [42, 42, 165]    # Brown for burn

# Step 7: Find and Draw Contours (Optional)
contours, _ = cv2.findContours(burn_mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contoured_img = overlay.copy()
cv2.drawContours(contoured_img, contours, -1, (0, 255, 255), 2)  # Yellow contours

# Step 8: Display Results
cv2.imshow('Original', image)
cv2.imshow('Fire Mask', fire_mask_clean)
cv2.imshow('Burn Mask', burn_mask_clean)
cv2.imshow('Fire Detected', fire_detected)
cv2.imshow('Burn Detected', burn_detected)
cv2.imshow('Overlay', overlay)
cv2.imshow('Burn Contours', contoured_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 9: Save Results
cv2.imwrite('fire_mask.png', fire_mask_clean)
cv2.imwrite('burn_mask.png', burn_mask_clean)
cv2.imwrite('fire_detected.png', fire_detected)
cv2.imwrite('burn_detected.png', burn_detected)
cv2.imwrite('overlay.png', overlay)
cv2.imwrite('burn_contours.png', contoured_img)

print("Fire/Burn detection complete! Check the generated PNG files.")
