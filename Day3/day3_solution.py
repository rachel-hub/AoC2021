# Load modules
import pandas as pd

# Set width of binary input
binary_width = 12

# Load data - file delimited with new line
input1 = pd.read_fwf("input.txt", header=None, widths=[1] * binary_width)


# Functions


# Define a function to convert two binary digit series to decimals
def convert_to_binary(series1, series2, series_length):
    power_of_two = 1
    series1_decimal = 0
    series2_decimal = 0
    for x in range(binary_width):
        print(x)
        series1_decimal += power_of_two * series1[binary_width - (x + 1)]
        series2_decimal += power_of_two * series2[binary_width - (x + 1)]
        power_of_two *= 2
        print([series1_decimal, series2_decimal, power_of_two])
    return [series1_decimal, series2_decimal]


# Part one - need to know the most common digit in each column
# If the average is > 0.5 it will be 1 and if it's less than it'll be 0
# Make use TRUE * 1 = 1 and FALSE * 1 = 0
averages = input1.mean()
most_common = (averages > 0.5) * 1
# Least common digit is then one minus this
least_common = 1 - most_common
# For the output, convert to decimal and multiply
[gamma, epsilon] = convert_to_binary(most_common, least_common, binary_width)
# Answer is gamma * epsilon
print(gamma * epsilon)

# Part 2
# Need to filter the data down to get binary ratings
O2_gen_rat = input1.copy()
index = 0
while (len(O2_gen_rat) > 1) & (index < binary_width):
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
while (len(CO2_scrub_rat) > 1) & (index < binary_width):
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
[O2_dec, CO2_dec] = convert_to_binary(O2_gen_rat, CO2_scrub_rat, binary_width)
# The multiply these to give answer
print(O2_dec * CO2_dec)
