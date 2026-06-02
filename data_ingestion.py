import pandas as pd
import os

DATA_FOLDER = "data/raw"

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

print(f"Found {len(csv_files)} CSV files")

for file in csv_files:
    print("\n" + "="*80)
    print(f"FILE: {file}")

    path = os.path.join(DATA_FOLDER, file)

    try:
        df = pd.read_csv(path)

        print("\nShape:")
        print(df.shape)

        print("\nDtypes:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error loading {file}: {e}")