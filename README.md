JWS to Excel Tool

Convert `.jws` and `.jwb` files into a single merged Excel file for easy analysis.

## Features

* Converts all JWS/JWB files to text.
* Merges wavelength and absorbance data into a single Excel sheet.
* Ready for plotting or further analysis.
* Clean and lightweight, works with Python 3.12+.

## Installation

Clone the repository and set up the virtual environment:

```bash
git clone https://github.com/ah1st/jws2excel.git
cd jws2excel
python3 -m venv venv
source venv/bin/activate
pip install --upgrade --force-reinstall .
```

> **Note:** The virtual environment `venv/` is ignored in Git thanks to `.gitignore`.

## Usage

Activate the virtual environment (if not already active):

```bash
source venv/bin/activate
```

Convert a folder of `.jws` or `.jwb` files to a merged Excel file:

```bash
python3 -m jws2excel.main --in-path /path/to/jws_folder --out-file /path/to/output.xlsx
```

Replace `/path/to/jws_folder` with your folder containing the JWS/JWB files,
and `/path/to/output.xlsx` with the desired path for the merged Excel file.

### Example

```bash
python3 -m jws2excel.main --in-path /home/mo/jws_test --out-file /home/mo/jws_test/merged.xlsx
```

This will create a single Excel file `merged.xlsx` in your target folder.

## Requirements

* Python 3.12+
* Dependencies are automatically installed via `pip install .`:

  * `pandas`
  * `openpyxl`
  * `jws2txt`

## Development Notes

* Temporary `.txt` files are created during conversion in the same folder.
* Existing temp files may be overwritten; the tool will report warnings if files exist.

---
