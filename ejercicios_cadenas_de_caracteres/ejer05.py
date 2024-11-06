"""
Encrypt a string using the Caesar cipher by shifting each letter a specified number of places in the alphabet,
according to a shift provided by the user.

Author: Roberto Cano Estévez
Date: 6/11/2024
"""
print("This program encrypts a string using the Caesar cipher with a user-specified shift.")
print("-----------------------------------------------------------------------------------")

continue_program = True
while continue_program:
    user_string = input("Enter a string to encrypt: ")
    try:
        shift = int(input("Enter the shift (number of positions): "))

        encrypted_string = ""
        for char in user_string:
            if char.isalpha():
                shift_base = ord('a') if char.islower() else ord('A')
                encrypted_string += chr(shift_base + (ord(char) - shift_base + shift) % 26)
            else:
                encrypted_string += char

        print("Encrypted string:", encrypted_string)

    except ValueError:
        print("Please enter a valid numeric shift value.")

    continue_program = input("Do you want to continue? (yes/no): ").lower() == 'yes'
