import functools

def add(x,y):
    return x+y

def sum_of_digits(number):
    return functools.reduce(add, list(map(int, str(number))))

print(sum_of_digits(104))
# print(list(map(int, str(104))))


def sum_string_lengh():
    with open('names.txt', 'r') as names:
        names = names.read().splitlines()

    return functools.reduce(lambda x,y: x+y, list(map(len, names)))

print(sum_string_lengh())