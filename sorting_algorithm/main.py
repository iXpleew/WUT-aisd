MAX_MEMORY = 1000
counter = 1
with open("input.txt", "r") as file:
    for i in range(MAX_MEMORY):
        print(file.readline(),end="")