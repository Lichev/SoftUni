from collections import deque


def time_in_seconds(times):
    hh, mm, ss = times.split(':')
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


def seconds_to_time(seconds):
    day = seconds // (24 * 3600)
    seconds = seconds % (24 * 3600)
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)


robots = input().split(";")
time = input()
sec = time_in_seconds(time)

dict_robots = {}
available_robots = deque()
product_to_procced = deque()

for i in robots:
    data = i.split("-")
    robot = data[0]
    proccesing_time = int(data[1])

    dict_robots[robot] = {}
    dict_robots[robot]['proc_time'] = proccesing_time
    dict_robots[robot]['time_left'] = proccesing_time

    available_robots.append(robot)

while True:
    command = input()

    if command == 'End':
        break

    product_to_procced.append(command)

while True:
    if not product_to_procced:
        break
    sec += 1

    if available_robots:
        current_rob = available_robots.popleft()
        current_procces = product_to_procced.popleft()
        print(f'{current_rob} - {current_procces} [{seconds_to_time(sec)}]')
    else:
        current = product_to_procced.popleft()
        product_to_procced.append(current)

    for x in dict_robots.keys():
        if x not in available_robots:
            if dict_robots[x]['time_left'] > 1:
                dict_robots[x]['time_left'] -= 1
            else:
                dict_robots[x]['time_left'] = dict_robots[x]['proc_time']
                available_robots.append(x)