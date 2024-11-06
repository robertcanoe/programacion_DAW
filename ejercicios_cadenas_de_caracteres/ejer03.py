"""
Request a string and two indices from the user, then extract and display the substring located between those indices.
Ensure that the indices are valid. When finished, ask the user if they want to continue; if yes, repeat the process
until they choose not to.

Author: Roberto Cano Estévez
Date: 6/11/2024
"""
print("This program extracts a substring from a string based on given start and end indices.")
print("-------------------------------------------------------------------------------------")

continue_program = True
while continue_program:
    user_string = input("Enter a string: ")
    try:
        start_index = int(input("Enter the start index: "))
        end_index = int(input("Enter the end index: "))

        if 0 <= start_index < end_index <= len(user_string):
            print("Extracted substring:", user_string[start_index:end_index])
        else:
            print("Indices are out of range or invalid.")

    except ValueError:
        print("Please enter valid numeric values for indices.")

    continue_program = input("Do you want to continue? (yes/no): ").lower() == 'yes'

