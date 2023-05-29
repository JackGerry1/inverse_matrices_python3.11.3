def get_matrix():
    """
    This Functions asks the user for input, which is added to the rows and columns of a matrix.

    Returns: 
        A list, which represents the rows and columns of the matrix. 
    """
    # Initialize an empty list to store the matrix
    matrix = []  
    # Loop over 3 rows
    for i in range(3):
        # Initialize an empty list to store the current row
        row = []        
        # Loop over 3 columns
        for j in range(3):
            # Keep asking for input until a valid number is entered
            while True:
                try:
                    value = float(input(f'Enter value for position [{i+1}, {j+1}]: '))
                    # Add the value to the current row
                    row.append(value)
                    # Break the loop once a valid number is entered
                    break
                except ValueError:
                    # If the input is not a valid number, print an error message, whilst staying at the current matrix position.
                    print("Invalid input. Please enter a valid number.")
        # Add the current row to the matrix
        matrix.append(row)
    # Return the matrix
    return matrix

def format_matrix(x):
    """
    This function formats the user matrix to make sure the value has three digits after the decimal place.

    Arguments:
        x: A number specifed by the user. 
    Returns: 
        All of the numbers reformated to have 3 decimal places.    
    """
    # Check if the number is an integer
    if int(x) == x:
        # If it is an integer, format it with 3 decimal places, and add zeros to the right of the decimal
        return "{:.3f}".format(x) + "0" * 0
    else:
        # If it is not an integer, format it with 3 decimal places
        return "{:.3f}".format(x)

def get_minor(matrix, row, col):
    """
    This function returns the minor of a given matrix by removing the specified row and column.
    
    Arguments:
        matrix: A list of lists representing the matrix entered by the user
        row: An integer indicating the row to be removed
        col: An integer indicating the column to be removed
        
    Returns:
        A list of lists representing the minor of the original matrix with the specified row and column removed.
    """
    minor = []
    # loop through the rows of the matrix
    for i in range(len(matrix)):
        # skip the row specified by the argument
        if i == row:
            continue
        row_elements = []
        # loop through the columns of the matrix
        for j in range(len(matrix[0])):
            # skip the column specified by the argument
            if j == col:
                continue
            # add the element from the current row and column to the row_elements list
            row_elements.append(matrix[i][j])
        # add the row_elements list to the minor matrix
        minor.append(row_elements)
    # return the minor matrix
    return minor

def get_determinant(matrix):
    """
    This function calculates the determinant of the given matrix.

    Arguments:
        matrix: A list of lists representing the matrix entered by the user
        
    Returns:
    A float or integer depending on the value of the determinant.
    """
    # Check if the matrix is 2x2
    if len(matrix) == 2:
        # If it is 2x2, return the determinant calculation for 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    
    # Initialize the determinant value
    determinant = 0

    # Iterate over the elements of the first row of the matrix
    for i in range(len(matrix)):
        # Calculate the determinant by adding the product of each element and its corresponding minor
        determinant += (-1)**i * matrix[0][i] * get_determinant(get_minor(matrix, 0, i))
    
    # Return the determinant
    return determinant

def get_cofactor_matrix(matrix):
    """
    Calculates the cofactor matrix of a given matrix.
    
    Arguments:
        matrix: A list of lists representing the matrix entered by the user
        
    Returns:
    The cofactor_matrix, which has values based on the values in the matrix entered by the user. 
    """
    cofactor_matrix = []
    # Iterate through each row of the matrix
    for i in range(len(matrix)):
        row = []
        # Iterate through each element of the row
        for j in range(len(matrix[0])):
            # Get the minor of the current element
            minor = get_minor(matrix, i, j)
            # Calculate the cofactor of the current element using the minor and the sign calculated from i and j
            row.append((-1)**(i+j) * get_determinant(minor))
        # Add the row to the cofactor matrix
        cofactor_matrix.append(row)
    return cofactor_matrix

def get_inverted_matrix(matrix):
    """
    Calculates the inverse of the matrix.
    
    Arguments:
        matrix: A list of lists representing the matrix entered by the user
        
    Returns:
    The inverted_matrix, which has values based on the values in the matrix entered by the user. 
    """
    # calculate the determinant of the matrix
    determinant = get_determinant(matrix)
    # check if the matrix is invertible, if not return None   
    if determinant == 0:
        return None
    else:
        # get the cofactor matrix of the given matrix
        cofactor_matrix = get_cofactor_matrix(matrix)
        # calculate the inverted matrix
        inverted_matrix = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                # each element of the inverted matrix is the cofactor of the corresponding element in the cofactor matrix, divided by the determinant
                row.append(cofactor_matrix[j][i] / determinant)
            inverted_matrix.append(row)
        return inverted_matrix

# Get the matrix input from the user
user_matrix = get_matrix()

# Calculate the determinant of the input matrix
determinant = get_determinant(user_matrix)
# If the determinant is non-zero, the matrix is invertible
if determinant:
    # Print the original matrix
    print("\nOriginal matrix:\n")
    formatted_matrix = [list(map(format_matrix, row)) for row in user_matrix]
    for row in formatted_matrix:
        print(row)

    # Get the inverted matrix
    inverted_matrix = get_inverted_matrix(user_matrix)

    # Print the inverted matrix
    print("\nInverted matrix:\n")
    formatted_matrix = [list(map(format_matrix, row)) for row in inverted_matrix]
    for row in formatted_matrix:
        print(row)
else:
    print("\nThe entered matrix was not invertible")