with open('inputs/day3.txt') as f:
    lines = f.readlines()
    s = 0
    chars = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    # Part 1
    for line in lines:
      l = line.rstrip()
      # Split l in half
      first_sack, second_sack = l[:len(l)//2], l[len(l)//2:]
      # Find the character that appears in both strings
      for c in first_sack:
        if c in second_sack:
          s += chars.index(c) + 1
          break
    print(s)

    # Part 2
    s = 0
    # Read file in groups of three lines
    for i in range(0, len(lines), 3):
      # Check for a common character in all three lines
      for c in lines[i]:
        if c in lines[i+1] and c in lines[i+2]:
          s += chars.index(c) + 1
          break
    print(s)