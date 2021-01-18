# a = lambda x:1
#
# print(a(3))
# print(a("s"))
# print(a(2))
# print(type(a(3)))
#
# a = lambda x,y:y
#
# print(a(2,5))
# print(a(2,3))



import functools

# Add plus 1 to number
def function(num, item):
    return num + 1

# Get input from user
password = input("Enter Your password (integers only): ")

# Convert input to int
lst = list(map(int, password))

# Sum all input int
magic = functools.reduce(function, lst)

# Check if all int in result from magic divide by 4
result = (lambda x: x % 4 == 0)(magic)

if result:
    print("Correct password!")
else:
    print("Wrong password.")


# 16
# [1,6]
# 2

# 2301
# [2,3,0,1]
# 5

# 444
# [4,4,4]
# 6

# 1234
# [1,2,3,4]
# 4
