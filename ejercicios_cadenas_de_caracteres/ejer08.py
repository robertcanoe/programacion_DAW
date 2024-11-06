"""
Replace words in a blacklist with asterisks in a given string. The blacklist and the string are both provided by the user.

Author: Roberto Cano Estévez
Date: 6/11/2024
"""
print("This program replaces blacklisted words in a string with asterisks.")
print("-------------------------------------------------------------------")

continue_program = True
while continue_program:
    user_string = input("Enter a string: ")
    blacklist = input("Enter blacklisted words separated by commas: ").split(',')
    for word in blacklist:
        user_string = user_string.replace(word.strip(), '*' * len(word.strip()))

    print("Filtered string:", user_string)

    continue_program = input("Do you want to continue? (yes/no): ").lower() == 'yes'
