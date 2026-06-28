
import csv
import json
import logging
import os

CSV_FILE = "students.csv"
JSON_FILE = "students.json"
LOG_FILE = "student_system.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class StudentExistsError(Exception):
    """
    Raised when a registration number already exists.
    """
    pass

def initialize_files():
    """
    Creates CSV and JSON files if they do not exist.
    """

    try:

        if not os.path.exists(CSV_FILE):

            with open(CSV_FILE, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow(
                    [
                        "RegistrationNo",
                        "Name",
                        "Age",
                        "Gender"
                    ]
                )

        if not os.path.exists(JSON_FILE):

            with open(JSON_FILE, "w") as file:

                json.dump({}, file, indent=4)

    except Exception as e:

        logging.error(f"Initialization Error : {e}")

def load_students():

    students = []

    try:

        with open(CSV_FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    except FileNotFoundError:

        print("CSV File not found.")

        logging.error("CSV File Missing")

    except Exception as e:

        print("Error loading students.")

        logging.error(e)

    return students


def save_students(student_list):

    try:

        with open(CSV_FILE, "w", newline="") as file:

            fieldnames = [
                "RegistrationNo",
                "Name",
                "Age",
                "Gender"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(student_list)

    except Exception as e:

        logging.error(e)


def load_details():

    try:

        with open(JSON_FILE, "r") as file:

            return json.load(file)

    except FileNotFoundError:

        return {}

    except json.JSONDecodeError:

        return {}

    except Exception as e:

        logging.error(e)

        return {}


def save_details(details):

    try:

        with open(JSON_FILE, "w") as file:

            json.dump(details, file, indent=4)

    except Exception as e:

        logging.error(e)


def student_exists(reg_no):

    students = load_students()

    for student in students:

        if student["RegistrationNo"] == reg_no:

            return True

    return False


def add_student():

    try:

        print("\n===== ADD NEW STUDENT =====")

        reg = input("Registration Number : ").strip()

        if student_exists(reg):
            raise StudentExistsError(
                "Registration Number Already Exists."
            )

        name = input("Student Name : ").strip()

        age = input("Age : ").strip()

        if not age.isdigit():
            raise ValueError("Age must be a number.")

        gender = input("Gender : ").strip()

        address = input("Address : ").strip()

        contact = input("Contact : ").strip()

        program = input("Program : ").strip()

        students = load_students()

        students.append({

            "RegistrationNo": reg,

            "Name": name,

            "Age": age,

            "Gender": gender

        })

        save_students(students)

        details = load_details()

        details[reg] = {

            "Address": address,

            "Contact": contact,

            "Program": program

        }

        save_details(details)

        print("\nStudent Added Successfully.")

        logging.info(f"Student Added : {reg}")

    except StudentExistsError as e:

        print(e)

        logging.error(e)

    except ValueError as e:

        print(e)

        logging.error(e)

    except Exception as e:

        print(f"\nUnexpected Error: {e}")

        logging.exception("Unexpected Error")

    finally:

        print("Add Student Operation Completed.\n")
        

def view_students():
    
    try:

        students = load_students()
        details = load_details()

        if len(students) == 0:
            print("\nNo student records found.")
            return

        print("\n" + "=" * 80)
        print("                     STUDENT RECORDS")
        print("=" * 80)

        for student in students:

            reg = student["RegistrationNo"]

            print(f"\nRegistration Number : {reg}")
            print(f"Name                : {student['Name']}")
            print(f"Age                 : {student['Age']}")
            print(f"Gender              : {student['Gender']}")

            if reg in details:

                print(f"Address             : {details[reg]['Address']}")
                print(f"Contact             : {details[reg]['Contact']}")
                print(f"Program             : {details[reg]['Program']}")

            print("-" * 80)

        logging.info("Viewed all student records.")

    except Exception as e:

        print("Error displaying students.")

        logging.error(e)

    finally:

        print()
        
        
def search_student():
    try:

        reg = input("\nEnter Registration Number: ").strip()

        students = load_students()
        details = load_details()

        found = False

        for student in students:

            if student["RegistrationNo"] == reg:

                found = True

                print("\nStudent Found")
                print("-" * 40)

                print(f"Registration Number : {reg}")
                print(f"Name                : {student['Name']}")
                print(f"Age                 : {student['Age']}")
                print(f"Gender              : {student['Gender']}")

                if reg in details:

                    print(f"Address             : {details[reg]['Address']}")
                    print(f"Contact             : {details[reg]['Contact']}")
                    print(f"Program             : {details[reg]['Program']}")

                logging.info(f"Searched Student : {reg}")

                break

        if not found:

            print("\nStudent not found.")

            logging.warning(f"Search failed for {reg}")

    except Exception as e:

        print("Search failed.")

        logging.error(e)

    finally:

        print()


def update_student():
    """
    Updates a student's information.
    """

    try:

        reg = input("\nEnter Registration Number to Update: ").strip()

        students = load_students()
        details = load_details()

        found = False

        for student in students:

            if student["RegistrationNo"] == reg:

                found = True

                print("\nLeave blank to keep existing value.\n")

                name = input(
                    f"Name ({student['Name']}): "
                ).strip()

                age = input(
                    f"Age ({student['Age']}): "
                ).strip()

                gender = input(
                    f"Gender ({student['Gender']}): "
                ).strip()

                if name:
                    student["Name"] = name

                if age:

                    if not age.isdigit():
                        raise ValueError("Age must be numeric.")

                    student["Age"] = age

                if gender:
                    student["Gender"] = gender

                if reg in details:

                    address = input(
                        f"Address ({details[reg]['Address']}): "
                    ).strip()

                    contact = input(
                        f"Contact ({details[reg]['Contact']}): "
                    ).strip()

                    program = input(
                        f"Program ({details[reg]['Program']}): "
                    ).strip()

                    if address:
                        details[reg]["Address"] = address

                    if contact:
                        details[reg]["Contact"] = contact

                    if program:
                        details[reg]["Program"] = program

                save_students(students)
                save_details(details)

                print("\nStudent Updated Successfully.")

                logging.info(f"Updated Student : {reg}")

                break

        if not found:

            print("\nStudent not found.")

            logging.warning(f"Update failed : {reg}")

    except ValueError as e:

        print(e)

        logging.error(e)

    except Exception as e:

        print("Update failed.")

        logging.error(e)

    finally:

        print()


def delete_student():
    """
    Deletes a student record.
    """

    try:

        reg = input("\nEnter Registration Number to Delete: ").strip()

        students = load_students()
        details = load_details()

        found = False

        for student in students:

            if student["RegistrationNo"] == reg:

                students.remove(student)

                found = True

                break

        if not found:

            print("\nStudent not found.")

            logging.warning(f"Delete failed : {reg}")

            return

        if reg in details:

            del details[reg]

        save_students(students)
        save_details(details)

        print("\nStudent Deleted Successfully.")

        logging.info(f"Deleted Student : {reg}")

    except Exception as e:

        print("Delete operation failed.")

        logging.error(e)

    finally:

        print()
        

def display_menu():
    """
    Displays the main menu.
    """

    print("\n" + "=" * 50)
    print("      STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 50)


def main():
    """
    Main program loop.
    """

    # Create files if they don't exist
    initialize_files()

    while True:

        display_menu()

        try:

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":

                add_student()

            elif choice == "2":

                view_students()

            elif choice == "3":

                search_student()

            elif choice == "4":

                update_student()

            elif choice == "5":

                delete_student()

            elif choice == "6":

                print("\nThank you for using the Student Record Management System.")

                logging.info("System exited successfully.")

                break

            else:

                print("\nInvalid choice. Please enter a number between 1 and 6.")

                logging.warning(f"Invalid menu choice: {choice}")

        except KeyboardInterrupt:

            print("\n\nProgram interrupted by user.")

            logging.warning("Program interrupted using keyboard.")

            break

        except Exception as e:

            print("An unexpected error occurred.")

            logging.error(e)

        finally:

            print("-" * 50)

if __name__ == "__main__":
    main()