import time
import passmanager
import DBManager
import os

def show_menu():

    print("----------WELCOME TO THE PASSWORD MANAGER MENU----------")
    time.sleep(2)
    print("What would you like to do?")
    print("1. Create a new password?")
    print("2. Update/Remove a password")
    print("3. Retrieve a password")
    print("4. Display all passwords")
    print("5. Generate a password")
    print("6. Check a passwords strength")
    print("E. Exit")
    print("\n")

    def startup():

        if not os.path.exists('master.txt'):
            passmanager.first_time()
            DBManager.create_table()





    if passmanager.check_master():
        print("----------You're in!----------")
        time.sleep(0.5)
        print("-" * 30)
        time.sleep(0.5)

        while True:

            show_menu()
            choice = input("Please enter your choice: ")
            print("\n")
            if choice == "1":
                passmanager.addpassword()
            elif choice == "2":
                passmanager.update_password()
            elif choice == "3":
                passmanager.retrieve_password()
            elif choice == "4":
                passmanager.display_all()
            elif choice == "5":
                DBManager.close_db()
                break

    else:
        print("Your master password is not correct. Try Again. ")
        if __name__ == '__main__':
            startup()
