from datetime import datetime
students = {
    "102": "Bittu",
    "132": "Abhishek",
    "130": "Raja",
    "182": "Ashutosh",
    "106": "Rajnish",
    "183": "pradeep",
    "185": "Sadhiya",
    "184": "Alok",
}
print("Scan Student ID Card")
while True:
    card_id =input("Enter Card ID:")
    now = datetime.now()
    formatted_datetime = now.strftime("%Y%m%D %H:%M:%S")
    if card_id in students:
        print("Access Granted:", students[card_id])
        print("Attendance Marked\n",formatted_datetime)
        print()
    else:
        print("Invalid Card! Alert\n",formatted_datetime)
        print()


