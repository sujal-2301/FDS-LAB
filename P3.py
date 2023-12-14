import numpy as np

def print_menu():
    print("\nMatrix Operations Menu:")
    print("a) Addition of two matrices")
    print("b) Subtraction of two matrices")
    print("c) Multiplication of two matrices")
    print("d) Transpose of a matrix")
    print("e) Exit")

def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    return np.multiply(matrix1, matrix2)

def transpose_matrix(matrix):
    return np.transpose(matrix)

# Initializing two matrices
matrix_A = np.array([[1, 5], [3, 2]])
matrix_B = np.array([[3, 5], [7, 1]])

while True:
    print("\nThe matrix A is:\n", matrix_A)
    print("The matrix B is:\n", matrix_B)
    
    print_menu()
    choice = input("Enter your choice (a, b, c, d, e): ").lower()

    if choice == 'a':
        print("The addition of the two matrices is:\n", add_matrices(matrix_A, matrix_B))
    elif choice == 'b':
        print("The subtraction of two matrices is:\n", subtract_matrices(matrix_A, matrix_B))
    elif choice == 'c':
        print("The multiplication of the two matrices is:\n", multiply_matrices(matrix_A, matrix_B))
    elif choice == 'd':
        print("The transpose of the matrix A is:\n", transpose_matrix(matrix_A))
        print("The transpose of the matrix B is:\n", transpose_matrix(matrix_B))
    elif choice == 'e':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
