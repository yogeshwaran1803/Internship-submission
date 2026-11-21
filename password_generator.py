import secrets
import string

# Get the password length from the user
length = int(input("Enter the password length: "))

# Let the user choose the password complexity
print("Choose password complexity:")
print("1. Letters only")
print("2. Letters and numbers")
print("3. Letters, numbers, and symbols")
choice = int(input("Enter your choice (1-3): "))

# Select the characters to use
if choice == 1:
    characters = string.ascii_letters
elif choice == 2:
    characters = string.ascii_letters + string.digits
elif choice == 3:
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    characters = ""
    print("Invalid choice.")

# Generate and display the password
if length <= 0:
    print("Password length must be greater than zero.")
elif characters != "":
    password = ""
    for i in range(length):
        password = password + secrets.choice(characters)

    print("Your password is:", password)
