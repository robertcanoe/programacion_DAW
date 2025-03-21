"""
This program checks if a string entered by the user is a palindrome (reads the same from left to right and right to left, ignoring spaces, punctuation, and capitalization).

Author: Roberto Cano Estévez
Date: 6/11/2024
"""

print("This program checks a string and tells the user if it is a palindrome or not.")
print("-----------------------------------------------------------------------------")

try:
    text = input("Enter a string: ").lower()

    processed_text = ''.join(char for char in text if char.isalnum())

    is_palindrome = processed_text == processed_text[::-1]

    if is_palindrome:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

except ValueError:
    print("Invalid input: Please enter a valid string.")

except KeyboardInterrupt:
    print("\nProcess interrupted by the user.")
