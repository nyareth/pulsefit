# Test main function
def get_role() :
    print("Select Role:")
    print("1. Studio Administrator\n2. Booking Officer\n3. Member\n4. Accountant\n5. Maintenance Staff")
    role = int(input("~>"))
    if role < 0 or role > 5:
        return print("Enter Role 1-5")
    return role;

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

def admin_task():
    # (add, update, remove)")
    print("1. Manage classes and schedules (add, update, remove)")
    # 
    print("2. View all data (members, bookings, payments)")
    # (total bookings, revenue, most popular classes, available slots)
    print("3. Generate an overall report ")
    print("4. Exit")
    task = int(input("Admin# "))


def booking_task():
    print("Register new members")
    print("Process class bookings, cancellations and reschedules")
    print("View current bookings and member attendance history")

def member_task():
    pass

def accountant_task():
    pass

def maintence_task(): 
    pass

while (True):
    role = get_role()
    get_task(role)


