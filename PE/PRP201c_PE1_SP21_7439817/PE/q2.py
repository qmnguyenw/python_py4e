fname = "mbox-short.txt"

fh = open(fname.strip())
count = 0

time_arr = []
hour_arr = []
hour_dict = dict()

for line in fh:
    if line.startswith('From '):
        # print(line.rstrip())
        time = line.rstrip().split()[5]
        # print(time)
        time_arr.append(time)
        hour = time.rstrip().split(':')[0]
        hour_arr.append(hour)
        hour_dict[hour] = hour_dict.get(hour, 0) + 1
        second = time.rstrip().split(':')[2]
        count += 1

# print('---\n')
# print('Time array:', time_arr, '\n')
# print('Hour array:', hour_arr, '\n')
# print("Time exists in file", count, "cases\n")
# print('The counts of hours in these time', len(hour_arr), '\n')
# print('The frequently of hour', hour_dict, '\n')
# print('Sort time array by hour', sorted(time_arr), '\n')
# print('Sort hour array by hour', sorted(hour_arr), '\n')
print(hour_dict)
print('-------')
print(dict(sorted(hour_dict.items(), key=lambda item: item[1])))
