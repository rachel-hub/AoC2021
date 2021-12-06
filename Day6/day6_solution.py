# Example input
# input1 = [3, 4, 3, 1, 2]

# Real input
with open("input.txt") as file:
    input1 = [x.split(',') for x in file.readlines()]
# Now sort out to numeric type
input1 = [int(x) for x in input1[0]]

# Count up the items and put into a dictionary
num0s = input1.count(0)
num1s = input1.count(1)
num2s = input1.count(2)
num3s = input1.count(3)
num4s = input1.count(4)
num5s = input1.count(5)
num6s = input1.count(6)
num7s = input1.count(7)
num8s = input1.count(8)

fish_dict = {
    0: num0s,
    1: num1s,
    2: num2s,
    3: num3s,
    4: num4s,
    5: num5s,
    6: num6s,
    7: num7s,
    8: num8s
}

fish_dict2 = fish_dict.copy()  # Get ready for part 2 with the same input

# 80 days for part 1
for x in range(80):
    print(x)
    num0s = fish_dict[0]
    new_fish_dict = {
        0: fish_dict[1],
        1: fish_dict[2],
        2: fish_dict[3],
        3: fish_dict[4],
        4: fish_dict[5],
        5: fish_dict[6],
        6: fish_dict[7] + num0s,
        7: fish_dict[8],
        8: num0s
    }
    fish_dict = new_fish_dict.copy()

print(sum(fish_dict.values()))

# Part 2 is the same but 256 days
# Need to re-initialise the dictionary
for x in range(256):
    print(x)
    num0s = fish_dict2[0]
    new_fish_dict = {
        0: fish_dict2[1],
        1: fish_dict2[2],
        2: fish_dict2[3],
        3: fish_dict2[4],
        4: fish_dict2[5],
        5: fish_dict2[6],
        6: fish_dict2[7] + num0s,
        7: fish_dict2[8],
        8: num0s
    }
    fish_dict2 = new_fish_dict.copy()

print(sum(fish_dict2.values()))
