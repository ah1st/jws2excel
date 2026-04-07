from setuptools import setup, find_packages

setup(
    name="jws2excel",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
        "jws2txt"
    ],
    entry_points={
        "console_scripts": [
            "jws2excel=jws2excel.main:main"
        ]
    },
)
