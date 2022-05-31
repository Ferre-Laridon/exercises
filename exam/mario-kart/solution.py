with open("input.txt") as f:
    # copy file to new file
    lines = f.readlines()
    with open("tijdelijk.txt", "w") as t:
        for line in lines:
            t.write(line)

# put first 100 elements of input.txt in dictionary with scores starting at 100 to 1 as values
with open("input.txt", "r") as f:
    scores = {}
    for i in range(100):
        scores[f.readline().strip()] = 100 - i

# do this for 99 extra rounds
for i in range(99):
    # delete first 100 lines
    for k in range(100):
        with open("tijdelijk.txt", "r") as f:
            lines = f.readlines()

        with open("tijdelijk.txt", "w") as f:
            for number, line in enumerate(lines):
                if number not in [0]:
                    f.write(line)

    # read next 100 lines of input.txt and add the scores from 100 to 1 to the dictionary and so on
    with open("tijdelijk.txt", "r") as f:
        for j in range(100):
            name = f.readline().strip()
            scores[name] += (100-j)

# convert the dictionary to a list and sort them descending based on score
scores_list = list(scores.items())
sorted_by_score = sorted(scores_list, key=lambda score: score[1], reverse=True)

# write the name of the first 10 players to output.txt
with open("output.txt", "w") as f:
    for i in range(10):
        f.write(str(sorted_by_score[i][0]) + "\n")