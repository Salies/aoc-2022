# screw python sets
# classic O(n) hash map solution ftw
def all_unique(s):
    hash_map = {}
    for c in s:
        if hash_map.get(c) == True:
            return False
        hash_map[c] = True
    return True

f = open('inputs/day6.txt', 'r')
lines = f.readlines()
f.close()

line = lines.pop(0).strip()

i = 0
# each 4 characters, check if they're all unique
while not all_unique(line[i:i+4]):
    i += 1
print("Part one:", i + 4)

# Part two could be done in the first loop, but I think making another one is
# a more elegant solution
while not all_unique(line[i:i+14]):
    i += 1
print("Part two:", i + 14)

'''
Piroquinha optimized version
this version doesn't make much sense because I'm pretty sure it would result
in more operations than the first one (two accesses and a rewrite, insted of just a 4-byte read)
but I'm leaving it here just for the sake of it
i = 3
while not all_unique(string):
    i += 1
    string = string[1:] + line[i]
'''