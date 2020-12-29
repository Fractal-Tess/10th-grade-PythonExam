try:
    import os
    import sys
    import classes
    from os import path
    import json
except Exception as err:
    print(f"Some modules are missing:[{err}]")
    sys.exit(0)

train_load = {}
def load_trains():
    print(os.getcwd())
    with open("trains.json") as jf:
        data = json.load(jf)

        print(data)
load_trains()