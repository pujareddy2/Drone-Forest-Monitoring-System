# Task 1: Data Acquisition & Preprocessing
import cv2
import numpy as np

# 1. Read Images
before_img = cv2.imread('area_before.png')
after_img = cv2.imread('area_after.png')

# Check if images loaded successfully
if before_img is None or after_img is None:
    raise ValueError("Check that 'area_before.png' and 'area_after.png' exist in your folder.")

# 2. Resize Images (Uniform Size)
fixed_size = (512, 512)
before_img = cv2.resize(before_img, fixed_size)
after_img = cv2.resize(after_img, fixed_size)

# 3. Convert to Grayscale
before_gray = cv2.cvtColor(before_img, cv2.COLOR_BGR2GRAY)
after_gray = cv2.cvtColor(after_img, cv2.COLOR_BGR2GRAY)

# 4. Normalize Images
before_norm = cv2.normalize(before_gray.astype(np.float32), None, 0, 1.0, cv2.NORM_MINMAX)
after_norm = cv2.normalize(after_gray.astype(np.float32), None, 0, 1.0, cv2.NORM_MINMAX)

# 5. Masking Example (Optional: Use if you need ROI)
# Simple threshold mask for demonstration
_, mask = cv2.threshold(before_gray, 127, 255, cv2.THRESH_BINARY)
before_masked = cv2.bitwise_and(before_gray, mask)

# 6. Save Preprocessed Images
cv2.imwrite('before_resized.png', before_img)
cv2.imwrite('after_resized.png', after_img)
cv2.imwrite('before_grayscale.png', before_gray)
cv2.imwrite('after_grayscale.png', after_gray)
cv2.imwrite('before_normalized.png', (before_norm*255).astype('uint8'))
cv2.imwrite('after_normalized.png', (after_norm*255).astype('uint8'))
cv2.imwrite('before_masked.png', before_masked)
cv2.imwrite('after_preprocessed.png', after_img)

print("Preprocessing complete! Output files: before_resized.png, after_resized.png, before_grayscale.png, after_grayscale.png, before_normalized.png, after_normalized.png, before_masked.png, after_preprocessed.png")
