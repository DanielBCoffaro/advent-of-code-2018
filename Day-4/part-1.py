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
            guards[currentguard['id']] = 0
        guards[currentguard['id']] += timeasleep

sleepiestguard = max(guards, key=guards.get)
minutesasleep = []

for i, x in enumerate(lines):
    if 'Guard' in x:
        currentguard = guard_line = parse('[1518-{date} {time}] Guard #{id} begins shift', x)
    if 'asleep' in x and currentguard['id'] == sleepiestguard:
        sleep_time = parse('[1518-{date} 00:{time}] falls asleep', x)
    if 'wakes' in x and currentguard['id'] == sleepiestguard:
        wake_time = parse('[1518-{date} 00:{time}] wakes up', x)
        timeasleep = int(wake_time['time']) - int(sleep_time['time'])
        if currentguard['id'] not in guards:
            guards[currentguard['id']] = 0
        minutesasleep = minutesasleep + list(range(int(sleep_time['time']), int(wake_time['time'])))

minutecount = Counter(minutesasleep).most_common(1)
print(int(sleepiestguard) *  minutecount[0][0])
