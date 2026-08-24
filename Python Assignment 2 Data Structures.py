# 1. List Creation:
# a. Create a list named age_list with five integer elements. For eg., [24, 25, 26, 27, 28]
# a. Create a list of five integers
age_list = [24, 25, 26, 27, 28]
print(age_list)
# b. Create a list named name_list with five string elements.
name_list = ["Regina", "Anu", "Meera", "John", "David"]
print(name_list)

# Append the string "Yazhini" to name_list.
name_list.append("Yazhini")
print(name_list)
# b. Insert the element 30 at index 2 in age_list.
age_list.insert(2, 30)
print(age_list)
# Remove the string "Yazhini" from name_list.
name_list.remove("Yazhini")
print(name_list)
# d. Pop the last element from age_list.
age_list.pop()
print(age_list)
# e. Extend the age_list with additional ages [29, 30, 26]
age_list.extend([29, 30, 26])
print(age_list)

# f. Sort age_list in descending order
age_list = sorted(age_list)[::-1]
print(age_list)

# Find Max age, Min age and sum of all ages from age_list.

print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of all ages:", sum(age_list))
# Print the first element of name_list.
print(name_list[0])
# b. Print the last element of name_list.
print(name_list[-1])
# c. Print the elements from index 2 to index 4 in name_list.
print(name_list[2:5])
# d. Print the elements of name_list in reverse order.
print(name_list[::-1])
# a. Create a dictionary named student_marks that maps the names of five
# students to their marks (use scale of from 0 to 100).
student_marks = {
    "Anu": 85,
    "Rahul": 92,
    "Meera": 78,
    "Arun": 88,
    "Priya": 95
}
print(student_marks)
# b. Access and print the mark of a specific student, of your choice.
print(student_marks["Anu"])
# c. Add a new student "Janani" with a mark of 80 to the student_marks dictionary.
student_marks["Janani"] = 80
print(student_marks)
# d. Update the mark of any one older student to 82.
student_marks["Anu"] = 82
print(student_marks)
# e. Use the keys(), values(), and items() methods to print all keys, values, and key-value pairs in the student_marks dictionary.
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())
# a. Create a set called my_set with following values:
# ['a','e','i','o','u','a','a','i']
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
# b. Attempt to change the value of my_set[4] = 's'. If code throws an error, provide
# an explanation.
print(my_set)
# my_set[4] = 's'
# /------- Explanation: A Python set is unordered and does not support indexing
# c. Create two sets:

# set1 with values: {1, 3, 5, 7, 9}
# set2 with values: {2, 3, 5, 8, 10}
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}
# d. Compute and print the union and intersection of set1 and set2.
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

# 1. Prompt user for Input. Score range should be from 0 to 10 (both inclusive).
# 2. Find the performance category based on the input score using following criteria:
# a. Above Average: Score greater than 7
# b. Average: Score between 4 and 7(both inclusive)
# c. Below Average: Score lesser than 4
# 3. Output: Print the Performance category
# 4. Additional Step: You can give a prompt of your choice to each category.
# For eg: If score below average “Need to Improve your performance, consistent
# practice will lead to better results”.

score = float(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

elif score > 7:
    print("Performance Category: Above Average")
    print("Excellent performance! Keep up the good work.")

elif score >= 4:
    print("Performance Category: Average")
    print("Good effort! Keep practicing to improve your performance.")

else:
    print("Performance Category: Below Average")
    print("Need to improve your performance. Consistent practice will lead to better results.")