import sys
from termcolor import colored

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)

from classes.member import member
from classes.user import user
import validators as VALIDATORS
import queries as QUERIES


class admin(user):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_user(self, user_name):
        user_attributes = QUERIES.lookup_item("databases/users.json", user_name)
        if user_attributes != None:
            for key, value in user_attributes.items():
                print("user {} is {}".format(key, value))
        elif user_attributes == None:
            print(
                colored(
                    "USER DOES NOT EXISTS EXCEPTION: user name '{}' does not exist in the '{}' database".format(
                        user_name, "databases/users.json"
                    ),
                    "red",
                )
            )

    def add_new_user(self):
        first_name = VALIDATORS.get_name("\nEnter user first name: ")
        last_name = VALIDATORS.get_name("Enter user last name: ")
        user_name = VALIDATORS.get_user_name("Enter user name: ")

        res = QUERIES.lookup_item("databases/users.json", user_name)
        while res != None:
            suggested_user_name = QUERIES.suggest_user_name(user_name)
            res = QUERIES.lookup_item("databases/users.json", suggested_user_name)
            if res != None:
                continue
            print(
                colored(
                    "USER ALREADY EXISTS EXCEPTION: user name '{}' is already registered, you can use '{}' as a user name".format(
                        user_name, suggested_user_name
                    ),
                    "red",
                )
            )
            user_name = VALIDATORS.get_user_name("\nEnter user name: ")
            res = QUERIES.lookup_item("databases/users.json", user_name)

        age = VALIDATORS.get_numeric("Enter user age: ", 10)
        phone_number = VALIDATORS.get_phone_number("Enter user phone number: ")
        address = VALIDATORS.get_address("Enter user address: ")
        role = VALIDATORS.get_role("Enter user role (member or admin): ")
        password = VALIDATORS.get_password("Enter user password: ")

        user_attributes = {
            "first_name": first_name,
            "last_name": last_name,
            "user_name": user_name,
            "address": address,
            "phone_number": phone_number,
            "password": password,
            "role": role,
            "age": age,
        }
        if role == "admin":
            user_object = admin(**user_attributes)
        elif role == "member":
            credit = int(input("Enter member credit: "))
            user_attributes["credit"] = credit
            user_object = member(**user_attributes)
        return user_object

    def update_record(self, user_name, key, value):
        user_object = construct_object(user_name)
        setattr(user_object, key, value)

    def show_records(self):
        QUERIES.lookup_all_database("databases/users.json")

    def delete_record(self, user_name):
        QUERIES.delete_item("databases/users.json", user_name)


def construct_object(user_name):
    user_attributes = QUERIES.lookup_item("databases/users.json", user_name)
    if user_attributes["role"] == "admin":
        constructed_object = admin(**user_attributes)
    elif user_attributes["role"] == "member":
        constructed_object = member(**user_attributes)
    return constructed_object
