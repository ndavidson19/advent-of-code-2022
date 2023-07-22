import io
import re

def main():
    with open("adventofcode.com_2022_day_1_input.txt") as f:
        lines = f.readlines()
        elf_dict = {}
        count = 0
        for line in lines:
            if line != "\n":
                elf_dict[count] = elf_dict.get(count, 0) + int(line.strip())
            else:
                count += 1
        print(sorted(elf_dict.items(), key=lambda x: x[1], reverse=True))


main()
