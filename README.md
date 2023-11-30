# Ternary Plot with Experimental Data

This repository contains code to generate a ternary plot using Python's Matplotlib library, showcasing experimental data related to chemical compositions.

## Overview

The script `ternary_plot.py` utilizes Matplotlib and mpltern libraries to create a ternary plot. It visualizes experimental data points representing the composition of a mixture involving acetic acid, water, and butyl acetate. The plot helps in understanding the relationships and distribution of these components within the mixture.

## Requirements

To run the script, the following libraries are required:
- NumPy
- Pandas
- Matplotlib
- mpltern

## Usage

1. Ensure all necessary libraries are installed.
2. Prepare your data in Excel format:
   - `veriler.xlsx`: Contains experimental data.
   - `labveri.xlsx`: Additional laboratory data for comparison.
3. Run the `ternary_plot.py` script.
4. The generated plot displays the experimental and laboratory data points in a ternary diagram.

## Code Structure

- `ternary_plot.py`: Python script generating the ternary plot.
- `mpltern.datasets`: Module providing triangular grid generation for the ternary plot.

## How to Run

Execute the `ternary_plot.py` script by running the following command:

```bash
python ternary_plot.py


# Additional Ternary Plot with Tie Lines

The repository also includes an additional script `tie_line_plot.py` to create a ternary plot showcasing tie lines for specific data points.

## Overview

The `tie_line_plot.py` script utilizes Matplotlib, mpltern, NumPy, and Pandas libraries to create a ternary plot. It visualizes experimental data points representing the composition of a mixture involving acetic acid, water, and butyl acetate, including tie lines.

## Requirements

The following libraries are required to run the script:
- NumPy
- Pandas
- Matplotlib
- mpltern

## Usage

1. Ensure all necessary libraries are installed.
2. Prepare your data in Excel format:
   - `tielinedahilveri.xlsx`: Contains data for tie lines.
   - `labveri.xlsx`: Additional laboratory data for comparison.
3. Run the `tie_line_plot.py` script.
4. The generated plot displays tie lines along with given data and laboratory data points in a ternary diagram.

## Code Structure

- `tie_line_plot.py`: Python script generating the ternary plot with tie lines.
- `mpltern.datasets`: Module providing triangular grid generation for the ternary plot.

## How to Run

Execute the `tie_line_plot.py` script by running the following command:

```bash
python tie_line_plot.py

