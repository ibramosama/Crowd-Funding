import sys

from Project import Project
from CreateProject import create_project
from User import User
from viewProject import view_projects
from searchProject import search_projects
import Authentication


Useremail=""

def login():
    global Useremail

    # prompt user for login details
    email = input("Enter email: ")
    password = input("Enter password: ")
    # attempt to login user
    user = User("","",email, password,"")
    if user.login():
        print("Login successful")
        Useremail = email
        return True
    else:
        print("Invalid email or password")
        return False


def mainMenu():
    global Useremail
    choice = input("Please enter\n1 for register\n2 for Login \n")

    if choice == "1":
        Authentication.register()
        mainMenu()
    elif choice == "2":
        m=login()
        if m==True :
            projectsMenu()
        mainMenu()
    else:
        print("please enter valid choice")
        mainMenu()

def projectsMenu():


    print("================================================================")
    choice = input("please enter your choice\n1) Create you project\n2) view all project \n3) edit in your project  \n4) delete in your project \n5) search for projects by date \n6) Return to main menu \n7)exit\ns")
    if choice == "1":
        create_project(Useremail)
        projectsMenu()
    elif choice == "2":
        view_projects()
        projectsMenu()
    elif choice == "3":
        title = input("enter the project title which you want update: ")
        Project.edit_project(title, Useremail)
        projectsMenu()
    elif choice == "4":
        title = input("enter the project title which you want delete: ")
        Project.delete_project(title, Useremail)
        projectsMenu()
    elif choice == "5":
        search_projects()
        projectsMenu()
    elif choice == "6":
        mainMenu()
    elif choice == "6":
        sys.exit("Good Bye")
    else:
        print("please enter valid choice")
        projectsMenu()

mainMenu()
