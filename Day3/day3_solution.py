# Load modules
import pandas as pd

# Set width of binary input
binary_width = 12

# Load data - file delimited with new line
input1 = pd.read_fwf("input.txt", header=None, widths=[1]*binary_width)

# Part one - need to know the most common digit in each column
# If the average is > 0.5 it will be 1 and if it's less than it'll be 0
averages = input1.mean()
most_common_is_one = averages > 0.5
# Now produce most common digit by multiplying by 1
most_common = most_common_is_one * 1
# Least common digit is then one minus this
least_common = 1 - most_common
# For the output, convert to decimal and multiply
power_of_two = 1
gamma = 0
epsilon = 0
for x in range(binary_width):
    print(x)
    gamma += power_of_two * most_common[binary_width - (x + 1)]
    epsilon += power_of_two * least_common[binary_width - (x + 1)]
    power_of_two *= 2
    print([gamma, epsilon, power_of_two])

# Answer is gamma * epsilon
print(gamma * epsilon)

# Part 2
# Need to filter the data down to get binary ratings
O2_gen_rat = input1.copy()
index = 0
while (len(O2_gen_rat) > 1) & (index < 12):
    print([len(O2_gen_rat), index])
    col_avg = O2_gen_rat[index].mean()
    if col_avg >= 0.5:
        O2_gen_rat = O2_gen_rat.loc[O2_gen_rat[index] == 1].copy()
    else:
        O2_gen_rat = O2_gen_rat.loc[O2_gen_rat[index] == 0].copy()
    index += 1
print(O2_gen_rat)

CO2_scrub_rat = input1.copy()
index = 0
while (len(CO2_scrub_rat) > 1) & (index < 12):
    print([len(CO2_scrub_rat), index])
    col_avg = CO2_scrub_rat[index].mean()
    if col_avg >= 0.5:
        CO2_scrub_rat = CO2_scrub_rat.loc[CO2_scrub_rat[index] == 0].copy()
    else:
        CO2_scrub_rat = CO2_scrub_rat.loc[CO2_scrub_rat[index] == 1].copy()
    index += 1
print(CO2_scrub_rat)

# Now to convert these to decimal and multiply
# Need our one row dataframes to be series for this to work
O2_gen_rat = O2_gen_rat.squeeze()
CO2_scrub_rat = CO2_scrub_rat.squeeze()
power_of_two = 1
O2_dec = 0
CO2_dec = 0
for x in range(binary_width):
    print(x)
    O2_dec += power_of_two * O2_gen_rat[binary_width - (x + 1)]
    CO2_dec += power_of_two * CO2_scrub_rat[binary_width - (x + 1)]
    power_of_two *= 2
    print([O2_dec, CO2_dec, power_of_two])

# The multiply these to give answer
print(O2_dec * CO2_dec)

# test = input1.loc[input1[0] == 1]

input1.head()