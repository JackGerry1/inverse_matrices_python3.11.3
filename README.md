# Matrix Inversion

This repository contains two Python scripts, `inverse_matrix.py` and `inverse_matrix_numpy.py`, that calculate the inverse of a matrix entered by the user.

## inverse_matrix.py

This script prompts the user to enter a 3x3 matrix and calculates its inverse using custom functions. It follows the following steps:

1. The user is asked to enter the values for each position in the matrix.
2. The matrix is created and stored as a list of lists.
3. The determinant of the matrix is calculated using recursive functions.
4. If the determinant is non-zero (indicating an invertible matrix), the original matrix and the inverted matrix are printed.

## inverse_matrix_numpy.py

This script follows a similar process as `inverse_matrix.py`, but it utilizes the NumPy library to simplify the calculations. The steps are as follows:

1. The user is prompted to enter the values for each position in the matrix.
2. The matrix is created as a NumPy array.
3. The determinant of the matrix is calculated using the `np.linalg.det()` function.
4. If the determinant is non-zero, the original matrix and the inverted matrix are printed using NumPy's `np.linalg.inv()` function.

Both scripts format the output matrices to ensure three decimal places are displayed.

## Usage

1. Run `inverse_matrix.py` or `inverse_matrix_numpy.py` using a Python interpreter.
2. Follow the prompts to enter the values for each position in the matrix.
3. View the output, which includes the original matrix and its inverted form if the matrix is invertible.

Note: For `inverse_matrix_numpy.py`, make sure you have NumPy installed on your system. You can install it using `pip install numpy`.

Feel free to explore and experiment with these scripts to calculate the inverse of different matrices.

