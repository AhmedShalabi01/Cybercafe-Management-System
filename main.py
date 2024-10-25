import os
from termcolor import colored

import validators as VALIDATORS
import queries as QUERIES

from classes.session import session
from classes import computer, drinks

import classes.admin as ADMIN

comp = computer.computer()
drink = drinks.drinks()


def main():
    print("\n\nWelcome to cybercafe management system\n\n")
    print("1. Admin login")
    print("2. Terminate Progrm")
    main_input = VALIDATORS.get_numeric("\n> ", 1, 2)

    while main_input != 2:
        if main_input == 1:
            login_input = None
            while login_input != 2:
                os.system("clear")
                user_name = VALIDATORS.get_user_name("Enter your user name: ")
                password = VALIDATORS.get_password("Enter your password: ")
                user_attributes = QUERIES.lookup_item("databases/users.json", user_name)
                if user_attributes == None or password != user_attributes["password"]:
                    print(
                        colored(
                            "\nINCORRECT USER INFORMSTION EXCEPTION",
                            "red",
                        )
                    )
                    print("\nChoose an option to continue:")
                    print("1. try to login again")
                    print("2. return")
                    login_input = VALIDATORS.get_numeric("> ", 1, 2)
                    if login_input == 1:
                        continue
                    else:
                        break

                role = user_attributes.get("role")
                if role == "admin":
                    admin_object = ADMIN.construct_object(user_name)
                    os.system("clear")
                    print(
                        "\n\nWelcome to cybercafe management system admin dashboard\n\n"
                    )
                    print("1. master entry")
                    print("2. cafe management")
                    print("3. admin logout")
                    admin_input = VALIDATORS.get_numeric("\n> ", 1, 3)

                    while admin_input != 3:
                        if admin_input == 1:
                            master_entry_input = None
                            # master entry options starts here
                            while master_entry_input != 4:
                                os.system("clear")
                                print("1. user entry")
                                print("2. computer entry")
                                print("3. return")
                                master_entry_input = VALIDATORS.get_numeric(
                                    "\n> ", 1, 3
                                )
                                if master_entry_input == 1:
                                    user_entry_input = None
                                    while user_entry_input != 6:
                                        os.system("clear")
                                        print("1. Add New User")
                                        print("2. Show User")
                                        print("3. Update Record")
                                        print("4. Delete Record")
                                        print("5. Show Records")
                                        print("6. Return")
                                        user_entry_input = VALIDATORS.get_numeric(
                                            "\n> ", 1, 6
                                        )
                                        if user_entry_input == 1:
                                            # 1. Add New User
                                            os.system("clear")
                                            admin_object.add_new_user()
                                        elif user_entry_input == 2:
                                            # 2. Show User
                                            while True:
                                                os.system("clear")
                                                user_name_input = (
                                                    VALIDATORS.get_user_name(
                                                        "Enter user name: "
                                                    )
                                                )
                                                admin_object.show_user(user_name_input)
                                                show_user_option_input = VALIDATORS.get_numeric(
                                                    "\n\nChoose an option to continue: \n1. show another user\n2. return\nYour input is: ",
                                                    1,
                                                    2,
                                                )
                                                if show_user_option_input == 2:
                                                    break

                                        elif user_entry_input == 3:
                                            # 3. Update Record
                                            while True:
                                                os.system("clear")
                                                user_name_input = (
                                                    VALIDATORS.get_user_name(
                                                        "Enter user name: "
                                                    )
                                                )
                                                user_key = input(
                                                    "Enter attribute name: "
                                                )
                                                user_value = input(
                                                    "Enter new value of {}: ".format(
                                                        user_key
                                                    )
                                                )

                                                admin_object.update_record(
                                                    user_name_input,
                                                    user_key,
                                                    user_value,
                                                )

                                                print(
                                                    "\n{} attributes after updating are: \n".format(
                                                        user_name_input
                                                    )
                                                )
                                                admin_object.show_user(user_name_input)
                                                update_user_option_input = VALIDATORS.get_numeric(
                                                    "\n\nChoose an option to continue: \n1. update attribute of another user\n2. return\nYour input is: ",
                                                    1,
                                                    2,
                                                )
                                                if update_user_option_input == 2:
                                                    break
                                        elif user_entry_input == 4:
                                            # 4. Delete Record
                                            os.system("clear")
                                            user_name_input = VALIDATORS.get_user_name(
                                                "Enter user name: "
                                            )
                                            admin_object.delete_record(user_name_input)
                                        elif user_entry_input == 5:
                                            # 5. Search Record
                                            os.system("clear")
                                            admin_object.show_records()
                                            while True:
                                                search_records_option_input = VALIDATORS.get_numeric(
                                                    "\n\nChoose an option to continue: \n1. return\nYour input is: ",
                                                    1,
                                                )
                                                if search_records_option_input == 1:
                                                    break
                                elif master_entry_input == 2:
                                    computer_entry_input = None
                                    while computer_entry_input != 6:
                                        os.system("clear")
                                        print("1. Add New Computer")
                                        print("2. Show Computer")
                                        print("3. Update Record")
                                        print("4. Delete Record")
                                        print("5. Search Record")
                                        print("6. Return")
                                        computer_entry_input = VALIDATORS.get_numeric(
                                            "\n> ", 1, 6
                                        )
                                        if computer_entry_input == 1:
                                            # 1. Add New Computer
                                            while True:
                                                cpu = input(
                                                    "Please enter the cpu model :"
                                                )
                                                if cpu != "":
                                                    break
                                                print("Error : Empty input")

                                            while True:
                                                ram = input(
                                                    "Please enter the ram size :"
                                                )
                                                if ram != "":
                                                    break
                                                print("Error : Empty input")

                                            while True:
                                                gpu = input(
                                                    "Please enter the gpu model :"
                                                )
                                                if gpu != "":
                                                    break
                                                print("Error : Empty input")

                                            while True:
                                                storage = input(
                                                    "Please enter the storage size :"
                                                )
                                                if storage != "":
                                                    break
                                                print("Error : Empty input")

                                            Comp = computer.computer(
                                                cpu, ram, gpu, storage
                                            )
                                            cpu = None
                                            ram = None
                                            gpu = None
                                            storage = None

                                        elif computer_entry_input == 2:
                                            print(comp.Show_All_Computers())

                                        elif computer_entry_input == 3:
                                            # 3. Update Record
                                            while True:
                                                computer_id = input(
                                                    "Please enter the computer ID :"
                                                )
                                                if computer_id != "":
                                                    break
                                                print("Error : Empty input")

                                            while True:
                                                cpu = input(
                                                    "Please enter the cpu model :"
                                                )
                                                if cpu != "":
                                                    break
                                                print("Error : Empty input")

                                            while True:
                                                ram = input(
                                                    "Please enter the ram size :"
                                                )
                                                if ram != "":
                                                    break
                                                print("Error : Empty input")

                                            while True:
                                                gpu = input(
                                                    "Please enter the gpu model :"
                                                )
                                                if gpu != "":
                                                    break
                                                print("Error : Empty input")

                                            while True:
                                                storage = input(
                                                    "Please enter the storage size :"
                                                )
                                                if storage != "":
                                                    break
                                                print("Error : Empty input")

                                            comp.Update_Record(
                                                computer_id,
                                                cpu,
                                                ram,
                                                gpu,
                                                storage,
                                            )
                                            computer_id = None
                                            cpu = None
                                            ram = None
                                            gpu = None
                                            storage = None

                                        elif computer_entry_input == 4:
                                            # 4. Delete Record
                                            while True:
                                                computer_id = int(
                                                    input(
                                                        "Please enter the computer ID :"
                                                    )
                                                )
                                                if computer_id != "":
                                                    break
                                                print("Error : Empty input")
                                            comp.Delete_Computer_by_index(computer_id)
                                            computer_id = None

                                        elif computer_entry_input == 5:
                                            # 5. Search Record
                                            while True:
                                                Key_word = input(
                                                    "What do you want to search about? "
                                                )
                                                if Key_word != "":
                                                    break
                                                print("Error : Empty input")
                                            print(comp.Search_Record(Key_word))
                                            Key_word = None

                                elif master_entry_input == 3:
                                    # return option
                                    break

                        elif admin_input == 2:
                            cafe_management_entry_input = None
                            # cafe management options start here
                            while cafe_management_entry_input != 3:
                                os.system("clear")
                                print("1. Bookings")
                                print("2. Drinks")
                                print("3. Return")
                                cafe_management_entry_input = VALIDATORS.get_numeric(
                                    "\n> ", 1, 3
                                )
                                if cafe_management_entry_input == 1:
                                    # bookings
                                    session_entry_input = None
                                    while session_entry_input != 4:
                                        os.system("clear")
                                        print("1. Start New Session")
                                        print("2. End Existing Session")
                                        print("3. Show Booking table")
                                        print("4. Return")
                                        session_entry_input = VALIDATORS.get_numeric(
                                            "\n> ", 1, 4
                                        )
                                        if session_entry_input == 1:
                                            user_name = VALIDATORS.get_user_name(
                                                "Enter user name: "
                                            )
                                            res = QUERIES.lookup_item(
                                                "databases/users.json",
                                                user_name,
                                            )
                                            if res != None:
                                                session_obj = session(user_name)
                                                session_obj.start_session()
                                            else:
                                                print(
                                                    colored(
                                                        "\nUSER DOES NOT EXIST EXCEPTION: user '{}' does not exist in '{}' database".format(
                                                            user_name,
                                                            "databases/users.json",
                                                        ),
                                                        "red",
                                                    )
                                                )
                                        elif session_entry_input == 2:
                                            session.end_session()

                                        elif session_entry_input == 3:
                                            print(session.show_all_sessions())

                                        elif session_entry_input == 4:
                                            # 4. return
                                            break
                                elif cafe_management_entry_input == 2:
                                    # drinks management options start here
                                    drinks_entry_input = None
                                    while drinks_entry_input != 7:
                                        os.system("clear")
                                        print("1. Add New Drink")
                                        print("2. Show Drinks")
                                        print("3. Update Record")
                                        print("4. Delete Record")
                                        print("5. Search Record")
                                        print("6. Buy a drink")
                                        print("7. Return")
                                        drinks_entry_input = VALIDATORS.get_numeric(
                                            "\n> ", 1, 7
                                        )
                                        if drinks_entry_input == 1:
                                            # 1. Add New Drink
                                            while True:
                                                drink_name = input(
                                                    "Please enter the drink name :"
                                                )
                                                if drink_name != "":
                                                    break
                                                print("Error : Empty input")

                                            while True:
                                                drink_Price = input(
                                                    "Please enter the drink Price :"
                                                )
                                                if drink_Price != "":
                                                    break
                                                print("Error : Empty input")

                                            Drink = drinks.drinks(
                                                drink_name, drink_Price
                                            )
                                            drink_name = None
                                            drink_Price = None

                                        elif drinks_entry_input == 2:
                                            # 2. Show Drinks
                                            print(drink.Show_All_Drinks())

                                        elif drinks_entry_input == 3:
                                            # 3. Update Record
                                            while True:
                                                Drink_id = int(
                                                    input("Please enter the drink ID :")
                                                )
                                                if Drink_id != "":
                                                    break
                                                print("Error : Empty input")

                                            while True:
                                                drink_name = input(
                                                    "Please enter the drink name :"
                                                )
                                                if drink_name != "":
                                                    break
                                                print("Error : Empty input")

                                            while True:
                                                drink_Price = input(
                                                    "Please enter the drink Price :"
                                                )
                                                if drink_Price != "":
                                                    break
                                                print("Error : Empty input")

                                            drink.Update_Record(
                                                Drink_id,
                                                drink_name,
                                                drink_Price,
                                            )
                                            drink_name = None
                                            Drink_id = None
                                            drink_Price = None

                                        elif drinks_entry_input == 4:
                                            # 4. Delete Record
                                            while True:
                                                Drink_id = int(
                                                    input("Please enter the drink ID :")
                                                )
                                                if Drink_id != "":
                                                    break
                                                print("Error : Empty input")
                                            drink.Delete_Drink_by_index(Drink_id)
                                            Drink_id = None

                                        elif drinks_entry_input == 5:
                                            # 5. Search Record
                                            while True:
                                                Key_word = input(
                                                    "What do you want to search about? "
                                                )
                                                if Key_word != "":
                                                    break
                                                print("Error : Empty input")
                                            print(comp.Search_Record(Key_word))
                                            Key_word = None

                                        elif drinks_entry_input == 6:
                                            # 5. Buy a drink
                                            while True:
                                                Drink_ID = int(input("Drink ID: "))
                                                if Drink_ID != "":
                                                    break
                                                print("Error : Empty input")

                                            while True:
                                                Session_ID = int(input("Session ID: "))
                                                if Session_ID != "":
                                                    break
                                                print("Error : Empty input")
                                            drink.Buy_a_drink(Session_ID, Drink_ID)
                                            Session_ID = None
                                            Drink_ID = None

                                        elif drinks_entry_input == 7:
                                            break

                        elif admin_input == 3:
                            # logout admin
                            break

                        os.system("clear")
                        print("1. master entry")
                        print("2. cafe management")
                        print("3. logout admin")
                        admin_input = VALIDATORS.get_numeric("\n> ", 1, 3)

                    if admin_input == 3:
                        # go to initial screen when admin is logged out
                        break

        os.system("clear")
        print("1. Admin login")
        print("2. Terminate Progrm")
        main_input = VALIDATORS.get_numeric("\n> ", 1, 2)

    os.system("clear")
    exit()


main()
