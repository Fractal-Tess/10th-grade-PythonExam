user_input = []
while (x:=input()) != '':
    user_input.append(x)
# user_input = [user_input[i:i+3] for i in range(0, len(user_input), 3)]
l = ['МЕЗДРА', '↦', '17:05', 'МОРАВИЦА', '17:10', '17:10', 'РУСКА БЯЛА', '17:13', '17:14', 'ВРАЦА', '17:22', '17:24']
stations, timers = zip(*[[l[i], l[i+2]] for i in range(0, len(l),3)])
print(stations)
print(timers)
