from parse import parse
from collections import Counter

filename = "data"
file = open(filename, "r")
lines = file.read().splitlines()
lines.sort()

guards = {}

for x in lines:
    if 'Guard' in x:
        currentguard = parse('[1518-{date} {time}] Guard #{id} begins shift', x)
    if 'asleep' in x:
        sleep_time = parse('[1518-{date} 00:{time}] falls asleep', x)
    if 'wakes' in x:
        wake_time = parse('[1518-{date} 00:{time}] wakes up', x)
        timeasleep = int(wake_time['time']) - int(sleep_time['time'])
        if currentguard['id'] not in guards:
            guards[currentguard['id']] = [0]*60
        minutes = list(range(int(sleep_time['time']), int(wake_time['time'])))
        for m in minutes:
            guards[currentguard['id']][m] += 1

max_minute = 0
guardid = 0
minute_index = 0

for g_id in guards:
    if max(guards[g_id]) > max_minute:
        max_minute = max(guards[g_id])
        guardid = g_id
        minute_index = guards[g_id].index(max(guards[g_id]))

print(int(guardid) * int(minute_index))
