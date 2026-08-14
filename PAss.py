# Q
import pandas as pd

# Create data for 5 students
student_data = {
    "Name": ["Sham", "Aisha", "Rahul", "Priya", "Arjun"],
    "Age": [22, 21, 23, 20, 22],
    "City": ["Pune", "Mumbai", "Delhi", "Nashik", "Nagpur"],
    "Marks": [85, 90, 78, 88, 92]
}

# 1. Create the DataFrame
students_df = pd.DataFrame(student_data)

# 2. Display the DataFrame
print("Student DataFrame:")
print(students_df)

# 3. Save the DataFrame to a CSV file
students_df.to_csv("students.csv", index=False)

# 4. Read the CSV file again
loaded_students = pd.read_csv("students.csv")

# 5. Display the loaded data
print("\nLoaded Data:")
print(loaded_students)

# Q1
#Pandas is a open-source python library used for data analysis and manipulation.
# Q2
# Pandas is used in AI/ML for data cleaning,preprocessing, and analysis.     
# Q3
# A series is a one-dimensional labeled array in pandas.
# Q4
# A Dataframe is a two-dimensional table with rows and columns in pandas.
# Q5
# cvs(Comma Separated values) file is a text file that stores tabular data separated by commas.

import pandas as pd

# Create student data
student_data = {
    "Name": ["Sham", "Aisha"],
    "Age": [22, 21],
    "Marks": [85, 90]
}

# Create a DataFrame
students_df = pd.DataFrame(student_data)

# Save the DataFrame as a CSV file
students_df.to_csv("students.csv", index=False)

# Read the CSV file
loaded_data = pd.read_csv("students.csv")

# Display the CSV data
print("CSV File Data:")
print(loaded_data)

# Q6
import pandas as pd

# Create a dictionary containing student information
student_data = {
    "Name": ["Sham", "Aisha", "Rahul"],
    "Age": [22, 21, 23],
    "Marks": [85, 90, 78]
}

# Create a DataFrame from the dictionary
students_df = pd.DataFrame(student_data)

# Display the DataFrame
print(students_df)