def is_anagram(first_string, second_string):
    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())

    is_anagram = check_letters(first_string_list, second_string_list)

    quick_sort(first_string_list, 0, len(first_string_list) - 1)
    quick_sort(second_string_list, 0, len(second_string_list) - 1)

    return (
        "".join(first_string_list),
        "".join(second_string_list),
        is_anagram,
    )


def check_letters(first_string_list, second_string_list):
    letters_checked = []
    first_string_length = len(first_string_list)
    second_string_length = len(second_string_list)
    char_amount = (
        first_string_length == second_string_length
        and first_string_length > 0
        and second_string_length > 0
    )
    for letter in first_string_list:
        if letter in second_string_list:
            letters_checked.append(True)
        else:
            letters_checked.append(False)
    return all(letters_checked) and char_amount


def quick_sort(string_list, start, end):
    if start < end:
        p = partition(string_list, start, end)
        quick_sort(string_list, start, p - 1)
        quick_sort(string_list, p + 1, end)


def partition(string_list, start, end):
    pivot = string_list[end]
    delimiter = start - 1

    for index in range(start, end):
        if string_list[index] <= pivot:
            delimiter = delimiter + 1
            string_list[index], string_list[delimiter] = (
                string_list[delimiter],
                string_list[index],
            )

    string_list[delimiter + 1], string_list[end] = (
        string_list[end],
        string_list[delimiter + 1],
    )

    return delimiter + 1


print(is_anagram("aeiou", "aeoiu"))
