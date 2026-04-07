import os
import pandas as pd

def merge_txt_files(txt_folder, output_excel):
    dataframes = []
    for file in sorted(os.listdir(txt_folder)):
        if file.endswith(".txt"):
            path = os.path.join(txt_folder, file)
            try:
                with open(path, "r") as f:
                    lines = f.readlines()
                start = 0
                for i, line in enumerate(lines):
                    if "WAVELENGTH" in line and "ABSORBANCE" in line:
                        start = i
                        break
                df = pd.read_csv(
                    path,
                    sep="\t",
                    skiprows=start,
                    engine="python"
                )
                df = df[["WAVELENGTH", "ABSORBANCE"]].copy()
                df["WAVELENGTH"] = pd.to_numeric(df["WAVELENGTH"], errors="coerce")
                df["ABSORBANCE"] = pd.to_numeric(df["ABSORBANCE"], errors="coerce")
                name = os.path.splitext(file)[0]
                df.columns = ["WAVELENGTH", f"ABS_{name}"]
                dataframes.append(df)
            except Exception as e:
                print(f"Error in {file}: {e}")
    if not dataframes:
        raise ValueError("No valid data found!")
    merged = dataframes[0]
    for df in dataframes[1:]:
        merged = pd.merge(merged, df, on="WAVELENGTH", how="outer")
    merged = merged.sort_values("WAVELENGTH")
    merged.to_excel(output_excel, index=False)
