# first get all lines from file
with open('cow.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()

# replace spaces with Unicode+2800  (fake braile space)
lines = [line.replace(' ', '\u2800') for line in lines]

# finally, write lines in the file
with open('cow2.txt', 'w', encoding="utf-8") as f:
    f.writelines(lines)