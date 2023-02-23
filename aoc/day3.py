# always subtracting 1 less because counting starts at 1
def get_priority(c):
    if c >= 'A' and c <= 'Z':
        return ord(c) - 38
    return ord(c) - 96

# refnum prevents the need for unique appearances
def string_to_map(s, sfreq, refnum = 0):
    for c in s:
        if c not in sfreq:
            sfreq[c] = 0

        if sfreq[c] == refnum:
            sfreq[c] += 1

f = open("inputs/day3.txt", "r")
lines = f.readlines()
f.close()

s = 0
sfreq = {}

# Part one
for line in lines:
    first_sack = line[:int(len(line)/2)]
    second_sack = line[int(len(line)/2):]

    string_to_map(first_sack, sfreq)

    for c in second_sack:
        if c not in sfreq:
            sfreq[c] = 0

        if sfreq[c] == 1:
            s += get_priority(c)
            break
    
    sfreq.clear()

print("Part one: %d" % s)

s = 0

# Part two
# Read line in groups of 3
for i in range(0, len(lines), 3):
    for j in range(0, 2):
        string_to_map(lines[i + j], sfreq, j)
    
    line = lines[i + 2]
    for c in line:
        if c not in sfreq:
            sfreq[c] = 0

        if sfreq[c] == 2:
            s += get_priority(c)
            break

    sfreq.clear()

print("Part two: %d" % s)