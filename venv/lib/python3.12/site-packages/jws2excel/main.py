import argparse
import os
import subprocess
from .merge import merge_txt_files

def main():
    parser = argparse.ArgumentParser(description="Convert JWS/JWB files to merged Excel")
    parser.add_argument("--in-path", required=True, help="Input folder with .jws/.jwb")
    parser.add_argument("--out-file", required=True, help="Output Excel file")
    args = parser.parse_args()

    temp_folder = os.path.join(args.in_path, "temp_txt")
    os.makedirs(temp_folder, exist_ok=True)

    print("Converting files...")
    subprocess.run([
        "jws2txt",
        "--in-path", args.in_path,
        "--out-dir", temp_folder
    ], check=True)

    print("Merging to Excel...")
    merge_txt_files(temp_folder, args.out_file)
    print("Done:", args.out_file)

if __name__ == "__main__":
    main()
