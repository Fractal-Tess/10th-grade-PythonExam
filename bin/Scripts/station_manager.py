import os, functions, sys


original_dir = os.getcwd()
station_list = []


def check_for_station_data_base():

    os.chdir(os.getcwd() + "/bin")
    if not os.path.exists("Stations_Data_Base"):
        print("Stations_Data_Base' Directory couldn't be found!")
        if functions.ask_for_yes_and_no("Should the program rebuild directory :y/n :"):
            os.mkdir("Stations_Data_Base")
        else:
            print("System terminating")
            sys.exit(0)
    os.chdir(original_dir + "/bin" + "/Stations_Data_Base")
    if not os.path.exists("stations.txt"):
        print("'stations.txt' file couldn't be found!")
        if functions.ask_for_yes_and_no("Should the program rebuild the file? :y/n :"):
            os.mkdir("stations.txt")
            # TODO: add generator functionality
            # generator()
            pass
    os.chdir(original_dir)


def generator():
    pass


def load_stations():
    os.chdir(os.getcwd() + "/bin" + "/Stations_Data_Base")
    with open("stations.txt") as f:
        global station_list
        station_list = [element.strip() for element in f.readlines()]
        print("Found " + str(len(station_list)) + " stations.")
    os.chdir(original_dir)
