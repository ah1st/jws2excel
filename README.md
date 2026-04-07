
````markdown
# JWS to Excel Tool

Convert `.jws` / `.jwb` files into a single merged Excel file.

## Clone the repository

```bash
git clone https://github.com/ah1st/jws2excel_project.git
cd jws2excel_project
````

## Installation

Create and activate a virtual environment, then install the package:

```bash
python3 -m venv venv
source venv/bin/activate
pip install .
```

## Usage

Activate the virtual environment (if not already):

```bash
source venv/bin/activate
```

Convert a folder of `.jws` or `.jwb` files to a merged Excel file:

```bash
python3 -m jws2excel.main --in-path /path/to/jws_folder --out-file /path/to/output.xlsx
```

Replace `/path/to/jws_folder` with your folder containing JWS/JWB files,
and `/path/to/output.xlsx` with the desired output Excel file path.

## Features

* Converts all JWS/JWB files to text
* Merges wavelength & absorbance into one Excel file
* Ready for plotting or analysis

```
