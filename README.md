# ism2411-data-cleaning-copilot
# ISM2411 Data Cleaning with GitHub Copilot

This project cleans a messy sales dataset using Python and pandas.  
The script standardizes column names, fixes inconsistent formatting, handles missing values, and removes invalid rows.  
It produces a clean, analysis-ready CSV file stored in the `data/processed/` folder.

---

## 📁 Project Structure
ism2411-data-cleaning-copilot/
├── data/
│ ├── raw/
│ │ └── sales_data_raw.csv
│ └── processed/
│ └── sales_data_clean.csv
├── src/
│ └── data_cleaning.py
├── README.md
└── reflection.md

---

## 🧼 What the Script Does

The Python script performs the following tasks:

- Loads the raw sales CSV file  
- Standardizes column names  
- Strips extra spaces from product names and categories  
- Handles missing prices and quantities  
- Removes invalid rows (negative prices/quantities)  
- Saves the cleaned dataset to `data/processed/`  

---

## ▶️ How to Run the Script

From the project root folder, run:
python src/data_cleaning.py


When the script finishes, you will see:

- A message confirming the cleaning is complete  
- A new file created at:
data/processed/sales_data_clean.csv

---

## 🛠️ Tools Used

- Python  
- pandas  
- GitHub  
- GitHub Copilot  

Copilot was used to help generate several functions in the cleaning script, then modified and reviewed to match the assignment requirements.

---

## 📄 Reflection

See `reflection.md` for details about how Copilot was used and what I learned from this assignment.
