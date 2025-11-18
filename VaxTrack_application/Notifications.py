import sqlite3

conn = sqlite3.connect("my_database.db")

# Create a cursor that will be used to execute SQL codes
cursor = conn.cursor()

class Notification:
    def __init__(self, notification_id, patient_id, notification_type, notification,  sent_date):
        self.patient_id = patient_id
        self.notification_id = notification_id
        self.notification = notification
        self.notification_type = notification_type
        self.sent_date = sent_date

    def notification_sender(self):
        try:
            cursor.execute("""
                INSERT INTO notifications (patient_id, notification_type, notification, sent_date)
                VALUES (?, ?, ?, ?)
            """, (self.patient_id, self.notification_type, self.notification, self.sent_date))
            conn.commit()  # Commit the transaction here
            return f"""======Congratulations=====
    Message sent successfully
    -------------------------
    Message Summary
        Message: {self.notification}
        Date:    {self.sent_date}
        Sent to:  {self.patient_id}
        Status:   Sent
    -------------------------"""
        except sqlite3.Error as e:
            return f"An error occurred: {e}"

    def view_all_notifications(self):
        cursor.execute("""
SELECT * FROM notifications;
""")
        work = cursor.fetchall()
        print(work)
        for row in work:
            row = f"""{row[0]}  | {row[1]} | {row[2]} | {row[3]}                          | {row[4]}
"""
            print(row)

    def individual_notification(self):
        while True:
            patient_id = input("Enter your the patient ID to view notifications: ").strip()
            if not patient_id or not patient_id.isdigit():
                print("Invalid input: Enter a valid ID eg 10")
                continue

            cursor.execute(f"""
                    select patient_id from patients
                    where patient_id={patient_id};""")
            your_id = cursor.fetchall()
            try:
                your_id = your_id[0][0]
            except IndexError as e:
                print(f"Patient ID {patient_id} does not exist")
                continue

            if int(patient_id) == your_id:
                print(f"Welcome to the system\nYour ID is {patient_id}")
            cursor.execute(f"""
                        select notification_id, patient_id, notification_type, notification, sent_date from notifications where patient_id={self.patient_id}
                        order by {4} desc;
                        """)
            work = cursor.fetchall()
            print("=========Notification History=========")
            print(" ")
            for row in work:
                row = f"""====================================
    Type:      {row[2]}
    Date Sent: {row[4]}
    Message:   {row[3]}                 
    """
                print(row)


    def view_notifications_history(self):
        cursor.execute(f"""
        select * from patients
        where patient_id={self.patient_id};
""")
        infor = cursor.fetchall()
        for row in infor:
            return f"""
=========================================
Welcome to your health dashboard
=========================================

-----------------------------------------
Full name:       | {row[1]} {row[2]}
-----------------------------------------
Patient ID:      | {row[0]}
-----------------------------------------
Date of birth:   | {row[3]} 
-----------------------------------------
Patient Gender:  | {row[4]}
-----------------------------------------
Patient Contact: | {row[5]}
-----------------------------------------
Current Address: | {row[6]}, {row[7]}
-----------------------------------------"""

    def vaccination_records(self):
        cursor.execute(f"""
select * from vaccination_records
                    where patient_id={self.patient_id};
""")
        records = cursor.fetchall()
        print(" ")
        for line in records:
            return f"""
====================================
Welcome to your Vaccination Records
====================================

--------------------------------
Vaccine         | Status
--------------------------------
Hepatitis B I   | {line[1]}
--------------------------------
Hepatitis B II  | {line[3]}
--------------------------------
Hepatitis B III | {line[5]}
--------------------------------

Next vacciantion date: {line[7]}"""


if __name__=='__main__':
    Notification = Notification(notification_id=int, patient_id=int, notification_type=str, notification=str, sent_date=any)
    Notification.notification_sender()
    Notification.individual_notification()
    Notification.view_notifications_history()
    Notification.view_all_notifications()
    Notification.vaccination_records()

conn.commit()
