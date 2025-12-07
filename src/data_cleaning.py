try:
    import pandas as pd
except ImportError:
    raise ImportError("pandas is not installed. Run: python3 -m pip install pandas --upgrade")

def clean_sales_data():
    # Load raw data
    df = pd.read_csv("data/raw/sales_raw.csv")

    # --- BASIC CLEANING ---

    # Strip spaces + lowercase product/category
    df["ProdName"] = df["ProdName"].str.strip().str.lower()
    df["CATEGORY"] = df["CATEGORY"].str.strip().str.lower()

    # Fix extra spaces inside names
    df["ProdName"] = df["ProdName"].str.replace("  ", " ", regex=False)

    # Remove negative quantities
    df["qty"] = df["qty"].apply(lambda x: max(x, 0) if pd.notnull(x) else x)

    # Replace missing prices with 0
    df["Price"] = df["Price"].fillna(0)

    # Replace missing quantities with 0
    df["qty"] = df["qty"].fillna(0)

    # Remove rows with no date
    df = df.dropna(subset=["date_sold"])

    # Remove duplicates
    df = df.drop_duplicates()

    # --- SAVE CLEANED DATA ---
    df.to_csv("data/processed/sales_clean.csv", index=False)
    print("Cleaning complete! File saved to data/processed/sales_clean.csv")

if __name__ == "__main__":
    clean_sales_data()
