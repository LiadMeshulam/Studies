def muliple_letter(char):
    return char + char

def double_letter(my_str):
    return ''.join(list(map(muliple_letter, my_str)))

print(double_letter("LIAD"))


def print_word_length():
    with open('names.txt', 'r') as names:
        names = names.read().splitlines()

    return list(map(lambda x: len(x), names))


print(print_word_length())