with open("attending.txt", "r") as f:
    attending = set(line.strip().lower() for line in f)

with open("all.txt", "r") as f:
    with open("absentees.txt", "w") as a:
        lines = f.readlines()
        for line in lines:
            if line.strip().lower() not in attending:
                a.write(line.lower())