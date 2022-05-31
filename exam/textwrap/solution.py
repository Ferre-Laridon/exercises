import textwrap


# parse line from input.txt and split it into object in a list
with open("input.txt", "r") as f:
    line = f.readline()
    wrap_list = textwrap.wrap(line, 40)

# print lines to output
with open("output.txt", "w") as f:
    for line in wrap_list:
        f.write(line + '\n')