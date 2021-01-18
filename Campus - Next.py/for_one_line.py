
# Coins
def combine_coins(coin, numbers):
    return [str(x) + coin for x in numbers]

print(combine_coins('$', range(5)))
#---------------------------------------------------------------------------

# Check duplicates
def intersection(list_1, list_2):
    return [x for x in list_1 if x in list_2]

print(intersection([1,2], [1,3,4,2]))
#---------------------------------------------------------------------------

# Prime number
def is_prime(number):
    return not bool([x for x in range(1, number -1) if number % x == 0 and x != 1])

print(is_prime(42))
print(is_prime(43))
#---------------------------------------------------------------------------

# Check string if have char that not 'a' or 'h'
def is_funny(string):
    return not bool([x for x in string if x != 'a' and x != 'h'])

print(is_funny('hahahahahhahaaaahhhaaahhah'))
print(is_funny('hahahahahhahaaaahhhaaahhahb'))
#---------------------------------------------------------------------------

# Move chars + plus by ascii
password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

def decrypt(password):
    return ''.join([chr(ord(x) + 2) for x in password if x.isalpha()])

print(decrypt(password))
#---------------------------------------------------------------------------

def longest_string():
    with open('names.txt', 'r') as names:
        names = names.read().splitlines()

    return sorted(names, key=len, reverse=True)[0]

print(longest_string())

#---------------------------------------------------------------------------

def shorter_word():
    with open('names.txt', 'r') as names:
        names = names.read().splitlines()

    return [x for x in names if len(x) == len(sorted(names, key=len)[0])]

print(shorter_word())