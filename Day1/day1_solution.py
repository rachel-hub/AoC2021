# Import module
import pandas as pd

# Load data - file delimited with new line so treat like a CSV
input1 = pd.read_csv("input.txt", header=None, names=["input"])

# Part 1 - looking at differences and whether or not they're increasing
# Create an offset to allow calculation of differences
input1["offset_input"] = input1.input.shift(1)
# Calculate the differences
input1["increase"] = (input1.input > input1.offset_input)
# Use that TRUE = 1 anf FALSE = 0 to sum
increases = input1.increase.sum()
# Print answer
print(increases)

# Part 2 - looking at differences in the sum of three things
# Add an offset by 2 to help with this
input1["double_offset_input"] = input1.input.shift(2)
# Now calculate the sum of the three offsets
input1["three_sum"] = input1.input + input1.offset_input + input1.double_offset_input
# And offset it so we can calculate differences in three sums
input1["offset_three_sum"] = input1.three_sum.shift(1)
# Now calculate whether three sum is increasing or not
input1["three_sum_increase"] = (input1.three_sum > input1.offset_three_sum)
# Use that TRUE = 1 and FALSE = 0 to sum
increases2 = input1.three_sum_increase.sum()
# Print answer
print(increases2)
