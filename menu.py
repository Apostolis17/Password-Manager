# menu will display options onto screen
# terminal or Tkinter GUI?
import time
import pass_manager
import db_manager

print("--------Hello---------")
time.sleep(1)
print("--------Welcome to Your Password Manager----------")
time.sleep(1)
# pwd = input("---------Please Enter the Master Password: ")

# if pwd == master_password - from hash_script:
# login_succes()


def login_success():
    print("---You're logged in!---")
    print("What would you like to do?")
    print("1. Add a new password")
    print("2. Update/Remove a password")
    print("3. Retrieve a password")
    print("4. Display all passwords")
    print("5. Exit")


while True:
    login_succ2ess()
    choice = input("Please enter your choice: ")
    if choice == "1":
        pass_manager.add_password()
    elif choice == "2":
        pass_manager.update_password()
    elif choice == "3":
        pass_manager.retrieve_password()
    elif choice == "4":
        db_manager.print_keys()
    elif choice == "5":
        db_manager.close_db()
        break

    # if 1. is selected, open add new password menu from pass_manager.py
    # if 2. is selected open update password function from pass_manager
    # if 3. is selected open retrieve password function from pass_manager
    # if 4 is selected, display all passwords
    # if 5 is selected, exit


# first display will take input for master password
# check if master_password matches, if so, grant access
# OR provide menu options, then ask for master password if someone selects option to
# see passwords
# options will include:
# 1. Enter a new password
# 		-Enter Service
#		-Enter Username
#		-Enter Password
#		-Upon button click, activate DB script to send data to database
# 2. Remove a password
# 3. View list of passwords
#
