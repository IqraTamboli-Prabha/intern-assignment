# Q1
#Question 1
#Import the NumPy library.
print("Q1:")
print("NumPy imported successfully")

#Question 2
#Create a 1D NumPy array containing numbers from 1 to 10.
import numpy as np

print("\nQ2:")
arr1 = np.arange(1, 11)
print(arr1)

#Question 3
#Create a 2D array of size 3 × 3.
print("\nQ3:")
arr2 = np.arange(1, 10).reshape(3, 3)
print(arr2)

#Question 4
#Create a 3D array of size 2 × 2 × 3.
print("\nQ3:")
arr2 = np.arange(1, 10).reshape(3, 3)
print(arr2)

#Question 5
#Display the number of dimensions (ndim) of a 2D array.
print("\nQ5:")
print(arr2.ndim)

#Question 6
#Display the shape of a 3D array.
print("\nQ6:")
arr3 = np.arange(1, 13).reshape(2, 2, 3)
print(arr3.shape)

#Question 7
#Display the total number of elements using size.
print("\nQ7:")
print(arr3.size)

#Question 8
#Display the data type (dtype) of an array.
print("\nQ8:")
print(arr1.dtype)

#Question 9
#Create a 5 × 5 array filled with zeros.
print("\nQ9:")
zeros = np.zeros((5, 5))
print(zeros)

#Question 10
#Create a 4 × 4 array filled with ones.
print("\nQ10:")
ones = np.ones((4, 4))
print(ones)

#Question 11
#Create a 3 × 3 array filled with the value 100.
print("\nQ11:")
arr11 = np.full((3, 3), 100)
print(arr11)

#Question 12
#Create a 5 × 5 Identity Matrix.
print("\nQ12:")
arr12 = np.eye(5)
print(arr12)
      
#Question 13
#Create an array using arange() from 10 to 50.
print("\nQ13:")
arr13 = np.arange(10, 51)
print(arr13)

#Question 14
#Create an array using arange() with a step size of 5.
print("\nQ14:")
arr14 = np.arange(0, 51, 5)
print(arr14)

#Question 15
#Create an array using linspace() from 1 to 100 with 10 values.
print("\nQ15:")
arr15 = np.linspace(1, 100, 10)
print(arr15)

#Question 16
#Create an array containing decimal values using linspace().
print("\nQ16:")
arr16 = np.linspace(0.5, 5.0, 10)
print(arr16)

#Question 17
#Create a Student Marks array containing marks of 10 students.
print("\nQ17:")
student_marks = np.array([78, 85, 92, 67, 74, 88, 95, 81, 69, 90])
print(student_marks)

#Question 18
#Display the shape, size, ndim, and dtype of the Student Marks array.
print("\nQ18:")
print("Shape:", student_marks.shape)
print("Size:", student_marks.size)
print("Dimensions:", student_marks.ndim)
print("Data Type:", student_marks.dtype)

#Question 19
#Create a 2 × 5 array using array().
print("\nQ19:")
arr19 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(arr19)

#Question 20
#Create a 3 × 4 array using nested lists.
print("\nQ20:")
arr20 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(arr20)

#Question 21
#Create an array of floating-point numbers.
print("\nQ21:")
arr21 = np.array([10.5, 20.2, 30.7, 40.1, 50.9])
print(arr21)

#Question 22
#Create an array of string values.
print("\nQ22:")
arr22 = np.array(["Apple", "Banana", "Mango", "Orange"])
print(arr22)

#Question 23
#Create an array of Boolean values.
print("\nQ23:")
arr23 = np.array([True, False, True, False, True])
print(arr23)

#Question 24
#Create a 6 × 6 matrix of zeros.
print("\nQ24:")
arr24 = np.zeros((6, 6))
print(arr24)
#Question 25
#Create a 10 × 10 Identity Matrix.
print("\nQ25:")
arr25 = np.eye(10)
print(arr25)

