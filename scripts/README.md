# Scripts Folder

This directory contains the core logic for the **Integrated Retail Sales Performance Tracking and Analysis** project.

## Contents
* **retail_analysis.py**: The primary Python script used for Step 1 (Data Pre-processing) and Step 2 (Predictive Analytics).

## Logic Flow
1. **Data Pre-processing**: Handles missing values, standardizes date formats, and creates derived columns like `Total_Amount`.
2. **Predictive Analytics**: Implements Random Forest for sales forecasting and K-Means for customer segmentation.
3. **Data Export**: Generates `cleaned_retail_data.csv` for integration with Power BI/Tableau.
