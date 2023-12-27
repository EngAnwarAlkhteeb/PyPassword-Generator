# Password Generator

If you're looking to enhance the security of your accounts, you can use this simple Python password generator. This tool creates strong passwords that can help protect your accounts from unauthorized access.

## Checking Email Security

Before diving into the code, it's always a good idea to check if your email has been compromised. You can use services like [Have I Been Pwned](https://haveibeenpwned.com/) to verify the security of your email.

## Code Explanation

The password generator script utilizes the `random` library in Python to create a unique and randomized password. Here's a brief overview of how the code works:

```python
import random

letters = [...]
numbers = [...]
symbols = [...]

# User input for password criteria
length_char = int(input("How many characters would you like your password to have? "))
n_symbols = int(input("How many symbols would you like your password to have? "))
n_numbers = int(input("How many numbers would you like your password to have? "))

# Lists to store characters, symbols, and numbers
password_list = []

# Generating random letters
for char in range(1, length_char + 1):
    password_list.append(random.choice(letters))

# Adding random symbols
for char in range(1, n_symbols + 1):
    password_list += random.choice(symbols)

# Adding random numbers
for char in range(1, n_numbers + 1):
    password_list += random.choice(numbers)

# Shuffling the password list
random.shuffle(password_list)

# Creating the final password
password = "".join(password_list)

print(f"Your password is: {password}")
