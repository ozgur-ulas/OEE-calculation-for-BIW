# 📘 OEE Calculation for BIW Production Lines (Renault Models) #

This repository provides a complete framework for calculating and analyzing Overall Equipment Effectiveness (OEE) across Body‑in‑White (BIW) production lines manufacturing multiple Renault vehicle models.
It includes methodology, data structures, Python scripts, notebooks, and templates for dashboards.

🚗 1. Project Overview
The BIW shop produces four Renault models:

- Clio 4 Hatchback (HB)
- Clio 4 Station Wagon (SW)
- Clio 5
- Megane 4

The production architecture includes:
- 1 Underbody line
- 2 Bodyside lines
- 4 Doors lines (merging into main line)
- 1 Main connection line
- 1 Doors connection line
- 1 Rework & final check line

🏭 2. BIW Production Flow
This project calculates OEE for each line and for the full BIW flow, considering model mix, cycle times, downtime, and quality losses.

<img width="540" height="517" alt="image" src="https://github.com/user-attachments/assets/bdbaa9dd-7185-4b2e-a515-143ce7c5594d" />

📊 3. OEE Methodology
OEE is calculated using the standard formula:

<img width="566" height="444" alt="image" src="https://github.com/user-attachments/assets/96604eb3-9af8-438b-93d8-1ffdf0d2a71f" />

🧩 4. Required Data Inputs
Production Data
- Total units produced per line
- Good units vs. rework/scrap
- Model mix per shift

Cycle Time Data
- Ideal cycle time per model
- Line‑specific cycle time differences

Downtime Data
- Breakdown events
- Micro‑stops
- Planned vs. unplanned downtime

Shift Calendar
- Planned production time
- Breaks, meetings, maintenance windows

🗂️ 5. Repository Structure

<img width="367" height="530" alt="image" src="https://github.com/user-attachments/assets/6fa6c649-7c30-4e50-93c0-6e9e9f401a94" />

🧮 6. How to Use the Python Scripts

- Install dependencies --> pip install -r requirements.txt
- Run OEE calculation --> python src/oee_calculator.py
- Run Jupyter notebook --> jupyter notebook notebooks/OEE_Analysis.ipynb

📈 7. Example Outputs
- OEE per line
- OEE per model
- Loss breakdown (Availability / Performance / Quality)
- Model‑mix impact on cycle time
- BIW bottleneck identification
- Power BI dashboard template

🛠️ 8. Future Improvements
- Real‑time MES integration
- Predictive downtime classification
- Machine learning for OEE forecasting
- Digital twin simulation for model‑mix optimization
