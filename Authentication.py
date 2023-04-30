import re

from User import User


def register():
    first_name = input("Enter your first name: ")
    while first_name == '':
        print("first name is invalid")
        first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    while last_name == '':
        print("last name is invalid")
        last_name = input("Enter your last name: ")


    email = input("Enter your email: ")
    while (check_email_exists(email)):
        print("Email is already  exist")
        email = input("Enter your email: ")
    while not (validate_email(email)) :
        print("Email is invalid")
        email = input("Enter your email: ")

    password = input("Enter your password: ")
    while password == '':
        print("password is invalid")
        password = input("Enter your password: ")

    confirm_password = input("Confirm your password: ")
    while confirm_password == '':
        print("password is invalid")
        confirm_password = input("Enter your password: ")

    # validate password
    while password != confirm_password:
        print("Passwords do not match")
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")

    mobile_number = input("Enter your mobile number: ")
    while not re.match(r'^01[0-2,5]{1}[0-9]{8}$', mobile_number):
        print("Invalid mobile number")
        mobile_number = input("Enter your mobile number: ")

    # create new user
    new_user = User(first_name, last_name, email, password, mobile_number)
    if new_user.register():
        print("Registration successful")
    else:
        print("Registration failed")

def check_email_exists(email):
    # check if email exists in database
    with open("users.txt", "r") as f:
        for line in f:
            data = line.strip().split(":")
            if len(data) >= 3 and data[2] ==email:
                return True
            return False
def validate_email(email):
    """Return True if the email address is valid, False otherwise."""

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False





