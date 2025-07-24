import re

def validate_email(email):
    pattern = r'^\S+@\S+\.\S+$'
    return re.match(pattern, email)

email = input("Enter your email: ")
if validate_email(email):
    print("Valid email!")
else:
    print("Invalid email.")
