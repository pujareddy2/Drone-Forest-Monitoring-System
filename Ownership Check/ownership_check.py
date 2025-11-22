import cv2
import numpy as np

# Step 1: Load risk layer and ownership mask
risk_layer = cv2.imread('risk_layer_composite.png', 0)        # Final risk map (grayscale)
ownership_mask = cv2.imread('ownership_mask.png', 0)          # Ownership mask: 1=Govt, 2=Private

if risk_layer is None or ownership_mask is None:
    raise ValueError("Check that 'risk_layer_composite.png' and 'ownership_mask.png' are present in the folder.")

# Step 2: Resize ownership mask to match risk layer
ownership_mask = cv2.resize(ownership_mask, (risk_layer.shape[1], risk_layer.shape[0]))

# Step 3: Threshold risk layer (returns binary: risky = 1, non-risky = 0)
_, risk_binary = cv2.threshold(risk_layer, 40, 1, cv2.THRESH_BINARY)

# Step 4: Find risky pixels for government and private land
govt_risk = np.where((ownership_mask == 1) & (risk_binary == 1), 1, 0)
private_risk = np.where((ownership_mask == 2) & (risk_binary == 1), 1, 0)

govt_count = int(np.sum(govt_risk))
private_count = int(np.sum(private_risk))
print(f"\nRisky area on Govt land  : {govt_count} pixels")
print(f"Risky area on Private land: {private_count} pixels\n")

# Step 5: Visualize risky areas by ownership (Govt=Blue, Private=Red, Other=Gray)
# Convert original image to color (for visualization)
ownership_vis = np.zeros((risk_layer.shape[0], risk_layer.shape[1], 3), dtype=np.uint8)
ownership_vis[:] = [80, 80, 80]  # Background gray

ownership_vis[govt_risk == 1] = [255, 0, 0]      # Govt risk = Blue
ownership_vis[private_risk == 1] = [0, 0, 255]   # Private risk = Red

cv2.imshow("Ownership Risk Map", ownership_vis)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("ownership_risk_visualization.png", ownership_vis)

# Step 6: Save CSV result for further statistics/reporting
np.savetxt('govt_risk_mask.csv', govt_risk, delimiter=',', fmt='%d')
np.savetxt('private_risk_mask.csv', private_risk, delimiter=',', fmt='%d')

print("Ownership-based risk visualization saved as 'ownership_risk_visualization.png'.")
print("Govt and Private risk CSV masks saved as 'govt_risk_mask.csv' and 'private_risk_mask.csv'.")
print("Ownership-linked reporting complete!")

