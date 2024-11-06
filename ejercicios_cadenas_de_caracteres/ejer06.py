"""
Ask the user to input a string and a delimiter, then split the string into a list using the specified delimiter,
and join that list into a new string using a different delimiter also provided by the user.

Author: Roberto Cano Estévez
Date: 6/11/2024
"""
print("This program splits a string using a specified delimiter and joins it using a new delimiter.")
print("--------------------------------------------------------------------------------------------")

continue_program = True
while continue_program:
    user_string = input("Enter a string: ")
    split_delimiter = input("Enter the delimiter to split the string: ")
    join_delimiter = input("Enter the delimiter to join the list: ")

    split_list = user_string.split(split_delimiter)
    joined_string = join_delimiter.join(split_list)

    print("Joined string:", joined_string)

    continue_program = input("Do you want to continue? (yes/no): ").lower() == 'yes'
