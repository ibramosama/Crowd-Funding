import datetime
import re

# Define a Project class to store project data
class Project:
    def __init__(self, title, details, target_amount, start_date, end_date, user_email):
        self.title = title
        self.details = details
        self.target_amount = target_amount
        self.start_date = start_date
        self.end_date = end_date
        self.user_email = user_email

    def get_duration(self):
        duration = self.end_date - self.start_date
        return duration.days

    @classmethod
    def delete_project(cls, title, user_email):
        with open('projects.txt', 'r') as f:
            lines = f.readlines()
        with open('projects.txt', 'w') as f:
            deleted = False
            for line in lines:
                data = line.strip().split(':')
                if data[0] == title:
                    if len(data) >= 4 and data[5] != user_email:
                        print("You don't have permission to delete this project")
                        f.writelines(lines)
                        return
                    deleted = True
                    continue
                f.write(line)
            if deleted:
                print(f"The project {title} has been deleted.")
            else:
                print(f"No project found with title {title}.")

    @classmethod
    def edit_project(cls, title, user_email):
        with open('projects.txt', 'r') as f:
            lines = f.readlines()
        with open('projects.txt', 'w') as f:
            edited = False
            for line in lines:
                data = line.strip().split(':')
                if data[0] == title:
                    if len(data) >= 4 and data[5] != user_email:
                        print("You don't have permission to edit this project")
                        f.writelines(lines)
                        return
                    edited = True
                    pattern = r'(?!\s)[^a-zA-Z0-9\s](?<!\s)'
                    # get new details from user
                    new_title = input("Enter new title (leave blank to keep current title): ")
                    if not new_title:
                        new_title = data[0]
                    else:
                        # Use the re.search function to search for the pattern in the input string
                        match = re.search(pattern, new_title)
                        while match:
                            print("Title is invalid")
                            new_title = input("Enter new title (leave blank to keep current title): ")

                    new_details = input("Enter new details (leave blank to keep current details): ")
                    if not new_details:
                        new_details = data[1]
                    else:
                        match = re.search(pattern, new_details)
                        while match:
                            print("Details is invalid")
                            new_details = input("Enter new details (leave blank to keep current details): ")

                    while True:
                        try:
                            new_target = input("Enter new target amount (leave blank to keep current target): ")
                            if not new_target:
                                new_target = data[2]
                            new_target = int(new_target)
                            break
                        except ValueError:
                            print("Invalid target amount. Please enter valid number")

                    while True:
                        try:
                            new_start = input(
                                "Enter new start date (YYYY-MM-DD) (leave blank to keep current start date): ")
                            if not new_start:
                                new_start = data[3]
                            else:
                                datetime.datetime.strptime(new_start, '%Y-%m-%d')
                            break
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                            f.writelines(lines)

                    while True:
                        try:
                            new_end = input(
                                "Enter new end date (YYYY-MM-DD) (leave blank to keep current end date): ")
                            if not new_end:
                                new_end = data[4]
                            else:
                                datetime.datetime.strptime(new_end, '%Y-%m-%d')
                            break
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                            f.writelines(lines)

                    # write the updated project to file
                    f.write(f"{new_title}:{new_details}:{new_target}:{new_start}:{new_end}:{user_email}\n")
                    continue
                f.write(line)
            if edited:
                print(f"The project {title} has been updated.")
            else:
                print(f"No project found with title {title}.")