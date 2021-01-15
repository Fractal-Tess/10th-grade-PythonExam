# import json
#
# for i in range(24, 30):
#     user_in = []
#     file_name = f"./bin/train_schedule/route{i}.json"
#     print(">>>")
#     while (x := input()) != '':
#         user_in.append(x)
#     station, timers = [user_in[::3], user_in[2::3]]
#     timers[-1] = user_in[-2]
#     print(timers)
#
#     with open(file_name, "w") as f:
#         json.dump([station, timers], f)
#     print("File has been saved")
# import json
# import os
# count = 0
# li = list()
# for file in os.listdir("bin/train_schedule"):
#     print(file)
#     if count == 5:
#         break
#     count+=1
#
#
#     with open(f"bin/train_schedule/{file}", "r") as f:
#         li.append(json.load(f))
#
# s = set(li)
from collections import Counter
import json
import os
all_routes = list()
for file in os.listdir("bin/train_schedule/"):
    with open(f"bin/train_schedule/{file}", "r") as f:
        all_routes.append(json.load(f)[0])
count = Counter([tuple(x) for x in all_routes])
print(count)
count.
# with open("bin/train_schedule/route1.json") as f:
#     original = ['ВИДИН', 'ВИДБОЛ', 'ЖЕГЛИЦА', 'СРАЦИМИР', 'ДИМОВО', 'БЕЛЩИЦА', 'ОРЕШЕЦ', 'ВОДНЯНЦИ', 'ДРЕНОВЕЦ', 'ДЪБОВА МАХАЛА', 'БРУСАРЦИ', 'МЕДКОВЕЦ', 'ДОЛНО ЦЕРОВЕНЕ', 'ГАБРОВНИЦА', 'МЪРЧЕВО', 'БОЙЧИНОВЦИ', 'РАКЕВО', 'КРИВОДОЛ', 'БЕЛИ ИЗВОР', 'ВРАЦА', 'МЕЗДРА ЮГ', 'ЗВЕРИНО', 'ЛАКАТНИК', 'СВОГЕ', 'СОФИЯ СЕВЕР', 'СОФИЯ']
#     li = json.load(f)[0]
#     tup = tuple(li)
#
#
# for file
