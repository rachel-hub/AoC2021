import networkx as nx

# Test input
input1 = [5, 4, 8, 3, 1, 4, 3, 2, 2, 3,
          2, 7, 4, 5, 8, 5, 4, 7, 1, 1,
          5, 2, 6, 4, 5, 5, 6, 1, 7, 3,
          6, 1, 4, 1, 3, 3, 6, 1, 4, 6,
          6, 3, 5, 7, 3, 8, 5, 4, 7, 8,
          4, 1, 6, 7, 5, 2, 4, 6, 4, 5,
          2, 1, 7, 6, 8, 4, 1, 7, 2, 1,
          6, 8, 8, 2, 8, 8, 1, 1, 3, 4,
          4, 8, 4, 6, 8, 4, 8, 5, 5, 4,
          5, 2, 8, 3, 7, 5, 1, 5, 2, 6]

# Real input
input1 = []
with open("input.txt") as file:
    for x in file.readlines():
        row_num_char = x.split("\n")[0]
        for y in range(len(row_num_char)):
            input1.append(int(row_num_char[y]))

# Set dimension
graph_dim = 10

# Create a graph object to work with
G1 = nx.generators.lattice.grid_2d_graph(graph_dim, graph_dim)

# Add the diagonal edges
G1.add_edges_from([
                      ((x, y), (x+1, y+1))
                      for x in range(graph_dim - 1)
                      for y in range(graph_dim - 1)
                  ] + [
    ((x+1, y), (x, y+1))
    for x in range(graph_dim - 1)
    for y in range(graph_dim - 1)
])

# Get a list of node IDs so these can be keys for attribute dictionaries
G1nodes = list(G1.nodes)

# Convert input1 to a dictionary of attributes
curr_attrs = {G1nodes[x]: input1[x] for x in range(len(input1))}

# Counter of total flashed
total_flashed = 0

# Count the first 100 flashes
for count in range(100):
    print(count)
    # First add 1 to all value
    for nd in G1nodes:
        curr_attrs[nd] += 1

    # Work out which ones should flash
    to_flash = {k: v for (k, v) in curr_attrs.items() if v > 9}
    flashed = {}
    # print(len(to_flash))
    while len(to_flash) > 0:
        for x in to_flash:
            # print("flashing")
            # print(x)
            for n in G1.neighbors(x):
                # print("neighbours")
                # print(n)
                curr_attrs[n] += 1
        flashed.update(to_flash)
        to_flash = {k: v for (k, v) in curr_attrs.items() if v > 9 and k not in flashed}

    # Keep count of how many flashes
    total_flashed += len(flashed)
    # Reset those which have flashed to 0
    curr_attrs.update({k: 0 for (k, v) in flashed.items()})
    print(total_flashed)

# Now find first time all flash simulataneously

# Reset curr_attrs
curr_attrs = {G1nodes[x]: input1[x] for x in range(len(input1))}
# Count the loops
loop_counter = 0
while max(curr_attrs.values()) > 0:
    print([loop_counter, max(curr_attrs.values())])
    # First add 1 to all value
    for nd in G1nodes:
        curr_attrs[nd] += 1

    # Work out which ones should flash
    to_flash = {k: v for (k, v) in curr_attrs.items() if v > 9}
    flashed = {}
    # print(len(to_flash))
    while len(to_flash) > 0:
        for x in to_flash:
            # print("flashing")
            # print(x)
            for n in G1.neighbors(x):
                # print("neighbours")
                # print(n)
                curr_attrs[n] += 1
        flashed.update(to_flash)
        to_flash = {k: v for (k, v) in curr_attrs.items() if v > 9 and k not in flashed}

    # Keep count of how many flashes
    total_flashed += len(flashed)
    # Reset those which have flashed to 0
    curr_attrs.update({k: 0 for (k, v) in flashed.items()})
    loop_counter += 1  # Add to loop counter

print(loop_counter)
