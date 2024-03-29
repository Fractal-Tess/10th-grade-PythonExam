import os.path
import random
from os import path


def ask_user(message):
    f = input(message)
    if f.lower() == "y":
        return True
    elif f.lower() == "n":
        return False
    else:
        print("Please enter a valid input.")
        return ask_user(message)


def generate_ticket_index():
    random_number = str(random.randrange(100000000, 999999999))
    original_dir = os.getcwd()
    os.chdir(str(os.getcwd()) + "/bin")

    if not os.path.exists("Ticket_Data_Base"):
        os.mkdir("Ticket_Data_Base")

    os.chdir(str(os.getcwd()) + "/Ticket_Data_Base")

    if path.exists("Ticket_ID_" + random_number + ".txt"):
        return generate_ticket_index()
    else:
        f = open("Ticket_ID_" + random_number + ".txt", "w+")
        f.writelines("ID = " + random_number + "\n")
        os.chdir(original_dir)
        return f
