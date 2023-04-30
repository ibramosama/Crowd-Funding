from datetime import datetime


def search_projects():
    print("Search for projects")
    search_field = input("Enter field to search by (title/details/total_target/start_date/end_date): ")
    while search_field not in ['title', 'details', 'total_target', 'start_date', 'end_date']:
        print("invalid search field")
        search_field = input("Enter field to search by (title/details/total_target/start_date/end_date): ")
    search_query = input(f"Enter {search_field} to search for: ")

    # retrieve projects from database that match search query
    projects = []
    with open('projects.txt', 'r') as f:
        for line in f:
            data = line.strip().split(':')
            if len(data) < 6:
                continue
            project_dict = {
                'title': data[0],
                'details': data[1],
                'total_target': float(data[2]),
                'start_date': datetime.strptime(data[3], '%Y-%m-%d').date(),
                'end_date': datetime.strptime(data[4], '%Y-%m-%d').date(),
                'user_email': data[5]
            }
            if search_query.lower() in str(project_dict[search_field]).lower():
                projects.append(project_dict)

    # display search results
    if not projects:
        print("No projects found.")
    else:
        print("Search results:")
        for project in projects:
            print(f"Title: {project['title']}\nDetails: {project['details']}\nTarget Amount: {project['total_target']}\n"
                  f"Start Date: {project['start_date']}\nEnd Date: {project['end_date']}\nUser Email: {project['user_email']}")
