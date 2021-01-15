import json

with open("../bin/train_schedule/route1.json") as f:
    station, time = json.load(f)
    print(station)
    print(time)
