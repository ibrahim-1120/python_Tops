rows = 5
for i in range(rows):
    spaces = " " * (rows - i - 1)
    if i == 0:
        stars = "*"
    elif i == rows - 1:
        stars = "* " * rows
    else:
        stars = "*" + " " * (2 * i - 1) + "*"
    print(spaces + stars)
