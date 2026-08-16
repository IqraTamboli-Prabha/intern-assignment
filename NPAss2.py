#Question 1
#Create an array containing numbers from 1 to 20.
#Display the first element.
import numpy as np
print("\nQ1:")
arr = np.arange(5, 25)
print(arr)
print("First element:", arr[0])

#Question 2
#Display the last element using negative indexing.
print("\nQ2:")
print("Last element:", arr[-1])

#Question 3
#Display the third element of an array.
print("\nQ3:")
print("Third element:", arr[2])

#Question 4
#Display the last five elements using slicing.
print("\nQ4:")
print("Last five elements:", arr[-5:])

#Question 5
#Display elements from index 3 to 8.
print("\nQ5:")
print("Elements from index 3 to 8:", arr[3:9])

#Question 6
#Create a 4 × 4 matrix.
#Display the first row.
print("\nQ6:")
matrix = np.array([
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34],
    [41, 42, 43, 44]
])
print(matrix)
print("First row:", matrix[0])

#Question 7
#Display the last row of the matrix.
print("\nQ7:")
print("Last row:", matrix[-1])

#Question 8
#Display the first column.
print("\nQ8:")
print("First column:", matrix[:, 0])

#Question 9
#Display the last column.
print("\nQ9:")
print("Last column:", matrix[:, -1])

#Question 10
#Display the middle two rows.
print("\nQ10:")
print("Middle two rows:")
print(matrix[1:3])

import numpy as np

# Create a 4 × 4 matrix for Q11–Q13
matrix = np.array([
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34],
    [41, 42, 43, 44]
])

#Question 11
#Display the middle two columns.
print("\nQ11:")
print("Middle two columns:")
print(matrix[:, 1:3])

#Question 12
#Display the first 2 × 2 sub-matrix.
print("\nQ12:")
print("First 2 × 2 sub-matrix:")
print(matrix[0:2, 0:2])

#Question 13
#Display the last 2 × 2 sub-matrix.
print("\nQ13:")
print("Last 2 × 2 sub-matrix:")
print(matrix[2:4, 2:4])

#Question 14
#Create a 3D array and display the first matrix.
print("\nQ14:")
arr3d = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])
print("First matrix:")
print(arr3d[0])

#Question 15
#Display the second matrix of a 3D array.
print("\nQ15:")
print("Second matrix:")
print(arr3d[1])

#Question 16
#Display a specific element from a 3D array.
print("\nQ16:")
print("Specific element:", arr3d[1, 0, 2])

#Question 17
#Create an array from 1 to 20.
#Display only even numbers using Boolean Indexing.
print("\nQ17:")
arr = np.arange(1, 21)
print("Even numbers:")
print(arr[arr % 2 == 0])

#Question 18
#Display only odd numbers using Boolean Indexing.
print("\nQ18:")
print("Odd numbers:")
print(arr[arr % 2 != 0])

#Question 19
#Display numbers greater than 10 using Boolean Indexing.
print("\nQ19:")
print("Numbers greater than 10:")
print(arr[arr > 10])

#Question 20
#Display numbers less than 15 using Boolean Indexing.
print("\nQ20:")
print("Numbers less than 15:")
print(arr[arr < 15])

#Question 21
#Use Fancy Indexing to display elements at index positions:
#0, 2, 4, 6
import numpy as np

print("\nQ21:")
arr = np.array([10, 20, 30, 40, 50, 60, 70])
print("Elements at index 0, 2, 4, 6:")
print(arr[[0, 2, 4, 6]])

#Question 22
#Use Fancy Indexing to display the first and last elements.
print("\nQ22:")
print("First and last elements:")
print(arr[[0, -1]])

#Question 23
#Create a 5 × 5 matrix.
#Display:
#First row
#Last row
#First column
#Last column
print("\nQ23:")
matrix5 = np.array([
    [101, 102, 103, 104, 105],
    [201, 202, 203, 204, 205],
    [301, 302, 303, 304, 305],
    [401, 402, 403, 404, 405],
    [501, 502, 503, 504, 505]
])

print("Matrix:")
print(matrix5)

print("First row:")
print(matrix5[0])

print("Last row:")
print(matrix5[-1])

print("First column:")
print(matrix5[:, 0])

print("Last column:")
print(matrix5[:, -1])

#Question 24
#Create a 4 × 5 matrix.
#Display only the first 3 columns.
print("\nQ24:")
matrix4 = np.array([
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45]
])

print("Matrix:")
print(matrix4)

print("First 3 columns:")
print(matrix4[:, :3])

#Question 25 (Final Challenge)
#Create the following matrix:
#1   2   3   4   5
#6   7   8   9   10
#11 12  13 14  15
#16 17  18 19  20
#21 22  23 24  25
print("\nQ24:")
matrix4 = np.array([
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45]
])

print("Matrix:")
print(matrix4)

print("First 3 columns:")
print(matrix4[:, :3])


# Question 25
print("\nQ25:")

matrix = np.arange(1, 26).reshape(5, 5)

print("Matrix:")
print(matrix)

# First row
print("\nFirst row:")
print(matrix[0])

# Last row
print("\nLast row:")
print(matrix[-1])

# First column
print("\nFirst column:")
print(matrix[:, 0])

# Last column
print("\nLast column:")
print(matrix[:, -1])

# Middle row
print("\nMiddle row:")
print(matrix[2])

# Middle column
print("\nMiddle column:")
print(matrix[:, 2])

# Top-left 2 × 2
print("\nTop-left 2 × 2:")
print(matrix[:2, :2])

# Bottom-right 2 × 2
print("\nBottom-right 2 × 2:")
print(matrix[-2:, -2:])

# Even numbers
print("\nEven numbers:")
print(matrix[matrix % 2 == 0])

# Odd numbers
print("\nOdd numbers:")
print(matrix[matrix % 2 != 0])

# Numbers greater than 15
print("\nNumbers greater than 15:")
print(matrix[matrix > 15])

# Numbers less than 10
print("\nNumbers less than 10:")
print(matrix[matrix < 10])

# Fancy Indexing
print("\nFancy Indexing (1, 7, 13, 19, 25):")
print(matrix[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])

# Negative Indexing
print("\nNegative Indexing:")
print("25:", matrix[-1, -1])
print("24:", matrix[-1, -2])
print("23:", matrix[-1, -3])

# Last three rows
print("\nLast three rows:")
print(matrix[-3:])

# First three columns
print("\nFirst three columns:")
print(matrix[:, :3])

