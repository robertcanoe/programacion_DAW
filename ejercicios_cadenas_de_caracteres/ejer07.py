"""
Find all positions of a substring within a longer string, both entered by the user.

Author: Roberto Cano Estévez
Date: 6/11/2024
"""
print("This program finds all occurrences of a specified substring within a given string.")
print("----------------------------------------------------------------------------------")

continue_program = True
while continue_program:
    user_string = input("Enter a string: ")
    substring = input("Enter the substring to find: ")

    positions = [i for i in range(len(user_string)) if user_string.startswith(substring, i)]
    print("Positions of the substring:", positions)

    continue_program = input("Do you want to continue? (yes/no): ").lower() == 'yes'
