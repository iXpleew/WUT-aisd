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
    'v': 28,
    'w': 29,
    'x': 30,
    'y': 31,
    'z': 32,
    'ź': 33,
    'ż': 34
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


def is_first_word_better(first_word: str, second_word: str) -> bool:
    index = 0
    while index < len(first_word) and index < len(second_word):
        if letter_values[first_word[index]] > letter_values[second_word[index]]:
            return False
        elif letter_values[first_word[index]] < letter_values[second_word[index]]:
            return True
        else:
            index += 1
    if len(first_word) > len(second_word):
        return False
    else:
        return True


def create_file_name(counter: int):
    return f"results/temp{counter}.txt"


def save_sorted_values(file_name: str, sorted_list: list[str]):
    with open(file_name, mode="w") as temp_file:
        for line in sorted_list:
            temp_file.write(f"{line}\n")


def create_new_file(files_list: list[str], words_list: list[str], counter: int):
    sorted_words = merge_sort(words_list)
    file_name = create_file_name(counter)
    files_list.append(file_name)
    save_sorted_values(file_name, sorted_words)


def compare_lists(first_list: list[str], second_list: list[str]):
    new_list = []
    first_pointer = second_pointer = 0
    while first_pointer < len(first_list) and second_pointer < len(second_list):
        if is_first_word_better(first_list[first_pointer], second_list[second_pointer]):
            new_list.append(first_list[first_pointer])
            first_pointer += 1
        else:
            new_list.append(second_list[second_pointer])
            second_pointer += 1
    
    if first_pointer >= len(first_list):
        while second_pointer < len(second_list):
            new_list.append(second_list[second_pointer])
            second_pointer += 1
    
    if second_pointer >= len(second_list):
        while first_pointer < len(first_list):
            new_list.append(first_list[first_pointer])
            first_pointer += 1
    return new_list
        

def compare_files(files: list[str]):
    midway = len(files) // 2
    for i in range(midway):
        with open(files[i], "r") as first_file, open(files[i+midway], "r") as second_file:
            first_list = [line[:-1] for line in first_file.readlines()]
            second_list = [line[:-1] for line in second_file.readlines()]
            output_list = compare_lists(first_list, second_list)
            file_name = create_file_name(i+1)
            save_sorted_values(file_name, output_list)

def main():
    MAX_MEMORY = 10000
    files_list = []
    word_list = []
    counter = 0
    with open("input.txt", "r") as file:
        for line in file:
            word_list.append(line[:-1])
            if len(word_list) == MAX_MEMORY:
                counter += 1
                create_new_file(files_list, word_list, counter)
                word_list.clear()
        if word_list:
            counter += 1
            create_new_file(files_list, word_list, counter)
            word_list.clear()
    compare_files(files_list)


if __name__=="__main__":
    main()

