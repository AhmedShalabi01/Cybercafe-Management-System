import sys

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)
import queries as QUERIES


class user:
    def __init__(self, **kwargs):
        self.__first_name = kwargs.get("first_name")
        self.__last_name = kwargs.get("last_name")
        self.__phone_number = kwargs.get("phone_number")
        self.__address = kwargs.get("address")
        self.__age = kwargs.get("age")
        self.__role = kwargs.get("role")
        self.__password = kwargs.get("password")
        self.__user_name = kwargs.get("user_name")
        res = QUERIES.lookup_item("databases/users.json", self.__user_name)
        if res == None:
            QUERIES.save_item("databases/users.json", kwargs)

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
        QUERIES.update_attribute(
            "databases/users.json",
            self.__user_name,
            "first_name",
            first_name,
        )

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
        QUERIES.update_attribute(
            "databases/users.json",
            self.__user_name,
            "last_name",
            last_name,
        )

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number
        QUERIES.update_attribute(
            "databases/users.json",
            self.__user_name,
            "phone_number",
            phone_number,
        )

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address
        QUERIES.update_attribute(
            "databases/users.json",
            self.__user_name,
            "address",
            address,
        )

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age
        QUERIES.update_attribute(
            "databases/users.json",
            self.__user_name,
            "age",
            age,
        )

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role
        QUERIES.update_attribute(
            "databases/users.json",
            self.__user_name,
            "role",
            role,
        )

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
        QUERIES.update_attribute(
            "databases/users.json",
            self.__user_name,
            "password",
            password,
        )
