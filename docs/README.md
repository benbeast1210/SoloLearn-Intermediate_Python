# SoloLearn-Intermediate_Python

These projects were completed in contribution toward the Intermediate Python Certificate from SoloLearn.

---

## Project #1: Letter Counter

From SoloLearn:
>Given a string as input, you need to output how many times each letter appears in the string.
>You decide to store the data in a dictionary, with the letters as the keys, and the corresponding counts as the values.
>Create a program to take a string as input and output a dictionary, which represents the letter count.
>
>Sample Input
>hello
>
>Sample Output
>{'h': 1, 'e': 1, 'l': 2, 'o': 1}
>You need to output the dictionary object.
>Note, that the letters are in the order of appearance in the string.

---

## Project #2: Spelling Backwards

From SoloLearn:
>Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.
>
>Sample Input
>HELLO
>
>Sample Output
>O
>L
>L
>E
>H

## Project #3: Alien Game

From SoloLearn:
>You are creating an alien FPS game!
>The game has two types of enemies, aliens and monsters. You shoot the aliens using your laser, and monsters using your gun.
>Each hit decreases the lives of the enemies by 1.
>The given code declares a generic Enemy class, as well as the Alien and Monster classes, with their corresponding lives count.
>It also defines the hit() method for the Enemy class.
>
>You need to do the following to complete the program:
>
>1. Inherit the Alien and Monster classes from the Enemy class.
>2. Complete the while loop that continuously takes the weapon of choice from user input and call the corresponding object's hit() method.
>
>Sample Input
>laser
>laser
>gun
>exit
>
>Sample Output
>Alien has 4 lives
>Alien has 3 lives
>Monster has 2 lives
>The while loop stops when the user enters 'exit'.

## Project #4: Registration System

From SoloLearn:
>You are making a registration form for a website.
>The form has a name field, which should be more than 3 characters long.
>Any name that has less than 4 characters is invalid.
>Complete the code to take the name as input, and raise an exception if the name is invalid, outputting "Invalid Name". Output "Account Created" if the name is valid.
>
>Sample Input
>abc
>
>Sample Output
>Invalid Name
>Use try/raise/except statements.

## Project #5: Title Encoder

From SoloLearn:
>You are given a file named "books.txt" with book titles, each on a separate line.
>To encode the book titles you need to take the first letters of each word in the title and combine them.
>For example, for the book title "Game of Thrones" the encoded version should be "GoT".
>
>Complete the program to read the book title from the file and output the encoded versions, each on a new line.
>You can use the .split() method to get a list of words in a string.