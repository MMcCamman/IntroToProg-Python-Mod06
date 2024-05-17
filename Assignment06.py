# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   McCamman, 2024/05/17, Completed Assignment
# ------------------------------------------------------------------------------------------ #

# Import Libraries
import json
import io as _io

# Define the Data Constants and Variables
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

menu_choice: str  # Hold the choice made by the user.
students: list   # a table of student data


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    McCamman, 2024-05-17,Created
    """

    @staticmethod
    def read_data_from_file(file_name: str):
        """
        Opens file and loads stored data

        ChangeLog: (Who, When, What)
        McCamman, 2024-05-17,Created
        """
        file = _io.TextIOWrapper
        student_data: list = []
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        writes any newly entered data to file

        ChangeLog: (Who, When, What)
        McCamman, 2024-05-17,Created
        """
        file = _io.TextIOWrapper
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()


# Input/Output --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    McCamman, 2024-05-17,Created
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        prints messages to user for any encountered errors

        ChangeLog: (Who, When, What)
        McCamman, 2024-05-17,Created
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        prints the menu

        ChangeLog: (Who, When, What)
        McCamman, 2024-05-17,Created
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """
        takes user input for menu selection

        ChangeLog: (Who, When, What)
        McCamman, 2024-05-17,Created
        """
        choice = "0"
        while choice not in ("1", "2", "3", "4"):
            choice = input("Please enter a valid menu choice number: ")
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        function to output current data

        ChangeLog: (Who, When, What)
        McCamman, 2024-05-17,Created
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data():
        """
        takes user input of student data

        ChangeLog: (Who, When, What)
        McCamman, 2024-05-17,Created
        """
        student_first_name: str
        student_last_name: str
        course_name: str
        student_data: dict = {}
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("There was a non-specific error!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


# Main Logic

students = FileProcessor.read_data_from_file(file_name=FILE_NAME)

# Repeat the follow tasks
while True:

    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students.append(IO.input_student_data())
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break

print("Program Ended")
