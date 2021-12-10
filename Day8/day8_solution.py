import pandas as pd

input1 = pd.read_table("input.txt",
                       header=None,
                       names=["sig1",
                              "sig2",
                              "sig3",
                              "sig4",
                              "sig5",
                              "sig6",
                              "sig7",
                              "sig8",
                              "sig9",
                              "sig10",
                              "sep",
                              "out1",
                              "out2",
                              "out3",
                              "out4"],
                       sep=' ')

input1.drop("sep", axis=1, inplace=True)  # Remove seperator column

# Part 1
# Work out lengths of strings

# Apply map applies to every value
num_lens = input1.applymap(len)

# Want to know about the number of output values where we have
# length two (must be one)
# length four (must be four)
# length three (must be seven)
# length seven (must be eight)


def is_known_number(x):
    if x in [2, 3, 4, 7]:
        return 1
    else:
        return 0


# Count how many answers are in our known values
ans1 = num_lens[["out1", "out2", "out3", "out4"]].applymap(is_known_number).to_numpy().sum()

print(ans1)

# Now do some decoding for part 2

answer_sum = 0
for index, row in input1.iterrows():
    signals = row[["sig1",
                   "sig2",
                   "sig3",
                   "sig4",
                   "sig5",
                   "sig6",
                   "sig7",
                   "sig8",
                   "sig9",
                   "sig10"]]
    # Lengths to help us figure out numbers
    signal_lengths = signals.map(len)

    # Work out character series for easy numbers
    one = signals.loc[signal_lengths == 2][0]
    four = signals.loc[signal_lengths == 4][0]
    seven = signals.loc[signal_lengths == 3][0]
    eight = signals.loc[signal_lengths == 7][0]

    # Turn these into sets for easier comparison
    one_set = set([x for x in one])
    four_set = set([x for x in four])
    seven_set = set([x for x in seven])
    eight_set = set([x for x in eight])

    # Now do three which contains one and has five digits
    possible_threes = signals.loc[signal_lengths == 5]
    possible_threes_sets = possible_threes.map(lambda x: set([y for y in x]))
    mapping = possible_threes_sets.map(lambda x: one_set.issubset(x))
    three = possible_threes.loc[mapping][0]
    three_set = set([x for x in three])

    # Next do nine which contains three and has six digits
    possible_nines = signals.loc[signal_lengths == 6]
    possible_nines_sets = possible_nines.map(lambda x: set([y for y in x]))
    mapping = possible_nines_sets.map(lambda x: three_set.issubset(x))
    nine = possible_nines.loc[mapping][0]
    nine_set = set([x for x in nine])

    # Next do five which is a subset of nine and not three with five digits
    possible_fives = signals.loc[signal_lengths == 5]
    possible_fives_sets = possible_fives.map(lambda x: set([y for y in x]))
    mapping = possible_fives_sets.map(lambda x: x.issubset(nine_set) and not three_set.issubset(x))
    five = possible_fives.loc[mapping][0]
    five_set = set([x for x in five])

    # Now do six which has five as a subset, is not nine with six digits
    possible_sixes = signals.loc[signal_lengths == 6]
    possible_sixes_sets = possible_sixes.map(lambda x: set([y for y in x]))
    mapping = possible_sixes_sets.map(lambda x: five_set.issubset(x) and not nine_set.issubset(x))
    six = possible_sixes.loc[mapping][0]
    six_set = set([x for x in six])

    # zero has six digits and is neither a subset of six or nine
    possible_zeroes = signals.loc[signal_lengths == 6]
    possible_zeroes_sets = possible_zeroes.map(lambda x: set([y for y in x]))
    mapping = possible_zeroes_sets.map(lambda x: not six_set.issubset(x) and not nine_set.issubset(x))
    zero = possible_zeroes.loc[mapping][0]
    zero_set = set([x for x in zero])

    # two has five digits and is neither a subset of three or five
    possible_twos = signals.loc[signal_lengths == 5]
    possible_twos_sets = possible_twos.map(lambda x: set([y for y in x]))
    mapping = possible_twos_sets.map(lambda x: not five_set.issubset(x) and not three_set.issubset(x))
    two = possible_twos.loc[mapping][0]
    two_set = set([x for x in two])

    digit_list = [zero, one, two, three, four, five, six, seven, eight, nine]
    digit_set_list = [zero_set, one_set, two_set, three_set, four_set,
                      five_set, six_set, seven_set, eight_set, nine_set]
    print(digit_list)

    # Now we've decoded work out the answer
    answer = (1000 * digit_set_list.index(set([x for x in row["out1"]]))) + (
            100 * digit_set_list.index(set([x for x in row["out2"]]))) + (
            10 * digit_set_list.index(set([x for x in row["out3"]]))) + (
        digit_set_list.index(set([x for x in row["out4"]])))

    print(answer)
    answer_sum += answer

print(answer_sum)
