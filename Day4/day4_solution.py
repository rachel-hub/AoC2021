# Modules
import numpy as np

# Read in the file
with open("input.txt") as file:
    lines = file.readlines()

# Split it up
split_lines = [inp.split('\n')[0] for inp in lines]
double_split_lines = [inp.split() for inp in split_lines]

# Now work it into things which are more like the inputs we want
input1 = []
temp = []
for x in double_split_lines:
    if x:  # This checks that x is not an empty list
        temp.append(x)
    else:  # If we get to an empty list we want to close off our current temp and start a new item
        input1.append(temp)
        temp = []

# First item are our bing calls
bingo_calls = input1[0][0][0]  # Get out of nested arrays to just a string
# Everything else is bingo boards
bingo_boards = input1[1:]

# Now we can work on our data types a bit
# List of numbers for the bingo calls
bingo_calls = [int(inp) for inp in bingo_calls.split(',')]
# Numeric numpy arrays for the bingo boards
bingo_boards = [np.array(board, dtype=int) for board in bingo_boards]

# Part 1
for val in bingo_calls:
    # For each board, what is the largest value in each row or column
    # This is useful because as check off values we replace them with -1
    # When the largest value in a row/column is -1 it is complete
    col_max_vals = [np.amax(board, axis=0) for board in bingo_boards]
    row_max_vals = [np.amax(board, axis=1) for board in bingo_boards]
    # Of the previous, for each board we're interested in the smallest
    # This is because we are looking for the first row/column to "bingo"
    board_smallest_col_max = [np.amin(arr) for arr in col_max_vals]
    board_smallest_row_max = [np.amin(arr) for arr in row_max_vals]
    # Then because we want the first board, find the best across all boards
    smallest_col_max = min(board_smallest_col_max)
    smallest_row_max = min(board_smallest_row_max)
    print([smallest_col_max, smallest_row_max])
    # If these are above 0, none of them are -1 yet, so we need to keep going
    if (smallest_col_max >= 0) & (smallest_row_max >= 0):
        for board in bingo_boards:
            board[board == val] = -1  # Replacing marked off values with -1
    # When we have a board that's complete, work out the total of its remaining elements
    else:
        print([previous_val, val])
        # Find the index of the winning board
        if smallest_col_max < 0:
            winning_board_ind = np.where(np.array(board_smallest_col_max) == -1)[0].item()
            print(winning_board_ind)
        elif smallest_row_max < 0:
            winning_board_ind = np.where(np.array(board_smallest_row_max) == -1)[0].item()
            print(winning_board_ind)
        # Extract the board and total up all the elements which aren't -1
        winning_board = bingo_boards[winning_board_ind]
        print(winning_board)
        remaining_board_total = winning_board[winning_board >= 0].sum()
        print(remaining_board_total)
        break  # We are done if we get here so exit out of the loop
    # Before we loop again record the previous value
    # At the end, this will be the one that solved the winning board
    # and val will increment to the one after it
    previous_val = val

# Part one output
print(previous_val * remaining_board_total)

# For part 2 want to find out which board wins last
for val in bingo_calls:
    # Like in part 1 we are interested in the smallest of the largest values in rows/columns
    col_max_vals = [np.amax(board, axis=0) for board in bingo_boards]
    row_max_vals = [np.amax(board, axis=1) for board in bingo_boards]
    board_smallest_col_max = [np.amin(arr) for arr in col_max_vals]
    board_smallest_row_max = [np.amin(arr) for arr in row_max_vals]
    # This time we want the last board to win
    # A board wins on a complete row or column so put these in one array so we can
    # look holistically at these
    smallest_totals = np.array([board_smallest_col_max,
                                board_smallest_row_max])
    smallest_total = np.amin(smallest_totals, axis=0)
    print(smallest_total)
    # Count how many board are yet to have any complete row columns
    num_still_to_win = sum(smallest_total >= 0)
    # We want to know the state of the last board to win when it wins so loop until they all have
    if num_still_to_win > 0:
        # We also want to know the last one to win so when we have only one to go, record its index
        if num_still_to_win == 1:
            last_winning_board_ind = np.where(smallest_total != -1)[0].item()
            print(last_winning_board_ind)
        for board in bingo_boards:
            board[board == val] = -1  # Replacing marked off values with -1
    # Once we get to the point where all boards have either a winning row/col
    else:
        print([previous_val, val])
        # Look at the last winning board and the total of its non-negative elements
        last_winning_board = bingo_boards[last_winning_board_ind]
        print(last_winning_board)
        remaining_board_total = last_winning_board[last_winning_board >= 0].sum()
        print(remaining_board_total)
        break
    previous_val = val # Again, this will be the one that solves at the end of the loop

# Final score of last board to win
print(previous_val * remaining_board_total)
