#Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

#writing code for UserInputDataProcessorTask1

#Asking for user input for both first and last name using while loop to allow for user entry retry
while True:
    print("Please enter your first name. HINT: first name must be at least 2 characters long")
    firstname = input()
    length = len(firstname)

#Writing if else statement to catch for entries less than 2 characters
    if length > 2:
        break
    else:
        print("Sorry, you must enter your first name with more than 2 characters")

while True:
    print("Please enter your last name. HINT: last name must be at least 2 characters long")
    lastname = input()
    length2 = len(lastname)

#Writing if else statement to catch for entries less than 2 characters
    if length2 > 2:
        break
    else:
        print("Sorry, you must enter your last name with more than 2 characters")

#Printing user entries for first and second name
print(f"Thank you, your first name as entered is {firstname}, and your last name as entered is {lastname}")