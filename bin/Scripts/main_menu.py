import sys

from ticket import new_ticket


def m_menu():
    user_input = input("_" * 35 + "\n" +
                       """For: New ticket :TYPE 'N'
                       For: Ticket check :TYPE 'C'
                       For: Train Graphic :TYPE 'T'
                       For: Day statistics :TYPE 'D'
                       For: Quit application :Type 'Q'
                       Input :""").lower()

    if user_input == "n":
        new_ticket()
    elif user_input == "c":
        pass
        # TODO: read ticket files and check for authenticity
    elif user_input == "t":
        # TODO:Depending on time, print all trains && their current position
        pass
    elif user_input == "d":
        # TODO:Read all tickets purchased for X day and print some statistics
        pass
    elif user_input == "q":
        sys.exit(0)
    else:
        print("Please enter a valid input!")
        m_menu()
