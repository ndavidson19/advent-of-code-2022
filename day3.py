import os

def convert_to_priority(char):
    '''
    function converts char to unicode and returns priority
    where a has priority 1, b has priority 2, etc.
    and A has priority 27, B has priority 28, etc.
    '''
    if ord(char) >= 97:
        return ord(char) - 96
    else:
        return ord(char) - 64 + 26
    


def main():
    sum = 0
    group = []
    with open("adventofcode.com_2022_day_3_input.txt") as f:
        rucksack = f.readlines()
        for item in rucksack:
            '''
            if item != "\n":
                middle = len(item.strip()) // 2
                left = item.strip()[:middle]
                right = item.strip()[middle:]
                set_left = set(left)
                set_right = set(right)
                common = set_left.intersection(set_right)
                if common_element := common.pop():
                    sum += convert_to_priority(common_element)
            '''
            # Now we want to find the common element between every three lines
            if item != "\n" and len(group) < 3:
                group.append(item.strip())
            elif item != "\n" and len(group) == 3:
                # find common element
                print(group)
                common = set(group[0]).intersection(set(group[1]))
                common = common.intersection(set(group[2]))
                print(common)
                if common_element := common.pop():
                    sum += convert_to_priority(common_element)
                group = []
                group.append(item.strip())

            else:
                print(sum)
                sum = 0

            # do the last group
            if len(group) == 3:
                common = set(group[0]).intersection(set(group[1]))
                common = common.intersection(set(group[2]))
                if common_element := common.pop():
                    sum += convert_to_priority(common_element)
                group = []
                
            print(sum)


        



main()