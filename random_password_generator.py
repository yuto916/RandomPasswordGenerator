# Date:     January 3, 2023
# File:     random_password_generator.py
# Descriptions: This program will create a random password based on the user input. 
#               User will input the length of the password along with the number of letters, digits, and special characters to be used.





import random


# Defining variables
valid_input = False

password = ""
password_length = ""
num_of_characters_left = ""

num_of_letters = ""
num_of_digits = ""
num_of_special_characters = ""


# Defining list(s)
list_of_special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '=', '?']


# Defining constants
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 30



# Getting length of password
while not valid_input:
    try:
        # Prompt the user for the length of password
        password_length = int(input("Please enter the length of the password: "))

        if password_length < PASSWORD_MIN_LENGTH:
            print("Please enter a value equal to or greater than " + str(PASSWORD_MIN_LENGTH) + " to create a secure password.")

        elif password_length > PASSWORD_MAX_LENGTH:
            print("The password length cannot be greater than " + str(PASSWORD_MAX_LENGTH) + ".")

        else:
            valid_input = True
            num_of_characters_left = password_length

    except:
        print("You must enter a positive integer.")

valid_input = False



# Getting number of letters to be used
while valid_input == False:
    try:
        # Prompt the user for the number of letters to be used
        num_of_letters = int(input("Please enter the number of letters to be used in the password: "))

        # If out of range, display error message
        if num_of_letters > num_of_characters_left or num_of_letters < 0:
            print("The number of letters must be in the range of 0 and " + str(num_of_characters_left) + ".")

        else:
            # If valid input, set valid input to true
            valid_input = True

            # Decide number of capital and small letters
            # 1. it will generate random integer within the range of 0 and the number of letters
            # 2. based on the random number generated, it will determine number of capital letters
            # 3. number of capital letters is subtracted from number of letters to determine number of small letters
            num_of_cap_letters = num_of_letters - random.randint(0, num_of_letters)
            num_of_small_letters = num_of_letters - num_of_cap_letters

            # Generate random capital letters according to the number of capital letters to be used
            # and store it in the variable password
            for i in range(num_of_cap_letters):
                i = chr(random.randint(65, 90))
                password += i

            # Generate random small letters according to the number of small letters to be used
            # and store it in the variable password
            for i in range(num_of_small_letters):
                i = chr(random.randint(97, 122))
                password += i

            # Determine the number of characters left to be used
            num_of_characters_left = password_length - (num_of_cap_letters + num_of_small_letters)
    except:
        print("You must enter a positive integer for number of letters.")

valid_input = False



# Getting number of digits to be used
while valid_input == False:
    try:
        # Prompt the user for the number of digits to be used
        num_of_digits = int(input("Please enter the number of digits to be used in the password: "))

        # If out of range, display error message
        if num_of_digits > num_of_characters_left or num_of_digits < 0:
            print("The number of digits must be in the range of 0 and " + str(num_of_characters_left) + ".")

        else:
            # If valid input, set valid input to true
            valid_input = True

            # Generate random digits according to the number of digits to be used and store it in the variable password
            for i in range(num_of_digits):
                i = random.randint(0, 9)
                password += str(i)

            # Determine the number of characters left to be used
            num_of_characters_left = num_of_characters_left - num_of_digits
    except:
        print("You must enter a positive integer for number of digits.")




# Displaying the number of special characters used
print("The number of special characters used will be " + str(num_of_characters_left) + ".")

       
# Generate random special characters from the list according to the number of special characters to be used
# and store it in the variable password
for i in range(num_of_characters_left):
    i = random.choice(list_of_special_characters)
    password += i




# Make the variable password a list, and store it in the list called password_list
password_list = list(password)

# Shuffle the elements in password_list
random.shuffle(password_list)

# Join the shuffle password_list to result
result = "".join(password_list)

# Print the result
print("\nGenerated password is: " + result)