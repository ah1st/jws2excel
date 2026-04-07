# JWS to Excel Tool

Convert `.jws` or `.jwb` files into a single merged Excel file.

## Installation

Clone this repository:

```bash
git clone https://github.com/ah1st/jws2excel_project.git
cd jws2excel_project
python3 -m venv venv
source venv/bin/activate
pip install .
Usage
python3 -m jws2excel.main --in-path /path/to/jws_files --out-file /path/to/merged.xlsx
Features
Converts all JWS/JWB files to text
Merges wavelength & absorbance into one Excel file
Ready for plotting or analysis

