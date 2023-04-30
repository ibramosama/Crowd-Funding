

from Authentication import User


def register():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    mobile_number = input("Enter your mobile number: ")
    # validate password and mobile number
    if password != confirm_password:
        print("Passwords do not match")
        return

    # Create new user object and add to list
    user = User(first_name, last_name, email, password, mobile_number)
    if user.register():
        print("Registration successful")


