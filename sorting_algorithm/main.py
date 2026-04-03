letter_values = {
    'a': 1,
    'ą': 2,
    'b': 3,
    'c': 4,
    'ć': 5,
    'd': 6,
    'e': 7,
    'ę': 8,
    'f': 9,
    'g': 10,
    'h': 11,
    'i': 12,
    'j': 13,
    'k': 14,
    'l': 15,
    'ł': 16,
    'm': 17,
    'n': 18,
    'ń': 19,
    'o': 20,
    'ó': 21,
    'p': 22,
    'r': 23,
    's': 24,
    'ś': 25,
    't': 26,
    'u': 27,
    'w': 28,
    'y': 29,
    'z': 30,
    'ź': 31,
    'ż': 32
}

def merge_sort(words: list[str]) -> list[str]:
    list_size = len(words)
    if list_size <= 1:
        return words
    
    mid = list_size // 2
    left_part = words[:mid]
    right_part = words[mid:]

    sort_left = merge_sort(left_part)
    sort_right = merge_sort(right_part)

    return merge(sort_left, sort_right)


def merge(left_list: list[str], right_list: list[str]):
    result = []
    i = j = 0

    while i < len(left_list) and j < len(right_list):
        if le


if __name__=="__main__":
    MAX_MEMORY = 10000
    counter = 1
    word_list = []
    with open("input.txt", "r") as file:
        for i in range(MAX_MEMORY):
            word_list.append(file.read())
    print(len(word_list))