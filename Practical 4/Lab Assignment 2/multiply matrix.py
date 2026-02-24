import numpy as np

# Input 5x3 matrix
print("Enter elements for 5x3 matrix (row-wise):")
matrix1 = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Input 3x2 matrix
print("Enter elements for 3x2 matrix (row-wise):")
matrix2 = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix2.append(row)

A = np.array(matrix1)
B = np.array(matrix2)

# Matrix multiplication
product = np.dot(A, B)

print("\nMatrix A (5x3):")
print(A)

print("\nMatrix B (3x2):")
print(B)

print("\nProduct Matrix (5x2):")
print(product)