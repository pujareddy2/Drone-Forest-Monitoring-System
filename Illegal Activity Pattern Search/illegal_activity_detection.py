import cv2
import numpy as np

# Step 1: Load and preprocess image
image = cv2.imread('after_preprocessed.png')
if image is None:
    raise ValueError("File 'after_preprocessed.png' missing.")

# Step 2: (Optional) Focus on ROI if needed
# Example: To process only the lower half (change as needed)
roi = image[image.shape[0]//2:, :]  # Adjust or skip this line for full image
gray_img = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

# Step 3: Blur image to reduce noise before edge detection
gray_blurred = cv2.GaussianBlur(gray_img, (7, 7), 0)

# Step 4: Edge detection with stricter thresholds
edges = cv2.Canny(gray_blurred, 80, 200)  # Higher threshold to limit spurious edges

# Step 5: Morphological opening to clean up edge map (removes small objects)
kernel = np.ones((5, 5), np.uint8)
edges_clean = cv2.morphologyEx(edges, cv2.MORPH_OPEN, kernel)

# Step 6: Find contours
contours, _ = cv2.findContours(edges_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output_img = roi.copy()

for cnt in contours:
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    x, y, w, h = cv2.boundingRect(approx)
    aspect_ratio = float(w) / h if h != 0 else 0

    # Stricter filtering for mining pits (rectangles with larger area)
    if len(approx) == 4 and cv2.contourArea(cnt) > 1500 and aspect_ratio > 0.6 and aspect_ratio < 1.8:
        cv2.drawContours(output_img, [approx], -1, (0, 255, 0), 3)  # Green rectangles

    # Bulldozer/logging paths: higher minimum area, very elongated shapes
    elif (aspect_ratio > 5 or aspect_ratio < 0.2) and cv2.contourArea(cnt) > 1200:
        cv2.drawContours(output_img, [approx], -1, (255, 0, 0), 3)  # Blue long paths

# Step 7: Improved Hough Line detection (higher minLineLength, stricter threshold)
lines = cv2.HoughLinesP(edges_clean, 1, np.pi / 180, threshold=120, minLineLength=120, maxLineGap=8)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        # Ignore vertical lines (likely trees)
        if abs(x2 - x1) > 40:  # Only draw lines significantly non-vertical
            cv2.line(output_img, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Red lines

# Step 8: Overlay detection on original image
result_img = image.copy()
result_img[image.shape[0]//2:, :] = output_img  # If ROI is applied

cv2.imshow('Improved Illegal Activity Detection', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('illegal_activity_improved.png', result_img)

print("Improved illegal activity detection complete. See 'illegal_activity_improved.png'.")
