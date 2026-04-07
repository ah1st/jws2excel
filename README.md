# JWS to Excel Tool

Convert `.jws` and `.jwb` files into a single merged Excel file.

## Features

- Converts all JWS/JWB files to text.
- Merges wavelength & absorbance into one Excel file.
- Ready for plotting or analysis.

## Installation

Clone the repository:

```bash
git clone https://github.com/ah1st/jws2excel.git
cd jws2excel

Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

Install the package:

pip install .
Usage

Convert a folder of .jws or .jwb files into a merged Excel file:

python3 -m jws2excel.main --in-path /path/to/jws_folder --out-file /path/to/output.xlsx

Replace /path/to/jws_folder with your folder containing JWS/JWB files,
and /path/to/output.xlsx with the desired output Excel file path.

Optional: You can also use the helper script (if included) for convenience:

./run_jws2excel.sh /path/to/jws_folder /path/to/output.xlsx
Notes
Temporary .txt files are created in temp_txt during conversion.
Ensure you have write permissions to the output folder.
