import io
import re

'''
We are going to create two sets, and check if one is a subset (fully contained) in the other.
The smart approach is to pick the set which has a smaller range to check for subset
Idea comes from math: if A is a subset of B, then A is fully contained in B
'''

is_subset = lambda a, b: a.issubset(b) or b.issubset(a)

def main():
    with open("adventofcode.com_2022_day_4_input.txt") as f:
        ranges = f.readlines()
        count = 0
        count2 = 0
        for rng in ranges:
            # remove ","
            rng = re.split(",", rng)
            # remove "\n"
            rng[-1] = rng[-1].strip()
            # convert to four ints
            rng = re.split("-", rng[0]) + re.split("-", rng[1])
            # convert to ints
            rng = [int(i) for i in rng]
            # convert to sets
            pairs = [set(range(rng[0], rng[1]+1)), set(range(rng[2], rng[3]+1))]
            # check if one is a subset of the other
            rng = is_subset(pairs[0], pairs[1])
            if rng:
                count += 1

            if len(pairs[0].intersection(pairs[1])) > 0:
                count2 += 1
        print(count)
        print(count2)

main()