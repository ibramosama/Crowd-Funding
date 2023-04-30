import re

class User:
    def __init__(self, first_name, last_name, email, password, mobile_number, is_active=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile_number = mobile_number
        self.is_active = is_active

    def register(self):
        # save user data to txt file
        with open("users.txt", "a") as f:
            f.write(f"{self.first_name}:{self.last_name}:{self.email}:{self.password}:{self.mobile_number}:{self.is_active}\n")
        return True


    def login(self):
        # check if email and password match
        with open("users.txt", "r") as f:
            for line in f:
                data = line.strip().split(":")
                if len(data) >= 4 and data[2] == self.email and data[3] == self.password:
                    self.is_active = True
                    return True
        return False


