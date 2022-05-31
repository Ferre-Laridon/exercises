import csv


# put contents from solutions.csv into a list
with open('solutions.csv') as f:
    solutions = list(csv.reader(f))[0]

# put contents from answers.csv into a list
with open('answers.csv', newline='') as f:
    answers = list(csv.reader(f))

# compare students answers to solutions
students = {}
for i in range(len(answers)):
    score = 0
    for j in range(len(solutions)):
        if (solutions[j] == answers[i][j+1]):
            score+=1
    # convert to dictionary
    students[answers[i][0]] = score

# write to file from dictionary
with open('output.txt', 'w') as f:
    for name, score in students.items():
        f.write('%s %s\n' % (name, score))
