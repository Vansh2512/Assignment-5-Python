# Assignment-5-Python

 
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
   
#Logic to solve 

This is a dictionary that stores student names and their marks.
Each name is the key, and the mark is the value.
Example: "Vansh" has 80 marks.

Asks the user to enter a name.
.capitalize() makes sure the first letter is uppercase and the rest are lowercase.
Example: if user types vAnSh, it becomes Vansh.

if b in a: checks if the entered name (after formatting) exists in the dictionary.
If it exists: it prints the marks.
If not: it shows "Student not found".

####################################################################################
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

#Logic to solve

Fisrt of all we created list.

b = a[0:5]
This uses list slicing to get elements from index 0 to 4 (5 is not included).
So, b = [1, 2, 3, 4, 5]

c = list(reversed(b))
This reverses the list b.
So c = [5, 4, 3, 2, 1]
