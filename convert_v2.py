import json
for i in range(20):
    user_in = []
    file_name = f"./bin/train_schedule/route{i}.json"

    while (x:=input(">>>")) != '':
        user_in.append(x)
    station, timers = [user_in[::3], user_in[2::3]]

    with open(file_name, "w") as f:
        json.dump([station, timers], f)
    print("File has been saved")