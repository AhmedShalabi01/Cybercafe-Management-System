from termcolor import colored


def get_numeric(placeholder, min_value=None, max_value=None):
    if min_value is not None and max_value is not None and max_value < min_value:
        raise ValueError(
            colored("min_value must be less than or equal to max_value.", "red")
        )
    while True:
        user_input = input(placeholder)
        try:
            user_input = int(user_input)
        except ValueError:
            print(colored("Input type must be in int.", "red"))
            continue
        if min_value == max_value:
            print(colored("Input must be equal to {0}.".format(max_value), "red"))
        elif max_value is not None and user_input > max_value:
            print(
                colored(
                    "Input must be less than or equal to {0}.".format(max_value), "red"
                )
            )
        elif min_value is not None and user_input < min_value:
            print(
                colored(
                    "Input must be greater than or equal to {0}.".format(min_value),
                    "red",
                )
            )
        else:
            return user_input


def get_phone_number(placeholder):
    while True:
        phone_number = input(placeholder)
        if len(phone_number) < 6 or len(phone_number) > 14:
            print(colored("phone number must be between 6 and 14 digits", "red"))
            continue
        return phone_number


def get_password(placeholder):
    # numbers_count = 0
    # capital_letters_count = 0
    while True:
        password = input(placeholder)
        # for char in password:
        #     if char.isnumeric():
        #         numbers_count += 1
        #     elif char.isupper():
        #         capital_letters_count += 1
        # if len(password) < 8:
        #     print(colored("password must have at least 8 letters", "red"))
        # elif numbers_count == 0:
        #     print(colored("password must have at least 1 number", "red"))
        # elif capital_letters_count == 0:
        #     print(colored("password must have at least 1 capital letter", "red"))
        # else:
        return password


def get_name(placeholder):
    while True:
        invalid_string = False
        name = input(placeholder)
        for char in name:
            if char.isnumeric():
                print(colored("name must be in letters only", "red"))
                invalid_string = True
                break
            if char.isspace():
                print(colored("name characters must be continous", "red"))
                invalid_string = True
                break
        if invalid_string:
            continue
        return name


def get_user_name(placeholder):
    while True:
        invalid_user_name = False
        user_name = input(placeholder)
        for char in user_name:
            if char.isspace():
                print(colored("user name must be wriiten without spaces", "red"))
                invalid_user_name = True
                break
            if char.isnumeric() or char.isalpha() or char == "_":
                continue
            else:
                print(
                    colored(
                        "user name supports only underscores '_' as a special character",
                        "red",
                    )
                )
                invalid_user_name = True
                break
        if invalid_user_name:
            continue
        return user_name


def get_address(placeholder):
    while True:
        invalid_address = False
        address = input(placeholder)
        for char in address:
            if (
                char.isnumeric()
                or char.isalpha()
                or char.isspace()
                or char == "_"
                or char == "-"
                or char == "."
                or char == ","
            ):
                continue
            else:
                invalid_address = True
                print(
                    colored(
                        "address supports only alphabet characters and '-', '_', ',' or '.' as special characters",
                        "red",
                    )
                )
                break
        if invalid_address:
            continue
        return address


def get_role(placeholder):
    while True:
        role = input(placeholder)
        if (
            role != "member"
            and role != "Member"
            and role != "admin"
            and role != "Admin"
        ):
            print(
                colored(
                    "member and admin roles are only supported",
                    "red",
                )
            )
            continue
        return role.lower()
