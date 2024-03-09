#Python List Transformation
#Task One: Sort grades in desending order and display the sorted list
print()
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
print(f"Original Grades List: {grades}")
grades.sort()
grades.reverse()
print(f"Grades List in Descending Order: {grades}")

print()

#Task Two: Calculate the average grade and display it
total = sum(grades)
length = len(grades)
avg = total/length
print(f"Average Grade: {avg}")

print()

#Task Three: Replace any grade below 80 with the value Failed
sliced = grades[:7]
low_scores = ["Failed", "Failed", "Failed"]
updated_grades = sliced + low_scores

print()

#Advanced List Methods and Identity Operators
#Task One: Find which students are in both lists
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

new_list = []

if submitted[0] in attended:
    new_list.append(submitted[0])
if submitted[1] in attended:
    new_list.append(submitted[1])
if submitted[2] in attended:
    new_list.append(submitted[2])
if submitted[3] in attended:
    new_list.append(submitted[3])

submitted = new_list

print(f"Students in both lists: {submitted}")

print()

#Task Two: Check if the lists are identical
print(f"The lists are identical: {submitted is attended}") 

print()

#Task Three: Remove any student from attended list if not in submitted list
attended.remove("Eve")
attended.remove("Frank")
attended.sort()
print(f"Updated attended list: {attended}")

print()

#Advanced Slicing Techniques
#Task One: Extract temperatures for the second week (7 days) of the month
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91,
 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_Week_temps = temperatures[14:21]
print(f"Temperatures of second week: {second_Week_temps}")

print()

#Task Two: Extract all temperatures above 100
temperatures.sort()
temps_above_100 = temperatures[23:]
print(f"Temperatures above 100: {temps_above_100}")

temperatures.reverse()
print(f"Reversed List: {temperatures}")
extracted_days = temperatures[5:11]
print("5th to 10th day of reversed list: ", extracted_days)

#List Comprehensions and Membership Operators
#Task One: Use list comprehension to create a new list containing even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [num for num in numbers if num % 2 == 0]
print(f"List of even numbers: {new_list}")

print()

#Task Two: Use list comprehension to create new list with numbers greater than five
new_list = [num for num in numbers if num > 5]
print(f"List of numbers greater than 5: {new_list}")

print()

#Task Three: Check if 7 is in original numbers list
print(f"Seven is in original numbers list: {7 in numbers}")

print()

#Deep Dive into Python Lists
#Task One: Filter out students w grades below 80. Print name, grade, activity
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

ineligible_students = students[2:]
ineligible_students_grades = grades[2:]
ineligible_students_activities = activities[2:]

print(f"Ineligible students: {ineligible_students}")
print(f"Ineligible students' grades: {ineligible_students_grades}")
print(f"Ineligible students' activities: {ineligible_students_activities}")

print()

#Task Three and Four: Add approved students to a new list and print it 
students_approved = students[0:2]
print(f"Approved Students: {students_approved}")
