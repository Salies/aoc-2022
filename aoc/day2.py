f = open("inputs/day2.txt", "r")
lines = f.readlines()
f.close()

# A data strucutre based solution
rule = {
    'A': ['X', 'Y', 'Z'], # rock
    'B': ['Y', 'Z', 'X'], # paper
    'C': ['Z', 'X', 'Y'], # scissors
}

# default points for char, position in rule, bonus points
points = {
    'X': [1, 2, 0],
    'Y': [2, 0, 3],
    'Z': [3, 1, 6],
}

sum_one = 0
sum_two = 0

for line in lines:
    inp, ans = line.split(' ')
    inp = inp.strip()
    ans = ans.strip()
    sum_one += points[ans][0]
    sum_two += points[rule[inp][points[ans][1]]][0] + points[ans][2]

    if ans == rule[inp][0]:
        sum_one += 3
        continue

    if ans == rule[inp][1]:
        sum_one += 6

print("Total score, part one: %d" % sum_one)
print("Total score, part two: %d" % sum_two)