def get_role() :
    print("Select Role:")
    print("1. Studio Administrator\n2. Booking Officer\n3. Member\n4. Accountant\n5. Maintenance Staff")
    role = int(input("Enter Role (1-5): "))
    if role < 0 or role > 5:
        return print("Enter Role 1-5")
    return role;

def view_menu():
    print("Pick an option")
    print(" 1. Members \n 2. Bookings \n 3. Payments \n 4. Classes")
    task = int(input("Enter Option (1-4): "))
    if task == 1:
        members_file = open("data/members.txt")
        for line in members_file:
            print(line)

def admin_task():
    # (add, update, remove)")
    print("1. Manage classes and schedules (add, update, remove)")
    # 
    print("2. View all data (members, bookings, payments)")
    # (total bookings, revenue, most popular classes, available slots)
    print("3. Generate an overall report ")
    print("4. Exit")
    task = int(input("Admin# "))
    if task == 2:
        view_menu()


def booking_task():
    print("1. Register new members")
    print("2. Process class bookings, cancellations and reschedules")
    print("3. View current bookings and member attendance history")

def member_task():
    pass

def accountant_task():
    pass

def maintence_task(): 
    pass

def get_task (role):
    if role == 1:
        admin_task()
    elif role == 2:
        booking_task()
    elif role == 3:
        member_task()
    elif role == 4:
        accountant_task()
    elif role == 5:
        maintence_task()
while True:
    role = get_role()
    get_task(role)

