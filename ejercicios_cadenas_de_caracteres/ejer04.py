"""
Replace all occurrences of a given substring with another substring specified by the user. When finished, ask the
user if they want to continue; if yes, repeat the process until they choose not to.

Author: Roberto Cano Estévez
Date: 6/11/2024
"""
print("This program replaces all occurrences of a specified substring with another substring in a given string.")
print("--------------------------------------------------------------------------------------------------------")

continue_program = True
while continue_program:
    user_string = input("Enter the original string: ")
    target_substring = input("Enter the substring to replace: ")
    replacement_substring = input("Enter the replacement substring: ")

    modified_string = user_string.replace(target_substring, replacement_substring)
    print("Modified string:", modified_string)

    continue_program = input("Do you want to continue? (yes/no): ").lower() == 'yes'
