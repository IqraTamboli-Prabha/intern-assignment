#Part:A

#Question 1
#Create a 1D NumPy array containing numbers from 1 to 12. Reshape it into a 3 × 4 matrix.
import numpy as np

print("\nQ1:")
arr1 = np.arange(1, 13)
matrix1 = arr1.reshape(3, 4)
print("1D Array:")
print(arr1)
print("3 × 4 Matrix:")
print(matrix1)

#Question 2
#Create a 1D array containing numbers from 1 to 16. Reshape it into a 4 × 4 matrix.
print("\nQ2:")
arr2 = np.arange(1, 17)
matrix2 = arr2.reshape(4, 4)
print("1D Array:")
print(arr2)
print("4 × 4 Matrix:")
print(matrix2)
#Question 3
#Create a 1D array containing numbers from 1 to 24. Convert it into a 2 × 3 × 4 3D array.
print("\nQ3:")
arr3 = np.arange(1, 25)
array3d = arr3.reshape(2, 3, 4)
print("3D Array:")
print(array3d)

#Question 4
#Create a 1D array containing 18 elements. Reshape it into a 3 × 6 matrix.
print("\nQ4:")
arr4 = np.arange(101, 119)
matrix4 = arr4.reshape(3, 6)
print("1D Array:")
print(arr4)
print("3 × 6 Matrix:")
print(matrix4)

#Question 5
#Create a 1D array containing 20 elements. Use -1 in reshape() to automatically calculate the number of rows or columns.
print("\nQ5:")
arr5 = np.arange(1, 21)
matrix5 = arr5.reshape(-1, 5)
print("1D Array:")
print(arr5)
print("Reshaped Matrix using -1:")
print(matrix5)

#Question 6
#Create a 3 × 4 matrix and reshape it into a 2 × 6 matrix.
print("\nQ6:")
matrix6 = np.arange(1, 13).reshape(3, 4)
new_matrix6 = matrix6.reshape(2, 6)
print("Original 3 × 4 Matrix:")
print(matrix6)

print("New 2 × 6 Matrix:")
print(new_matrix6)

#Question 7
#Create a 2 × 3 × 2 3D array and convert it back into a 1D array.
print("\nQ7:")
array7 = np.arange(1, 13).reshape(2, 3, 2)
one_d7 = array7.reshape(-1)

print("Original 3D Array:")
print(array7)

print("1D Array:")
print(one_d7)

#Part:B
#Question 8
#Create a 3 × 3 matrix and convert it into a 1D array using flatten().
import numpy as np

# Question 8
print("\nQ8:")
matrix8 = np.array([
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]
])

flat8 = matrix8.flatten()

print("Original Matrix:")
print(matrix8)

print("Flattened Array:")
print(flat8)

#Question 9
#Create a 4 × 2 matrix and convert it into a 1D array using ravel().
print("\nQ9:")
matrix9 = np.array([
    [21, 22],
    [23, 24],
    [25, 26],
    [27, 28]
])

ravel9 = matrix9.ravel()

print("Original Matrix:")
print(matrix9)

print("Raveled Array:")
print(ravel9)

#Question 10
#Create a 2 × 4 matrix and display its transpose using both:
#transpose()
#.T
print("\nQ10:")
matrix10 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print("Original Matrix:")
print(matrix10)

print("Using transpose():")
print(matrix10.transpose())

print("Using .T:")
print(matrix10.T)

#Question 11
#Create a 3 × 3 matrix and resize it into a 2 × 6 matrix using np.resize().
print("\nQ11:")
matrix11 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

resized11 = np.resize(matrix11, (2, 6))

print("Original Matrix:")
print(matrix11)

print("Resized 2 × 6 Matrix:")
print(resized11)

#Question 12
#Create a 1D array:
#[10,20,30]
#Resize it into a 3 × 3 matrix.
print("\nQ12:")
arr12 = np.array([10, 20, 30])

resized12 = np.resize(arr12, (3, 3))

print("Original Array:")
print(arr12)

print("Resized 3 × 3 Matrix:")
print(resized12)

#Question 13
#Create a 2 × 3 matrix. Use flatten(), modify the first element of the flattened array, and display both the original and flattened arrays.
print("\nQ13:")
matrix13 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

flat13 = matrix13.flatten()

flat13[0] = 999

print("Original Matrix:")
print(matrix13)

print("Modified Flattened Array:")
print(flat13)

#Question 14
#Create a 2 × 3 matrix. Use ravel(), modify the first element of the raveled array, and display both the original and raveled arrays.
print("\nQ14:")
matrix14 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

ravel14 = matrix14.ravel()

ravel14[0] = 999

print("Original Matrix:")
print(matrix14)

print("Modified Raveled Array:")
print(ravel14)

#Part:C
#Question 15
#Create two arrays:
#Array 1 = [10,20,30]
import numpy as np

#Array 2 = [40,50,60]
#Merge them using np.concatenate().

print("\nQ15:")
array1 = np.array([10, 20, 30])
array2 = np.array([40, 50, 60])

merged15 = np.concatenate((array1, array2))

print("Array 1:")
print(array1)

print("Array 2:")
print(array2)

print("Merged Array:")
print(merged15)

#Question 16
#Create two 2 × 2 matrices and merge them column-wise using np.hstack().
print("\nQ16:")
matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

merged16 = np.hstack((matrix1, matrix2))

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

print("Column-wise Merge:")
print(merged16)

#Question 17
#Create two 2 × 2 matrices and merge them row-wise using np.vstack().
print("\nQ17:")
matrix3 = np.array([
    [11, 12],
    [13, 14]
])

matrix4 = np.array([
    [21, 22],
    [23, 24]
])

merged17 = np.vstack((matrix3, matrix4))

print("Matrix 1:")
print(matrix3)

print("Matrix 2:")
print(matrix4)

print("Row-wise Merge:")
print(merged17)

#Question 18
#Create a 1D array containing numbers from 1 to 12. Split it into 4 equal parts.
print("\nQ18:")
arr18 = np.arange(1, 13)

parts18 = np.split(arr18, 4)

print("Original Array:")
print(arr18)

print("4 Equal Parts:")
for part in parts18:
    print(part)

#Question 19
#Create a 4 × 2 matrix and split it into 2 equal parts using np.split().
print("\nQ19:")
matrix19 = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80]
])

parts19 = np.split(matrix19, 2)

print("Original Matrix:")
print(matrix19)

print("2 Equal Parts:")
for part in parts19:
    print(part)
#Question 20
#Create three arrays:
#[1,2]

#[3,4]

#[5,6]
#Merge all three arrays using np.concatenate().
print("\nQ20:")
array_a = np.array([1, 2])
array_b = np.array([3, 4])
array_c = np.array([5, 6])

merged20 = np.concatenate((array_a, array_b, array_c))

print("Merged Array:")
print(merged20)

#Part:D
#Question 21
#Create the following salary array:
#[25000,30000,35000,40000,45000]
#Using broadcasting, add a ₹5000 bonus to every employee.
import numpy as np

print("\nQ21:")
salary = np.array([25000, 30000, 35000, 40000, 45000])

bonus = 5000
new_salary = salary + bonus

print("Original Salary:")
print(salary)

print("Salary after ₹5000 bonus:")
print(new_salary)

#Question 22
#Create the following student marks matrix:
#[[70,80,90],
#  #[60,75,85]]
#Add the following grace marks using broadcasting:
#[5,5,10]
#Display the updated marks.
print("\nQ22:")
marks = np.array([
    [70, 80, 90],
    [60, 75, 85]
])

grace = np.array([5, 5, 10])

updated_marks = marks + grace

print("Original Marks:")
print(marks)

print("Grace Marks:")
print(grace)

print("Updated Marks:")
print(updated_marks)

#Question 23
#Create a NumPy array:
#[10,20,30,40]
#Create a copy using copy(). Modify the copied array and display both the original and copied arrays.
print("\nQ23:")
arr23 = np.array([10, 20, 30, 40])

copy_arr = arr23.copy()
copy_arr[0] = 999

print("Original Array:")
print(arr23)

print("Copied Array:")
print(copy_arr)

#Question 24
#Create a NumPy array:
#[100,200,300,400]
#Create a view using view(). Modify the view and display both the original and view arrays.
print("\nQ24:")
arr24 = np.array([100, 200, 300, 400])

view_arr = arr24.view()
view_arr[0] = 999

print("Original Array:")
print(arr24)

print("View Array:")
print(view_arr)

#Question 25 (Mini Project)
#Create the following employee salary matrix:
#[[25000,30000,35000],
# [40000,45000,50000]]
#Perform all of the following operations:
#Display the original matrix.
#Reshape it into a 3 × 2 matrix.
#Flatten the reshaped matrix.
#Display the transpose of the original matrix.
#Increase every salary by ₹2000 using broadcasting.
#Create a copy of the salary matrix and modify one value.
#Create a view of the salary matrix and modify one value.
#Display all results and compare the outputs.
print("\nQ25:")

# 1. Original salary matrix
salary_matrix = np.array([
    [25000, 30000, 35000],
    [40000, 45000, 50000]
])

print("1. Original Salary Matrix:")
print(salary_matrix)


# 2. Reshape into 3 × 2
reshaped = salary_matrix.reshape(3, 2)

print("\n2. Reshaped 3 × 2 Matrix:")
print(reshaped)

# 3. Flatten the reshaped matrix
flattened = reshaped.flatten()

print("\n3. Flattened Matrix:")
print(flattened)


# 4. Transpose of original matrix
transposed = salary_matrix.transpose()

print("\n4. Transpose of Original Matrix:")
print(transposed)


# 5. Increase every salary by ₹2000
increased_salary = salary_matrix + 2000

print("\n5. Salary after ₹2000 Increase:")
print(increased_salary)

# 6. Create a copy and modify one value
salary_copy = salary_matrix.copy()
salary_copy[0, 0] = 99999

print("\n6. Original Matrix after Copy Modification:")
print(salary_matrix)

print("Copied Matrix:")
print(salary_copy)

# 7. Create a view and modify one value
salary_view = salary_matrix.view()
salary_view[0, 1] = 88888

print("\n7. Original Matrix after View Modification:")
print(salary_matrix)

print("View Matrix:")
print(salary_view)


# 8. Compare copy and view
print("\n8. Comparison:")

print("Original Matrix:")
print(salary_matrix)

print("Copy:")
print(salary_copy)

print("View:")
print(salary_view)