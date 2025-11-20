from Health_worker import display_health_workers_menu, Patients
from Patients_menu import display_patients_menu, Infants
from datetime import datetime

def menus():
    print(f"""
          ===========================================================
                WELCOME TO YOUR CARING HEALTHCARE PARTNER 
          ===========================================================
                      VACCINATION TRACKING SYSTEM
          -------------------{datetime.now().date()}------------------------------

          1. HEALTH PROFESSIONAL MENU
          2. PATIENTS MENU
          3. EXIT
           """)
    menu_choice = input("Enter a menu option to continue: ")
    try:
        menu_choice = int(menu_choice)
    except ValueError as e:
        print("Invalid menu option. Please select 1-3.")
        return
    if menu_choice == 1:
        print("")
        Health_worker_instance = Patients(patient_id=0) 
        display_health_workers_menu(Health_worker_instance)
    elif menu_choice == 2:
        print("------------------ENTER PATIENT ID-------------------")
        patient_id_input = input("Enter your Patient ID to access your menu: ").strip()
        if patient_id_input.isdigit():
            Infants_instance = Infants(patient_id=int(patient_id_input))
            display_patients_menu(Infants_instance)
        else:
            print("Invalid Patient ID. Please enter a number.")
    elif menu_choice == 3:
        print("")
        print("=========EXITING GOOD BYEE!!!===========")
    else:
        print("")
        print("Invalid menu option. Please select 1-3.")

if __name__=='__main__':
    menus()
