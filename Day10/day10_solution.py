# Module
import statistics

# test input
# input1 = ["[({(<(())[]>[[{[]{<()<>>",
#           "[(()[<>])]({[<{<<[]>>(",
#           "{([(<{}[<>[]}>{[]{[(<()>",
#           "(((({<>}<{<{<>}{[]{[]{}",
#           "[[<[([]))<([[{}[[()]]]",
#           "[{[{({}]{}}([{[{{{}}([]",
#           "{<[[]]>}<{[{[{[]{()[[[]",
#           "[<(<(<(<{}))><([]([]()",
#           "<{([([[(<>()){}]>(<<{{",
#           "<{([{{}}[<[[[<>{}]]]>[]]"]

# Real input
input1 = []
with open("input.txt") as file:
    for x in file.readlines():
        input1.append(x.split("\n")[0])  # Read in input line by line, stripping newline character off end

# Record what data we're allowed
valid_openings = ["(", "[", "{", "<"]
valid_endings = [")", "]", "}", ">"]
valid_parings = {"(": ")",
                 "[": "]",
                 "{": "}",
                 "<": ">"}

# Part 1
output_scores = {")": 3,
                 "]": 57,
                 "}": 1197,
                 ">": 25137}

ans_dict = {")": 0,
            "]": 0,
            "}": 0,
            ">": 0}

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


# Part 2
scores = []

output_scores2 = {")": 1,
                  "]": 2,
                  "}": 3,
                  ">": 4}

for x in input1:
    temp = []
    string_len = len(x)
    for y in range(string_len):
        my_char = x[y]
        if my_char in valid_openings:
            temp.append(x[y])
        elif my_char in valid_endings:
            most_recent = temp[-1]
            # print([most_recent, my_char])
            if valid_parings[most_recent] != my_char:
                break  # Move onto next item in outer loop
            temp.pop()  # Remove last element
        if y == string_len - 1 and len(temp) != 0:  # If we get here the string is incomplete
            print(temp)
            score = 0
            for item in reversed(temp):
                print(item)
                item_pair = valid_parings[item]
                score *= 5
                score += output_scores2[item_pair]
            print(score)
            scores.append(score)

print(scores)

# Want the middle one which is the median
ans2 = statistics.median(scores)
print(ans2)
