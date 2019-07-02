fn = '2019-06-30-easyplan-day24.md'

file = open(fn, 'r')

lines = file.readlines()

starts = []
ends = []

for line in lines:
    arr = line.split(' ')
    if 'Start:' in arr:
        time_str = arr[1]
        starts.append(time_str)
    if 'End:' in arr:
        time_end = arr[1]
        ends.append(time_end)

print(starts)
print(ends)

file.close()