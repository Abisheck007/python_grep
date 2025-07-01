import re


def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@gmail.com$'
        if re.match(pattern, email):
            return True
        else:
            return False
        
email = input("Enter your email: ")

if validate_email(email):
    print("Valid email address.")
else:
    print("Invalid email address. Please enter a valid Gmail address.")