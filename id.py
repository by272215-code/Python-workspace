import csv
import os
from datetime import datetime
# Student database
students = {
    "005": "Vaibhav",
    "032": "Abhishek", 
    "030": "Raja",
    "002": "Bittu Kumar",
     "082": "Ashutosh",
    "006": "Rajnish",
    "083": "pradeep",
    "085": "Sadhiya"
}
CSV_FILE = 'attendance.csv'
def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Time', 'ID', 'Name', 'Status'])
def log_attendance(id, name):
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([t, id, name, 'PRESENT'])
    return t
print("=== Student ID Card Monitoring System ===")
init_csv()
while True:
    card_id = input("Enter Card ID: ").strip()
    if card_id in students:
        name = students[card_id]
        timestamp = log_attendance(card_id, name)
        print(f"✓ Access Granted: {name} [{timestamp}]")
        print("Attendance marked!")
    else:
        print("✗ Invalid Card! Security Alert!")
