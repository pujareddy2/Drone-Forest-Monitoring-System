import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load all relevant masks/overlays
# Ensure these files exist from previous modules; otherwise adjust filenames
burn_severity = cv2.imread('burn_severity_map.png', 0)            # Fire/Burn severity (grayscale)
illegal_activity = cv2.imread('illegal_activity_detected.png', 0)  # Illegal pattern mask (grayscale or color)
change_mask = cv2.imread('change_mask.png', 0)                     # Change detection mask (grayscale)
path_trail = cv2.imread('path_trail_detected.png', 0)              # Path/trail detection (grayscale)

# Step 2: Standardize resolutions
target_size = (burn_severity.shape[1], burn_severity.shape[0])
illegal_activity = cv2.resize(illegal_activity, target_size)
change_mask = cv2.resize(change_mask, target_size)
path_trail = cv2.resize(path_trail, target_size)

# Step 3: Convert all masks to binary (threshold)
_, burn_mask = cv2.threshold(burn_severity, 40, 1, cv2.THRESH_BINARY)
_, illegal_mask = cv2.threshold(illegal_activity, 40, 1, cv2.THRESH_BINARY)
_, change_mask_bin = cv2.threshold(change_mask, 40, 1, cv2.THRESH_BINARY)
_, trail_mask = cv2.threshold(path_trail, 40, 1, cv2.THRESH_BINARY)

# Step 4: Combine layers with weighted sum (customize weights if desired)
# Burn and illegal may have greatest impact; adjust as needed for your project
risk_layer = (burn_mask * 2 +
              illegal_mask * 2 +
              change_mask_bin * 1 +
              trail_mask * 1)

# Step 5: Clip risk level (for visualization) and normalize to 0-5
risk_layer_norm = np.clip(risk_layer, 0, 5)

# Step 6: Visualize as a heatmap (useful for your dashboard or presentation)
plt.figure(figsize=(8, 6))
plt.imshow(risk_layer_norm, cmap='hot', interpolation='nearest')
plt.title("Composite Risk Layer")
plt.colorbar(label="Risk Level")
plt.tight_layout()
plt.show()

# Step 7: Save risk map as image and CSV
cv2.imwrite('risk_layer_composite.png', (risk_layer_norm * 50).astype(np.uint8))  # Multiplied for color depth
np.savetxt('risk_layer_composite.csv', risk_layer_norm, delimiter=',')

# Step 8: Print summary/report in console
print("Risk Layer Generation - Complete Summary")
print("------------------------------------------------")
unique, counts = np.unique(risk_layer_norm, return_counts=True)
for r, c in zip(unique, counts):
    print(f"Risk score {int(r)}: {c} pixels")

print("\nComposite risk layer saved as 'risk_layer_composite.png' and 'risk_layer_composite.csv'.")
print("Ready for dashboard integration and final reporting!")
