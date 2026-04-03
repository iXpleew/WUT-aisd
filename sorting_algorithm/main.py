MAX_MEMORY = 1000
counter = 1
word_list = []


def merge_sort(words: list[str]) -> list[str]:
    list_size = len(words)
    if list_size <= 1:
        return words
    
    mid = list_size // 2
    left_part = words[:mid]
    right_part = words[mid:]

    sort_left = merge_sort(left_part)
    sort_right = merge_sort(right_part)

    return []

with open("input.txt", "r") as file:
    for i in range(MAX_MEMORY):
        word_list.append(file.read())
print(len(word_list))