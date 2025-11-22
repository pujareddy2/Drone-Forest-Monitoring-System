import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Load "before" and "after" images ---
before_img = cv2.imread('before_preprocessed.png').astype(np.float32)
after_img = cv2.imread('after_preprocessed.png').astype(np.float32)

if before_img is None or after_img is None:
    raise ValueError("Make sure 'before_preprocessed.png' and 'after_preprocessed.png' exist in folder.")

# --- Step 2: Define proxy NDVI calculation (using green and red channels) ---
def proxy_ndvi(image):
    green = image[:, :, 1]
    red = image[:, :, 2]
    ndvi = (green - red) / (green + red + 1e-6)  # Adding epsilon to avoid division by zero
    return ndvi

before_ndvi = proxy_ndvi(before_img)
after_ndvi = proxy_ndvi(after_img)

# --- Step 3: Calculate Burn Severity (difference NDVI before - after) ---
burn_severity = before_ndvi - after_ndvi

# Clamp values for visualization and computation
burn_severity_clamped = np.clip(burn_severity, 0, 1)

# --- Step 4: Classify burn severity into levels ---
light_burn = (burn_severity_clamped > 0.1) & (burn_severity_clamped <= 0.3)
moderate_burn = (burn_severity_clamped > 0.3) & (burn_severity_clamped <= 0.6)
severe_burn = burn_severity_clamped > 0.6

# --- Step 5: Calculate Recovery Potential score (inverse of burn severity) ---
recovery_score = 1.0 - burn_severity_clamped

# --- Step 6: Display formulation and metrics ---
print("Formulas used:")
print("Proxy NDVI = (Green - Red) / (Green + Red)")
print("Burn Severity = NDVI_before - NDVI_after")
print("Recovery Score = 1 - Burn Severity\n")

# Numerical summaries
print(f"Average Burn Severity: {np.mean(burn_severity_clamped):.4f}")
print(f"Light Burn Area (pixels): {np.sum(light_burn)}")
print(f"Moderate Burn Area (pixels): {np.sum(moderate_burn)}")
print(f"Severe Burn Area (pixels): {np.sum(severe_burn)}")
print(f"Average Recovery Score: {np.mean(recovery_score):.4f}")

# --- Step 7: Visualizations for report/presentation ---
plt.figure(figsize=(15,6))

plt.subplot(1, 3, 1)
plt.title('Burn Severity Map')
plt.imshow(burn_severity_clamped, cmap='hot')
plt.colorbar()

plt.subplot(1, 3, 2)
plt.title('Burn Severity Classification')
severity_class_map = np.zeros(burn_severity_clamped.shape)
severity_class_map[light_burn] = 0.33
severity_class_map[moderate_burn] = 0.66
severity_class_map[severe_burn] = 1.0
plt.imshow(severity_class_map, cmap='inferno')
plt.colorbar(ticks=[0,0.33,0.66,1], label='Severity Level')
plt.clim(0,1)

plt.subplot(1, 3, 3)
plt.title('Recovery Potential Map')
plt.imshow(recovery_score, cmap='Greens')
plt.colorbar()

plt.tight_layout()
plt.show()

# --- Step 8: Save maps for final report ---
cv2.imwrite('burn_severity_map.png', (burn_severity_clamped * 255).astype(np.uint8))
cv2.imwrite('burn_severity_classification.png', (severity_class_map * 255).astype(np.uint8))
cv2.imwrite('recovery_potential_map.png', (recovery_score * 255).astype(np.uint8))

print("\nOutputs saved as burn_severity_map.png, burn_severity_classification.png, recovery_potential_map.png")
print("Burn Severity & Recovery Scoring task complete! Review visuals and printed metrics above.")
