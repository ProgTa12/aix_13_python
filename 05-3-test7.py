with open("basic.txt", "w")as file:
    file.write("Basic 1\nBasic 2")

with open("basic.txt", "r")as file:
    contents = file.read()
print(contents)