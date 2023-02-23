f = open("inputs/day4.txt", "r")
lines = f.readlines()
f.close()

count = 0
count_two = 0

for line in lines:
    line = line.strip()
    # fp = first pair, sp = second pair
    fp, sp = [[int(n) for n in pair.split('-')] for pair in line.split(",")]
    
    # if one range contains the other
    if (fp[0] <= sp[0] and sp[1] <= fp[1]) or (sp[0] <= fp[0] and fp[1] <= sp[1]):
        count += 1

    # if ranges overlap
    if (fp[0] <= sp[0] and sp[0] <= fp[1]) or (sp[0] <= fp[0] and fp[0] <= sp[1]):
        count_two += 1

print("Part one: %d" % count)
print("Part two: %d" % count_two)