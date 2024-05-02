def transpose_matrix(matrix):
    """
    Function to transpose a given matrix.

    Args:
        matrix (list): The matrix to be transposed.

    Returns:
        list: The transposed matrix.
    """
    m = len(matrix)  # Number of rows in the original matrix
    n = len(matrix[0])  # Number of columns in the original matrix
    transpose = [[0 for _ in range(m)] for _ in range(n)]  # Initialize the transposed matrix with zeros

    # Iterate over each element in the original matrix and transpose it
    for i in range(n):
        for j in range(m):
            transpose[i][j] = matrix[j][i]  # Swap rows and columns

    return transpose


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
    print(f"Enter the elements of the matrix ({rows}x{cols}), row by row:")
    for i in range(rows):
        row = []
        for j in range(cols):
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
    print(label + ":")
    for row in matrix:
        print(row)


# Get the dimensions of the matrix from the user
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

# Get the matrix from the user
print("Enter the elements of the matrix:")
matrix = get_matrix_from_user(m, n)

# Transpose the matrix
transposed_matrix = transpose_matrix(matrix)

# Print the transposed matrix
print_matrix(transposed_matrix, "Transposed Matrix")
