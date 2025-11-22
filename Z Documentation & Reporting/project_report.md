# Forest Monitoring & Risk Layer Project

## Project Summary
- Burned area detected and quantified
- Change detection mapped
- Risk layer generated and ownership overlay completed

## Key Statistics
- **Total burned area:** 41.18% of image
- **Risky area on government land:** 233 pixels
- **Risky area on private land:** 184 pixels

## Outputs
- [project_summary.png](project_summary.png): Visual overview (burn/chg/ownership)
- [govt_risk_mask.csv](govt_risk_mask.csv): Risk mask (govt parcels)
- [private_risk_mask.csv](private_risk_mask.csv): Risk mask (private parcels)

## Methodology
1. Preprocessed images and extracted burned areas
2. Detected change zones by differencing
3. Generated risk map by fusing all detection results
4. Overlaid ownership to identify at-risk parcels
5. Automated summary report generation for review and handover

---
**Prepared automatically by Python scripts for final submission.**
