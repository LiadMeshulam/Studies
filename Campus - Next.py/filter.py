def divide_by_four(number):
    return number % 4 == 0

def four_dividers(number):
    return list(filter(lambda x: x % 4 == 0, range(1, number)))

print(four_dividers(9))


# def shorter_word():
#     with open('names.txt', 'r') as names:
#         names = names.read().splitlines()
#
#     return list(filter(lambda x : len(x) == len(sorted(names, key=len)[0]), names))
#
# print(shorter_word())