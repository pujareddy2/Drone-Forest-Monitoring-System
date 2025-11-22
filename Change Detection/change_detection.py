import cv2
import numpy as np

# Load images
before_img = cv2.imread('before_preprocessed.png')
after_img = cv2.imread('after_preprocessed.png')

if before_img is None or after_img is None:
    raise ValueError("File 'before_preprocessed.png' or 'after_preprocessed.png' missing.")

# Resize to same size if needed
size = (512, 512)
before_img = cv2.resize(before_img, size)
after_img = cv2.resize(after_img, size)

# Convert to grayscale
before_gray = cv2.cvtColor(before_img, cv2.COLOR_BGR2GRAY)
after_gray = cv2.cvtColor(after_img, cv2.COLOR_BGR2GRAY)

# Compute absolute difference image
diff_img = cv2.absdiff(before_gray, after_gray)

# Threshold difference image (tune threshold based on image properties)
_, diff_thresh = cv2.threshold(diff_img, 30, 255, cv2.THRESH_BINARY)

# Morphological operations to reduce noise
kernel = np.ones((5, 5), np.uint8)
diff_open = cv2.morphologyEx(diff_thresh, cv2.MORPH_OPEN, kernel)

# Optional: dilate to connect areas
diff_dilated = cv2.dilate(diff_open, kernel, iterations=1)

# Overlay detected changes on original after image for visualization
overlay = after_img.copy()
overlay[diff_dilated > 0] = [0, 0, 255]  # Red color for changed pixels

# Show images
cv2.imshow('Before', before_img)
cv2.imshow('After', after_img)
cv2.imshow('Difference', diff_img)
cv2.imshow('Thresholded Change Mask', diff_dilated)
cv2.imshow('Overlay of Changes', overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save outputs
cv2.imwrite('change_diff.png', diff_img)
cv2.imwrite('change_mask.png', diff_dilated)
cv2.imwrite('change_overlay.png', overlay)

print("Change detection complete! Check 'change_diff.png', 'change_mask.png', and 'change_overlay.png'.")
