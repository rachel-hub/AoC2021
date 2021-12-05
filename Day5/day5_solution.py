# Load modules
import pandas as pd
import scipy as sp
import numpy as np
from scipy.sparse import csr_matrix

# Load data - file delimited with new line
input1 = pd.read_table("input.txt", header=None, names=["input"], sep='\n')
# Split data into columns we actually want
input1[['start', 'end']] = input1['input'].str.split('->', expand=True)
input1[['x1', 'y1']] = input1['start'].str.split(',', expand=True)
input1[['x2', 'y2']] = input1['end'].str.split(',', expand=True)
input1.x1 = pd.to_numeric(input1.x1)
input1.y1 = pd.to_numeric(input1.y1)
input1.x2 = pd.to_numeric(input1.x2)
input1.y2 = pd.to_numeric(input1.y2)

# We only want to work with data where inputs are horizontal
# or vertical lines - so filter our input down
smaller_input1 = input1.loc[(input1.x1 == input1.x2) | (input1.y1 == input1.y2)].copy()

max_matrix_dim = (max([smaller_input1.x1.max(),
                       smaller_input1.y1.max(),
                       smaller_input1.x2.max(),
                       smaller_input1.y2.max()])) + 1  # +1 because of 0 index

# Need to work out how to index the series which comes out of iterrows
# initialise an output matrix
output_matrix = csr_matrix((max_matrix_dim, max_matrix_dim),
                            dtype=np.int8)
for x in smaller_input1.iterrows():
    series_item = x[1]  # First element of the tuple is our data frame row
    # Extract the numbers we care about to avoid repeatedly looking them up
    x1 = series_item['x1']
    x2 = series_item['x2']
    y1 = series_item['y1']
    y2 = series_item['y2']
    if x1 == x2:
        num_vals = abs(y1 - y2) + 1  # Need to include both co-ordinates themselves
        row_indices = [x1] * num_vals  # X co-ordinate repeats for the number of values
        if y1 > y2:
            col_indices = list(range(y2, y1+1))
        else:
            col_indices = list(range(y1, y2+1))
        this_matrix = csr_matrix((np.array([1] * num_vals),
                                  (np.array(row_indices),
                                   np.array(col_indices))),
                                 shape=(max_matrix_dim, max_matrix_dim))

    elif y1 == y2:
        num_vals = abs(x1 - x2) + 1  # Need to include both co-ordinates themselves
        col_indices = [y1] * num_vals  # X co-ordinate repeats for the number of values
        if x1 > x2:
            row_indices = list(range(x2, x1 + 1))
        else:
            row_indices = list(range(x1, x2 + 1))
        this_matrix = csr_matrix((np.array([1] * num_vals),
                                  (np.array(row_indices),
                                   np.array(col_indices))),
                                 shape=(max_matrix_dim, max_matrix_dim))

    output_matrix += this_matrix

# Find how many are larger than two
print((output_matrix.toarray() > 1).sum())

# Part 2 also considers the diagonals
max_matrix_dim = (max([input1.x1.max(),
                       input1.y1.max(),
                       input1.x2.max(),
                       input1.y2.max()])) + 1  # +1 because of 0 index

# Need to work out how to index the series which comes out of iterrows
# initialise an output matrix
output_matrix = csr_matrix((max_matrix_dim, max_matrix_dim),
                            dtype=np.int8)
for x in input1.iterrows():
    series_item = x[1]  # First element of the tuple is our data frame row
    # Extract the numbers we care about to avoid repeatedly looking them up
    x1 = series_item['x1']
    x2 = series_item['x2']
    y1 = series_item['y1']
    y2 = series_item['y2']
    if x1 == x2:
        num_vals = abs(y1 - y2) + 1  # Need to include both co-ordinates themselves
        row_indices = [x1] * num_vals  # X co-ordinate repeats for the number of values
        if y1 > y2:
            col_indices = list(range(y2, y1+1))
        else:
            col_indices = list(range(y1, y2+1))

    elif y1 == y2:
        num_vals = abs(x1 - x2) + 1  # Need to include both co-ordinates themselves
        col_indices = [y1] * num_vals  # X co-ordinate repeats for the number of values
        if x1 > x2:
            row_indices = list(range(x2, x1 + 1))
        else:
            row_indices = list(range(x1, x2 + 1))

    # If neither x1=x2 or y1=y2 then we have a diagonal
    else:
        num_vals = abs(x1 - x2) + 1  # Need to include both co-ordinates themselves
        # The above assumes abs(x1 - x2) = abs(y1 - y2)
        if x1 > x2:
            row_indices = list(range(x2, x1+1))
            row_indices.reverse()
        else:
            row_indices = list(range(x1, x2+1))
        if y1 > y2:
            col_indices = list(range(y2, y1+1))
            col_indices.reverse()
        else:
            col_indices = list(range(y1, y2+1))

    this_matrix = csr_matrix((np.array([1] * num_vals),
                              (np.array(row_indices),
                               np.array(col_indices))),
                             shape=(max_matrix_dim, max_matrix_dim))

    output_matrix += this_matrix

# Find how many are larger than two
print((output_matrix.toarray() > 1).sum())
