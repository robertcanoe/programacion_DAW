"""
Replace 'a' with '4', 'e' with '3', 'i' with '1', and 'o' with '0' in a given string using the translate() method.

Author: Roberto Cano Estévez
Date: 6/11/2024
"""
print("This program replaces 'a' with '4', 'e' with '3', 'i' with '1', and 'o' with '0' in the given string.")
print("-----------------------------------------------------------------------------------------------------")

continue_program = True
while continue_program:
    user_string = input("Enter a string: ")
    translation_table = str.maketrans("a e i o", "4 3 1 0")
    translated_string = user_string.translate(translation_table)

    print("Translated string:", translated_string)

    continue_program = input("Do you want to continue? (yes/no): ").lower() == 'yes'
