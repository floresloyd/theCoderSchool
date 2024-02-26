import random

# Character sets
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = lowercase_letters.upper()
numbers = "0123456789"
symbols = "!@#$%^&*()"

# Combine all the characters
all_characters = lowercase_letters + uppercase_letters + numbers + symbols

# Get password length from user
password_length = int(input("Enter the length of the password: "))

# Generate the password
password = "" 
for i in range(password_length):
    password += random.choice(all_characters)
    

# Display the password
print(f"Your generated password is: {password}")
