def multiply_matrices(matrix1, matrix2):
    """
    Function to multiply two matrices.

    Args:
        matrix1 (list): The first matrix.
        matrix2 (list): The second matrix.

    Returns:
        list: The result of matrix multiplication.
    """
    m = len(matrix1)
    n = len(matrix2[0])
    result = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
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


# Get the dimensions of the matrices from the user
m = int(input("Enter the number of rows for the first matrix: "))
n = int(input("Enter the number of columns for the first matrix and the number of rows for the second matrix: "))
p = int(input("Enter the number of columns for the second matrix: "))

# Get the matrices from the user
print("Enter the elements of the first matrix:")
matrix1 = get_matrix_from_user(m, n)
print("Enter the elements of the second matrix:")
matrix2 = get_matrix_from_user(n, p)

# Multiply the matrices
result = multiply_matrices(matrix1, matrix2)

# Print the resulting matrix
print_matrix(result, "Resultant Matrix")
