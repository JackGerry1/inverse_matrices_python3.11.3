import numpy as np

def get_matrix():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            while True:
                # Checks to make sure user input is valid, so no letters, blank or symbols.
                try:
                    value = float(input(f'Enter value for position [{i+1}, {j+1}]: '))
                    row.append(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        # if the user has entered valid values append the row to the array for every interation of the inner loop
        matrix.append(row)
    # convert the matrix array into a numpy array, so we gain access to other numpy methods
    return np.array(matrix)

# Formats the matrix so that if the number is an integer than we will add three zeros after the decimal point.
# Else we just round the number to 3 decimal places.
def format_matrix(x):
    if int(x) == x:
        return "{:.3f}".format(x) + "0" * 0
    else:
        return "{:.3f}".format(x)

# NumPy (2022c). 
# numpy.vectorize — NumPy v1.22 Manual. [Online] numpy.org. 
# Available at: https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html. [Accessed 31st January 2023].
# Modified By changing the variable names and how the format_matrix is created.
format_matrix = np.vectorize(format_matrix)

# Assign user_matrix to the returned value of the get_matrix function.
# user_matrix will be of type np.array due to the conversion within the get_matrix function.
user_matrix = get_matrix()

# NumPy (2022a). 
# numpy.linalg.det — NumPy v1.22 Manual. [Online] numpy.org. 
# Available at: https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html [Accessed 31st January 2023].
# Modified By adding a if statement to check if matrix is invertible by getting the determinat of the users matrix.
determinant = np.linalg.det(user_matrix)
if determinant == 0:
    print("The entered matrix is not invertible.")

else:
    # Print original matrix
    print("\nOriginal matrix:\n")
    formatted_matrix = format_matrix(user_matrix)
    # format the users original matrix so that it has only one [] at the start and end of the output.
    print(str(formatted_matrix).replace("[["," [").replace("]]","]"))

    # NumPy (2022b). 
    # numpy.linalg.inv — NumPy v1.20 Manual. [Online] numpy.org. 
    # Available at: https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html [Accessed 31st January 2023].
    # Modifed: By reformating the output and having the matrix being defined in the get_matrix function. 
    inverted_matrix = np.linalg.inv(user_matrix)
    
    # Print inverted matrix
    print("\nInverted matrix:\n")
    formatted_matrix = format_matrix(inverted_matrix)
    # format the users inverted matrix so that it has only one [] at the start and end of the output.
    print(str(formatted_matrix).replace("[["," [").replace("]]","]"))