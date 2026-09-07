def get_role() :
    print("Select Role:")
    print("1. Studio Administrator\n2. Booking Officer\n3. Member\n4. Accountant\n5. Maintenance Staff\n0. Exit")
    print("")
    role = int(input("Enter Role: "))
    if role < 0 or role > 5:
        print("Invalid option")
        return print("Enter Role 1-5")
    return role;
print("")


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


#DEF VIEW
def view_members () :
    members_file = open("data/members.txt")
    for line in members_file:
        print(line)

def view_bookings () :
    bookings_file = open("data/bookings.txt")
    for line in bookings_file:
        print(line)

def view_payments ():
    payments_file = open("data/payments.txt")
    for line in payments_file:
        print(line)
def view_classes () :
    classes_file = open("data/classes.txt")
    for line in classes_file:
        print(line)

#ADMIN ROLES
def admin_task():

    print("")
    print("--------------------------------\n      Studio Administrator      \n--------------------------------")
    print("Select Role:")
    print("1. Manage classes and schedules (add, update, remove)")
    print("2. View all data (members, bookings, payments)")
    # (total bookings, revenue, most popular classes, available slots)
    print("3. Generate an overall report ")
    print("4. Exit")
    task = int(input("Enter option (1-4): "))
    if task == 1:
        print("1. Add\n2. Update\n3. Remove")
        if task == 1:
            add_classes()


    if task == 2:
        print("")
        print("Pick an Option")
        print("1. Members\n2. Bookings\n3. Payments\n4. Exit")
        option = int(input("Enter an option (1-4): "))
        if option == 1:
            view_members()
        elif option == 2:
            view_bookings()
        elif option == 3:
            view_payments()
        elif option == 4:
            return task


# (add, update, remove)")
def add_classes():
    print("-------Add Classes--------")

    class_id = (input("Enter Class ID: "))
    name = input("Enter class name: ")
    instructor = input("Enter instructor name: ")
    data = input("Enter data YYYY/MM/DD: ")
    time = input(f"Enter time HM:MM : ")
    slots = input ("Enter available slots: ")
    status = "Active"
    price = input("Enter price (e.g: 25.00): ")

    new_line = f"{class_id}|{name}|{instructor}|{data}|{time}|{slots}|{status}|{price}\n"
    classes_file = open("data/classes.txt","a")
    classes_file.write(new_line)
    classes_file.close()

    print("Congratulations! Class Added successfully")














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

    # get role
role = get_role()
get_task(role)