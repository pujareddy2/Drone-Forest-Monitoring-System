import cv2
import numpy as np

# 1. Read Images
before_img = cv2.imread('area_before.png')
after_img = cv2.imread('area_after.png')

# Resize for consistency
fixed_size = (512, 512)
before_img = cv2.resize(before_img, fixed_size)
after_img = cv2.resize(after_img, fixed_size)

# Grayscale conversion
before_gray = cv2.cvtColor(before_img, cv2.COLOR_BGR2GRAY)
after_gray = cv2.cvtColor(after_img, cv2.COLOR_BGR2GRAY)

# Normalize images
before_norm = cv2.normalize(before_gray.astype(np.float32), None, 0, 1.0, cv2.NORM_MINMAX)
after_norm = cv2.normalize(after_gray.astype(np.float32), None, 0, 1.0, cv2.NORM_MINMAX)

# Optional masking
_, mask = cv2.threshold(before_gray, 127, 255, cv2.THRESH_BINARY)
before_masked = cv2.bitwise_and(before_gray, mask)

# Display images in pop-up windows
cv2.imshow('Before - Original', before_img)
cv2.imshow('After - Original', after_img)
cv2.imshow('Before - Grayscale', before_gray)
cv2.imshow('Before - Normalized', (before_norm*255).astype('uint8'))
cv2.imshow('Before - Masked', before_masked)

# Wait until any key is pressed, then clean up windows
cv2.waitKey(0)
cv2.destroyAllWindows()
