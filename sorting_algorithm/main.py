MAX_MEMORY = 1000
counter = 1
word_list = []


def merge_sort(words: list[str]) -> list[str]:
    return []

with open("input.txt", "r") as file:
    for i in range(MAX_MEMORY):
        word_list.append(file.read())
print(len(word_list))