f = open("inputs/day1.txt", "r")
lines = f.readlines()
f.close()

aux = 0
max_rank = [0, 0, 0]

for line in lines:
    if not len(line.strip()) == 0:
        aux += int(line)
        continue

    # If it's bigger than the first, update the ranks accordingly
    if aux > max_rank[0]:
        max_rank[0] = aux
        max_rank.sort()

    aux = 0

print("The top elf is carrying %d calories." % max_rank[0])
print("The top three elves are carrying %d calories in total." % sum(max_rank))