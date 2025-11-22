import cv2
import numpy as np

# Step 1: Load Image
image = cv2.imread('after_preprocessed.png')
if image is None:
    raise ValueError("Image file 'after_preprocessed.png' not found.")

# Step 2: Grayscale & Blur to reduce noise
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 3: Adaptive Edge Detection
edges = cv2.Canny(blur, 50, 150)

# For debugging: Show edge map—trails should show as bold lines
cv2.imshow("Edge Map", edges)
cv2.waitKey(500)  # Show briefly

# Step 4: (Optional but recommended) Morphological Close to connect broken edges
kernel = np.ones((5, 5), np.uint8)
edges_clean = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# Step 5: Hough Line Transform with permissive settings
lines = cv2.HoughLinesP(
    edges_clean, 
    1, 
    np.pi / 180, 
    threshold=50,           # Lower: more lines
    minLineLength=50,       # Lower: shorter trails
    maxLineGap=20           # Higher: allows gaps
)

output_img = image.copy()
trail_count = 0

# Step 6: Draw all lines for review, then filter by angle & length if needed
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))

        # Main road and burnt area boundary may be detected; filter near-horizontal trails
        if length > 40 and (-60 < angle < 60):
            cv2.line(output_img, (x1, y1), (x2, y2), (255, 0, 0), 3)
            trail_count += 1

# Step 7: Show and save outputs
cv2.imshow("Path/Trail Detection Output", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("path_trail_detected.png", output_img)
print(f"Detection complete! Paths/trails found: {trail_count}. See 'path_trail_detected.png'.")

# Optional: Save edge map for report
cv2.imwrite("edge_map.png", edges)
