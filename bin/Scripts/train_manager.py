try:
    import os
    import sys
    import classes
    from os import path

except Exception as e1:
    print("Some modules are missing:[{}]".format(e1))

original_dir = os.getcwd()

train_file_location = os.getcwd() + "/bin/Trains_Data_base"
train_file_name = "trains.json"

train_object_list = []
list_of_all_stations = []


def check_train_data_base():
    try:
        os.chdir(train_file_location)
    except Exception as e2:
        print("Pathfinding error: {}".format(e2))
        sys.exit(0)
    if not path.exists(train_file_name):
        print("{} at directory'{}' could not be found.".format(train_file_name, train_file_location))
        sys.exit(0)

def generator():
    pass  # TODO : add train generator method()


def load_trains():
    global train_object_list

    with open("trains.json", "r") as f:
        pass


