def is_palindrome_recursive(word, low_index, high_index):
    if word is None or word == "":
        return False
    elif high_index <= low_index:
        return True
    else:
        low_letter = word[low_index]
        high_letter = word[high_index]
        index_status = low_letter == high_letter
        if not index_status:
            return False
        else:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)


is_palindrome_recursive("GG", 0, 1)
