def add_matrices(matrix1, matrix2):
    """
    Function to add two matrices element-wise.

    Args:
        matrix1 (list): The first matrix.
        matrix2 (list): The second matrix.

    Returns:
        list: The result matrix after addition.
            Returns None if matrices have different dimensions.
    """
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions")
        return None

    # Initialize the result matrix
    result = []

    # Iterate over rows of matrices
    for i in range(len(matrix1)):
        row = []
        # Iterate over columns of matrices
        for j in range(len(matrix1[0])):
            # Add corresponding elements of matrices
            row.append(matrix1[i][j] + matrix2[i][j])
        # Append row to result matrix
        result.append(row)

    return result


def get_matrix_from_user(rows, cols):
    """
    Function to get a matrix from the user.

    Args:
        rows (int): Number of rows in the matrix.
        cols (int): Number of columns in the matrix.

    Returns:
        list: The matrix entered by the user.
    """
    matrix = []
    # Prompt user to enter elements of the matrix
    print(f"Enter the elements of the matrix ({rows}x{cols}), row by row:")
    for i in range(rows):
        row = []
        for j in range(cols):
            # Get element from the user
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    return matrix


def print_matrix(matrix, label="Matrix"):
    """
    Function to print a matrix.

    Args:
        matrix (list): The matrix to be printed.
        label (str): Label for the matrix. Default is "Matrix".
    """
    # Print the matrix with the given label
    print(label + ":")
    for row in matrix:
        print(row)


# Get the dimensions of the matrices from the user
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

# Get the matrices from the user
print("Enter the elements of the first matrix:")
matrix1 = get_matrix_from_user(m, n)
print("Enter the elements of the second matrix:")
matrix2 = get_matrix_from_user(m, n)

# Add the matrices
result = add_matrices(matrix1, matrix2)
if result:
    # Print the resultant matrix
    print_matrix(result, "Resultant Matrix")
