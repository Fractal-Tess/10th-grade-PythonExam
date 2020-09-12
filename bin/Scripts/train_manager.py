import os, functions, sys, classes


original_dir = os.getcwd()
train_list = []


def check_train_data_base():
    os.chdir(original_dir + "/bin")
    if not os.path.exists("Trains_Data_base"):
        print("Train_Data_Base' Directory couldn't be found!")
        if functions.ask_for_yes_and_no("Should the program rebuild directory :y/n :"):
            os.mkdir("Trains_Data_base")
                #TODO: add generator functionality
                #generator()
        else:
            print("System terminating")
            sys.exit(0)

    os.chdir(original_dir + "/bin/Trains_Data_Base")
    print("Found " + str(len(os.listdir(os.getcwd()))) + " train configuration file(s).")
    os.chdir(original_dir)
    return None


def generator():
    pass


def load_trains():
    os.chdir(original_dir + "/bin/Trains_Data_Base")
    for n in range(0, len(os.listdir(os.getcwd()))):
        with open(os.listdir(os.getcwd())[n], "r") as f:
            global train_list
            try:
                train_list.append(classes.Train(*map(str.strip, f.readlines()[:9])))
            except TypeError:
                print("Train configuration file '" + os.listdir(os.getcwd())[n] + "' is corrupted.")
        os.chdir(original_dir)
    os.chdir(original_dir)
