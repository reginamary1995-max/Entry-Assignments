# 1. String Concatenation:
# Write a Python program that takes two strings i.e string 1 “Hello ”, string 2 get name as
# input from the user and concatenates them together. Display the concatenated string as
# the output./
string1 = "Hello "
string2 = input("Enter the name: ")
# string2 = "ggg"

print(string1 + string2)

# Now concatenate string 3 “, welcome to Python programming” to the existing string and
# display the output string.
string3 = ", welcome to Python programming"
print(string1 + string2 + string3)

# 2. String Slicing and Indexing:
# Write a Python program using the above concatenated string as input and performs the
# following tasks:
final = string1 + string2 + string3
print(final)
# a. Print the first character of the string.
print(final[0])
# b. Print the last character of the string.
print(final[-1])
# c. Print the first 5 characters of the string.
print(final[:5])
# d. Print the last 11 characters of the string.
print(final[-11:])
# e. Print the string in reverse.
print(final[::-1])
# f. Use slicing and print the word “Python” from the existing string.
print(final[25:32])

# 3. String Methods:
# Write a Python program that takes a string, strM = “Python beginner tutorial” and
# perform the following tasks:
# a. Convert the sentence to uppercase.

strM = "Python beginner tutorial"
print(strM.upper())
# b. Convert the sentence to lowercase.
print(strM.lower())

# c. Use Capitalize and return the sentence to the original input form.
print(strM.capitalize())

# d. Count the total number of occurrences of character ‘t’ in the string.
print(strM.count('t'))
# e. Replace all occurrences of “Python” with “Machine Learning” in the input string
# strM = “Python beginner 
print(strM.replace("Python", "Machine Learning"))

# Tuples (Creation, Modification and Access) :
# Create 1st tuple with values -> (10, 20, 30), 2nd tuple with values -> (40, 50, 60):
t1 = (10, 20, 30)
t2 = (40, 50, 60)
# a. Concatenate the two tuples and store it in “t_combine”
t_combine = t1 + t2 
print("Combined tuple:", t_combine)
# b. Repeat the elements of “t_combine” 3 times
print("Repeated tuple:", t_combine * 3)
# c. Access the 3rd element from “t_combine”
print("Third element is ", t_combine[2])
# d. Access the first three elements from “t_combine”
print("First three elements:", t_combine[:3])
# e. Access the last three elements from “t_combine”
print("Last three elements:", t_combine[-3:])
