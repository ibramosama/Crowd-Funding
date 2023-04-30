from datetime import datetime

from Python_Project.Project import Project

def view_projects():
    # Read project data from database file
    projects = []
    with open("projects.txt", "r") as file:
        for line in file:
            project_data = line.split(":")
            data = line.strip().split(':')
            if len(data) < 6:
                continue
            title = project_data[0]
            details = project_data[1]
            target_amount = float(project_data[2])
            start_date_str = project_data[3].strip()
            end_date_str = project_data[4].strip()

            # Validate date format
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            except ValueError:
                print(f"Invalid date format for project: {title}")
                continue

            # Validate date range
            if end_date <= start_date:
                print(f"End date should be after start date for project: {title}")
                continue

            project = Project(title, details, target_amount, start_date, end_date,"")
            projects.append(project)

    # Display project details
    if not projects:
        print("No projects found.")
    else:

        for project in projects:
            print("________________________________________________________")
            print("Available Projects:")
            print(f"Title: {project.title}")
            print(f"Details: {project.details}")
            print(f"Target Amount: {project.target_amount} EGP")
            print(f"Duration: {project.get_duration()} days")


def view_my_projects(user):
    with open("projects.txt", "r") as f:
        for line in f:
            data = line.strip().split(":")
            if len(data) >= 7 and data[6] == user.email:
                title = data[0]
                details = data[1]
                target_amount = float(data[2])
                start_date = data[3].strip()
                end_date = data[4].strip()
                backers = data[5].split(",")
                project = Project(title, details, target_amount, start_date, end_date, user)
                project.backers = backers
                print(f"Title: {project.title}")
                print(f"Details: {project.details}")
                print(f"Target amount: {project.target_amount}")
                print(f"Start date: {project.start_date}")
                print(f"End date: {project.end_date}")
                print(f"Backers: {project.backers}")

