# Load modules
import pandas as pd

# Load data - file delimited with new line
input1 = pd.read_table("input.txt", header=None, names=["input"], sep='\n')

# Split input into two columns and make numbers numeric
input1[['direction', 'distance']] = input1['input'].str.split(' ', expand=True)
input1.distance = pd.to_numeric(input1.distance)

# Now process the directions for pat 1
# forward X increases the horizontal position by X units
# down X increases the depth by X units
# up X decreases the depth by X units
forward_distance = input1.loc[input1['direction'] == 'forward'].distance.sum()
down_distance = input1.loc[input1['direction'] == 'down'].distance.sum()
up_distance = input1.loc[input1['direction'] == 'up'].distance.sum()

# Part 1 solution asks for final horizontal position multiplied by final depth
print(forward_distance * (down_distance - up_distance))

# Part 2 has a more complicated regime
# down X increases your aim by X units
# up X decreases your aim by X units
# forward X does two things:
#    It increases your horizontal position by X units
#    It increases your depth by your aim multiplied by X

# Work out how much aim changes by on each turn
input1["change_in_aim"] = (
    (input1.direction == 'up') * -1 * input1.distance +
    (input1.direction == 'down') * input1.distance)

# Aim is a running total so use cumsum to get it
input1["aim"] = input1.change_in_aim.cumsum()

# Think about horizontal position
input1["change_in_horizontal_position"] = (
    (input1.direction == 'forward') * input1.distance)

# And now depth
input1["change_in_depth"] = (
    (input1.direction == 'forward') * input1.distance * input1.aim)

# For part 2 output we want final horizontal position multiplied by final depth
print(input1.change_in_horizontal_position.sum() *
      input1.change_in_depth.sum())
