import sys
import ticket
import classes, train_manager


def m_menu():
    #Todo : reduce print function
    print("_____________________________________________")
    print("For: New ticket :TYPE 'N'")
    print("For: Check existing ticket :TYPE 'C'")
    print("For: Train Graphic :TYPE 'T'")
    print("For: Day statistics :TYPE 'D'")
    print("For: Quit application :Type 'Q'")
    print("____________________________________________")
    user_input = input("Input :")

    if user_input.lower() == "n":
        ticket.new_ticket()
    elif user_input.lower() == "c":
        pass
        #TODO: read ticket files and check for authenticity
    elif user_input.lower() == "t":
        #TODO: function that returns a list/dict with all currect active trains and their origin, destination,
        # current location, destination + route
        pass
    elif user_input.lower() == "d":
        #TODO: ....
        pass
    elif user_input.lower() == "q":
        sys.exit(0)
    else:
        print("Please enter a valid input!")
        m_menu()
