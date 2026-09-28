class Student:
    def set(details):

        print("..WELCOME TO THE SMART STUDY ASSISTANT..")
        print("...LET SIGN IN FIRST...")

        details.name= input("\n ENTER THE STUDENT NAME:")
        details.course = input("\n ENTER THE COURSE OF THE STUDENT:")
        details.semester = input("\n ENTER THE SEMESTER OF THE STUDENT:")

    def show(details):
        print("\n THE NAME OF THE STUDENT IS:",details.name)
        print("\n THE COURSE OF THE STUDENT IS:",details.course)    
        print("\n THE SEMESTER OF THE STUDENT IS:",details.semester)
