"""
This program checks if a string entered by the user is a palindrome (reads the same from left to right and right to left, ignoring spaces, punctuation, and capitalization).

Author: Roberto Cano Estévez
Date: 6/11/2024
"""

print("This program checks a string and tells the user if it is a palindrome or not.")
print("-----------------------------------------------------------------------------")

try:
    text = input("Enter a string: ")

    # Convert the string to lowercase
    text = text.lower()

    # Remove non-alphanumeric characters
    processed_text = ''.join(char for char in text if char.isalnum())

    # Check if it is a palindrome
    is_palindrome = processed_text == processed_text[::-1]

    # Display the result
    if is_palindrome:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

except ValueError:
    print("Invalid input: Please enter a valid string.")

except KeyboardInterrupt:
    print("\nProcess interrupted by the user.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")