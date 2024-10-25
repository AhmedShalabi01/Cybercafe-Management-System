import sys
import json
from termcolor import colored

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)


def lookup_item(database, item):
    with open(database, "r") as json_database:
        dict_database = json.load(json_database)
        for entry in dict_database:
            for item_name in entry:
                if item_name == item:
                    json_database.close()
                    return entry[item_name]


def lookup_all_database(database):
    with open(database, "r") as json_database:
        dict_database = json.load(json_database)
        for entry in dict_database:
            print(entry)
        json_database.close()


def update_attribute(database, item, key, value):
    count = -1
    index = None
    json_database = open(database, "r")
    updated_dict_database = json.load(json_database)
    for entry in updated_dict_database:
        for item_name in entry:
            count += 1
            if item_name == item:
                index = count
                break
        if index != None:
            json_database.close()
            break
    if index != None:
        updated_dict_database[index][item][key] = value
        jsonFile = open(database, "w+")
        jsonFile.write(json.dumps(updated_dict_database, indent=4))
        jsonFile.close()
    elif index == None:
        print(
            colored(
                "\nERROR update_attribute(): the item '{}' does not exist in the '{}' database".format(
                    item, database
                ),
                "red",
            )
        )


def save_item(database, item_attributes):
    json_database = open(database, "r")
    updated_dict_database = json.load(json_database)
    item_name = item_attributes.get("user_name")
    response = lookup_item(database, item_name)
    if response == None:
        item_entry = {item_name: item_attributes}
        updated_dict_database.append(item_entry)
        with open(database, "w") as f:
            json.dump(updated_dict_database, f, indent=4)
        print(
            colored(
                "\nitem '{}' has been successful saved into the '{}' database".format(
                    item_name, database
                ),
                "green",
            )
        )
    else:
        print(
            colored(
                "\nERROR save_item(): the item {} already exists in the {} database".format(
                    item_name, database
                ),
                "red",
            )
        )


def delete_item(database, item):
    count = -1
    index = None
    json_database = open(database, "r")
    updated_dict_database = json.load(json_database)
    for entry in updated_dict_database:
        for item_name in entry:
            count += 1
            if item_name == item:
                index = count
                break
        if index != None:
            json_database.close()
            break

    if index != None:
        del updated_dict_database[index]
        with open(database, "w") as f:
            json.dump(updated_dict_database, f, indent=4)
    if index == None:
        print(
            colored(
                "\nERROR delete_item(): item '{}' does not exist in the '{}' database".format(
                    item, database
                ),
                "red",
            )
        )


def suggest_user_name(user_name):
    counter = 1
    while True:
        response = lookup_item("databases/users.json", user_name)
        if response != None:
            user_name = user_name + str(counter)
            counter += 1
            continue
        elif response == None:
            break

    return user_name
