def reverse(sentence, reverse_word):
    if type(reverse_word) != str:
        return ("Invalid input")

    if reverse_word not in sentence:
        return ("The word was not found")

    find = sentence.find(reverse_word)
    return sentence[:find] + reverse_word[::-1] + sentence[find + len(reverse_word):]

