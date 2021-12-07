# Module
import statistics

# Test input
# input1 = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

# Real input
with open("input.txt") as file:
    input1 = [x.split(',') for x in file.readlines()]
# Now sort out to numeric type
input1 = [int(x) for x in input1[0]]

# Best position to get them to should be tha median
best_pos = statistics.median(input1)
print(best_pos)

# Work out the fuel to get there
fuel = sum([abs(x - best_pos) for x in input1])
print(fuel)

# Part 2 is with non-constant fuel use
# Best position here will likely be near the mean
best_pos2 = sum(input1) / len(input1)
print(best_pos2)
best_pos2 = round(best_pos2)
print(best_pos2)

# Work out the fuel
fuel2 = sum([sum(range(int(abs(x - best_pos2) + 1))) for x in input1])
print(fuel2)

# Now look at neighbours to this to check what's best
for x in range(-10, 11):
    new_central_pos = best_pos2 + x
    new_fuel = sum([sum(range(int(abs(x - new_central_pos) + 1))) for x in input1])
    if new_fuel < fuel2:
        answer_fuel = new_fuel
        answer_pos = new_central_pos

print([answer_pos, answer_fuel])
