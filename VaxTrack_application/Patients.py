import sqlite3
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

from Notifications import Notification
from Health_worker import Patients

class Infants:
    def __init__(self, patient_id):
        self.patient_id = patient_id

    def view_my_info(self):
        Patients_sys.view_solo_info()
        while True:
            print("""
        ==================================
        How do you wish to continue
        ==================================
        ----------------------------------
        1. Return to the previous menu
        2. Exit
        """)
            question = input("Please enter your choice: ")
            if not question or not question.isdigit():
                print("Invalid input. enter (1-2)")
                continue
            if not question == "2" and not question == "1":
                print("Invalid input. Enter 1/2")
            if question == "2":
                print("Exiting. Goodbye")
                exit(1)
            if question == "1":
                break
            continue

    def view_my_notifications(self):
        Notification_sys.individual_notification()
        while True:
            print("""
    ==================================
    How do you wish to continue
    ==================================
    ----------------------------------
    1. Return to the previous menu
    2. Exit
    """)
            question = input("Please enter your choice: ")
            if not question or not question.isdigit():
                print("Invalid input. enter (1-2)")
                continue
            if not question == "2" and not question == "1":
                print("Invalid input. Enter 1/2")
            if question == "2":
                print("Exiting. Goodbye")
                exit(1)
            if question == "1":
                break
            continue

    def view_vaccination_records(self):
        patient_id = input("Enter the your patients ID to check the vaccination records")
        Notification_sys.vaccination_records()
        while True:
            print("""
        ==================================
        How do you wish to continue
        ==================================
        ----------------------------------
        1. Return to the previous menu
        2. Exit
        """)
            question = input("Please enter your choice: ")
            if not question or not question.isdigit():
                print("Invalid input. enter (1-2)")
                continue
            if not question == "2" and not question == "1":
                print("Invalid input. Enter 1/2")
            if question == "2":
                print("Exiting. Goodbye")
                exit(1)
            if question == "1":
                break
            continue

if __name__=='__main__':
    Infants = Infants(patient_id=int)
    def view_hospital_info_page():
        Patients.display_hospital_info()
        while True:
            print("""
        ==================================
        How do you wish to continue
        ==================================
        ----------------------------------
        1. Return to the previous menu
        2. Exit
        """)
            question = input("Please enter your choice: ")
            if not question or not question.isdigit():
                print("Invalid input. enter (1-2)")
                continue
            if not question == "2" and not question == "1":
                print("Invalid input. Enter 1/2")
            if question == "2":
                print("Exiting. Goodbye")
                exit(1)
            if question == "1":
                break
            continue

    def display_patients_menu():
        while True:
            print("""================WELCOME TO YOUR HEALTHCARE MENU==============
            1. VIEW INFO
            2. VIEW VACCINATION RECORDS
            3. VIEW NOTIFICATIONS
            4. VIEW HOSPITAL INFO PAGE
            5. EXIT
            """)
            menu_choice = input("Enter a menu option 1-6 to proceed: ")
            try:
                menu_choice = int(menu_choice)
            except ValueError:
                print("Invalid menu option choice.")
                exit()
            if menu_choice == 1:
                print("===========MY INFO PAGE=============")
                print("")
                Infants_sys.view_my_info()
            elif menu_choice == 2:
                print("===========MY VACCINATIONS PAGE=============")
                print("")
                Infants_sys.view_vaccination_records()
            elif menu_choice == 3:
                print("===========MY NOTIFICATIONS PAGE=============")
                print("")
                Infants_sys.view_my_notifications()
            elif menu_choice == 4:
                print("===========MY HOSPITAL INFO PAGE=============")
                print("")
                view_hospital_info_page()
            elif menu_choice == 5:
                print("==========EXITING, GOODBYE============")
                break
            else:
                print("Invalid menu option")
                continue

display_patients_menu()

conn.commit()


