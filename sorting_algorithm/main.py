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
        if is_first_word_better(left_list[i], right_list[j]):
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
    result.extend(left_list[i:])
    result.extend(right_list[j:])
    return result
        


def is_first_word_better(first_word, second_word):
    first_incr = second_incr = 0
    while first_incr < len(first_word) and second_incr < len(second_word):
        if letter_values[first_word[first_incr]] > letter_values[second_word[second_incr]]:
            return False
        elif letter_values[first_word[first_incr]] < letter_values[second_word[second_incr]]:
            return True
    if len(first_word) > len(second_word):
        return False
    else:
        return True

if __name__=="__main__":
    MAX_MEMORY = 10
    counter = 1
    word_list = []
    with open("input.txt", "r") as file:
        for i in range(MAX_MEMORY):
            word_list.append(file.readline())
    
    sorted_words = merge_sort(word_list)
    for word in sorted_words:
        print(word)
