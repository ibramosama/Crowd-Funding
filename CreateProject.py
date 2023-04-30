import re
from datetime import datetime
from Python_Project.Project import Project

def create_project(user_email):

    title = input("Enter project title: ")
    while title == '' or contains_special_characters(title):
        print("title is invalid")
        title = input("Enter project title: ")

    details = input("Enter project details: ")
    while details == '' or contains_special_characters(details):
        print("details is invalid")
        details = input("Enter project details: ")

    while True:
        try:
            target_amount = float(input("Enter project target amount: "))
            break
        except ValueError:
            print("Invalid target amount. Please enter valid number")

    while True:
        try:
            start_date_str = input("Enter project start date (YYYY-MM-DD): ")
            end_date_str = input("Enter project end date (YYYY-MM-DD): ")
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please use the format YYYY-MM-DD")

    # Create new project object and add to list
    project = Project(title, details, target_amount, start_date, end_date, user_email)
    with open("projects.txt", "a") as file:
        file.write(
            f"{project.title}:{project.details}:{project.target_amount}:{project.start_date}:{project.end_date}:{user_email}\n")

    print("Project created successfully.")


def contains_special_characters(input_string):
    # Define a regular expression pattern that matches any non-alphanumeric characters
    pattern = r'(?!\s)[^a-zA-Z0-9\s](?<!\s)'

    # Use the re.search function to search for the pattern in the input string
    match = re.search(pattern, input_string)

    # If a match is found, return True, otherwise return False
    if match:
        return True
    else:
        return False
