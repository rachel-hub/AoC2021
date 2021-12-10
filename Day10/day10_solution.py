# test input
input1 = ["[({(<(())[]>[[{[]{<()<>>",
          "[(()[<>])]({[<{<<[]>>(",
          "{([(<{}[<>[]}>{[]{[(<()>",
          "(((({<>}<{<{<>}{[]{[]{}",
          "[[<[([]))<([[{}[[()]]]",
          "[{[{({}]{}}([{[{{{}}([]",
          "{<[[]]>}<{[{[{[]{()[[[]",
          "[<(<(<(<{}))><([]([]()",
          "<{([([[(<>()){}]>(<<{{",
          "<{([{{}}[<[[[<>{}]]]>[]]"]

# Real input
input1 = []
with open("input.txt") as file:
    for x in file.readlines():
        input1.append(x.split("\n")[0])  # Read in input line by line, stripping newline character off end

ans_dict = {")": 0,
            "]": 0,
            "}": 0,
            ">": 0}

valid_openings = ["(", "[", "{", "<"]
valid_endings = [")", "]", "}", ">"]
valid_parings = {"(": ")",
                 "[": "]",
                 "{": "}",
                 "<": ">"}
output_scores = {")": 3,
                 "]": 57,
                 "}": 1197,
                 ">": 25137}

for x in input1:
    temp = []
    for y in range(len(x)):
        my_char = x[y]
        if my_char in valid_openings:
            temp.append(x[y])
        elif my_char in valid_endings:
            most_recent = temp[-1]
            print([most_recent, my_char])
            if valid_parings[most_recent] == my_char:
                print("Valid")
            else:
                print("Not valid")
                ans_dict[my_char] += 1
                break  # Move onto next item in outer loop
            temp.pop()  # Remove last element
    print(ans_dict)

ans1 = 0
for ending in valid_endings:
    ans1 += ans_dict[ending] * output_scores[ending]

print(ans1)


#     x0 = x[0]
#     xn = x[-1]
#     print([x0, xn, ord(x0), ord(xn)])
#     if x0 == "(":
#         if xn != ")" and xn in valid_endings:
#             ans_dict[xn] += 1
#     else:
#         if ord(x0) + 2 != ord(xn) and xn in valid_endings: # Use that other brackets are two different in ASCII
#             ans_dict[xn] += 1
#
# print(ans_dict)

