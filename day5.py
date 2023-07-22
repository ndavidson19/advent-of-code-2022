# couple ways to think about this

# 1. Use a datastructure such as a stack which uses last in first out (LIFO) to store the data
# this is useful as we are moving crates from one stack to another

# 2. Use a lookup table to store the data, and then use a loop to iterate through the data
# this is useful as we can store the data as a dictionary, and then use a loop to iterate through the data


def main():
    with open("adventofcode.com_2022_day_5_input.txt") as f:
        crates = f.readlines()
        # the first 10 lines are the drawing
        # the rest are the instructions
        drawing = crates[:9]
        crates = crates[10:]

        for line in drawing:
            # need to parse the drawing
            # we can use a list comprehension to do this
            parser = [char for char in line.strip().replace("[", "").replace("]", "")]
            stacks = {i+1: line.replace("[", "").replace("]", "").split() for i, line in enumerate(line.strip().split("\n"))}
            print(stacks)
            #print(parser)
        #for crate in crates:
            #print(crate)
        #print(drawing)


main()