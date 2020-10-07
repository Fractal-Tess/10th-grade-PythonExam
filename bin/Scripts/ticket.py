import time, main_menu, functions, classes, train_manager

try_again = "Do you want to try again? y/n :"
breaker = "______________________________"


def new_ticket():

    candidate_trains = []

    # 1 starting station
    print(breaker)
    ticket_starting_station = ss_f()

    # 2 End station
    print(breaker)
    ticket_end_station = es_f(ticket_starting_station)

    # 3 Date
    print(breaker)
    trip_time = date_and_hour()

    print(breaker + "\nChose a train ~ ")
    for train in train_manager.train_object_list:
        if classes.Train.check_route(train, ticket_starting_station, ticket_end_station, trip_time):
            candidate_trains.append(train)

    for index, train in enumerate(candidate_trains):

        if ticket_starting_station == train.starting_station:
            print(breaker + "\n" +
                  train.starting_station + " to " + train.end_station +
                  "\nRoute :" + '>'.join(train.route) +
                  "\nTrain departs from station " + ticket_starting_station +
                  " at: " + str(':'.join(train.departure_time)) +
                  "\nTrain arrives at destination, station " + ticket_end_station +
                  " at: " + ':'.join(str(elem) for elem in classes.Train.arrives_at(train, ticket_end_station)) +
                  "\nTicket price = " + train.ticket_price +
                  "\nTo chose this train, type :" + str(index))
        else:
            print(breaker + "\n" +
                  train.starting_station + " to " + train.end_station +
                  "\nRoute :" + '>'.join(train.route) +
                  "\nTrain arrives at station " + ticket_starting_station +
                  " at: " + ':'.join(str(elem) for elem in classes.Train.arrives_at(train, ticket_starting_station)) +
                  "\nTrain arrives at destination, station " + ticket_end_station +
                  " at: " + ':'.join(str(elem) for elem in classes.Train.arrives_at(train, ticket_end_station)) +
                  "\nTicket price = " + train.ticket_price +
                  "\nTo chose this train, type :" + str(index))

    chosen_train(candidate_trains)

    ammount_of_tickets = ticket_amount()


    #
    # TODO:dd
    # load possible choices
    # check for date and hour
    #
    # check for seats for given trip (ticket_amount)

def chosen_train(candidate_trains):
    user_input = input("Chose a train ~:")
    if user_input.lower().capitalize() == "Main":
        main_menu.m_menu()
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a number \n" + breaker)
        chosen_train(candidate_trains)
    if user_input > len(candidate_trains) or user_input < 0:
        print("Number does not correspond to any train")
        chosen_train(candidate_trains)
    else:
        return candidate_trains[user_input]


def ticket_amount():
    user_input = input("How many tickets? :")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Input was incorrect")
        if functions.ask_user(try_again):
            return ticket_amount()
        else:
            main_menu.m_menu()
    return user_input


def ss_f():
    for station in station_manager.list_of_all_stations:
        print(station)
    user_input = input("Pick a starting station :").lower()
    user_input = user_input.capitalize()
    if user_input in station_manager.list_of_all_stations:
        return user_input
    print("Invalid input")
    if functions.ask_user(try_again):
        return ss_f()
    else:
        main_menu.m_menu()


def es_f(ss):
    for station in station_manager.list_of_all_stations:
        print(station)
    user_input = input("Pick a destination :").lower()
    user_input = user_input.capitalize()
    if user_input == ss:
        print("Starting station and Ending station CANNOT be the same!")
        if functions.ask_user(try_again):
            return es_f(ss)
        else:
            main_menu.m_menu()
    if user_input in station_manager.list_of_all_stations:
        return user_input
    print("Please spell the station correctly!")
    if functions.ask_user(try_again):
        return es_f(ss)
    else:
        main_menu.m_menu()


def date_and_hour():
    trip_time = input("Time of the trip? :")
    if (len(trip_time)) > 5:
        print("Input was incorrect\n Too many characters.")
        if functions.ask_user(try_again):
            print("Input example  Day:Hour\n Input example  07:20")
            return date_and_hour()
        else:
            main_menu.m_menu()

    if ":" not in trip_time:
        print("Please separate the numbers with a ':'")
        if functions.ask_user(try_again):
            return date_and_hour()
        else:
            main_menu.m_menu()
    else:
        trip_time = trip_time.strip().split(":")
        try:
            trip_time = [int(x) for x in trip_time]
        except ValueError:
            print("Input must be 2 numbers separated by a ':'")
            if functions.ask_user(try_again):
                return date_and_hour()
            else:
                main_menu.m_menu()
        return trip_time