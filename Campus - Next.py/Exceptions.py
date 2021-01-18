# def open_file(file_name):
#     try:
#         file = open(file_name,'r')
#     except IOError:
#         print(f"No such file with name {file_name}")
#     else:
#         print(file.read())
#         file.close()
#     finally:
#         print("Finished block")
#
# open_file('names1.txt')

# ---------------------------------------------------------------------

# class UnderAgeException(Exception):
#
#     def __init__(self, name, age):
#         self.argsName = name
#         self.argsAge = age
#
#     def __str__(self):
#         return f"You under age 18, {18 - self.argsAge} more year you can invite"
#
# def send_invitation(name, age):
#     try:
#         if int(age) < 18:
#             raise UnderAgeException(name, age)
#         else:
#             print("You should send an invite to " + name)
#     except Exception as e:
#         print(e)
#
# send_invitation('liad', 17)

# ----------------------------------------------------------------------

def checkInput(userName, password):
    exceptions = []

    # UserName too short
    if len(userName) < 3:
        exceptions.append(UsernameTooShort(userName))

    # UserName too long
    if len(userName) > 16:
        exceptions.append(UsernameTooLong(userName))

    # UserName illegal chars
    if any(not c.isalpha() and not c.isdigit() and not c == '_' for c in userName):
        exceptions.append(UsernameContainsIllegalCharacter(userName))

    # Password too short
    if len(password) < 8:
        exceptions.append(PasswordTooShort(password))

    # Password too long
    if len(password) > 40:
        exceptions.append(PasswordTooLong(password))

    # Password illegal char
    if any(not c.isupper() and not c.islower() and not c.isdigit() and not c.punctuation() and not c.isalpha() for c in password):
        exceptions.append(PasswordMissingCharacter(password))

    if len(exceptions) > 1:
        [print(e) for e in exceptions]

    else:
        print("OK")


class UsernameContainsIllegalCharacter(Exception):

    def __init__(self, args):
        self.args = args

    def __str__(self):
        return f"User name you entered conatin illegal char."

class UsernameTooShort(Exception):

    def __init__(self, args):
        self.args = args

    def __str__(self):
        return "The user name too short, must conatins at least 3 chars."

class UsernameTooLong(Exception):

    def __init__(self, args):
        self.args = args

    def __str__(self):
        return "The user name too long, must contains under then 16 chars."

class PasswordTooShort(Exception):

    def __init__(self, args):
        self.args = args

    def __str__(self):
        return "The password too short, must contains as least 8 chars."

class PasswordTooLong(Exception):

    def __init__(self, args):
        self.args = args

    def __str__(self):
        return "The password too long, must contains under 40 chars."

class PasswordMissingCharacter(Exception):

    def __init__(self, args):
        self.args = args

    def __str__(self):
        return "The password missing must char."


# checkInput("1", "2")
# checkInput("0123456789ABCDEFG", "2")
# checkInput("A_a1.", "12345678")
# checkInput("A_1", "2")
# checkInput("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
# checkInput("A_1.)", "abcdefghijklmnop")
# checkInput("A_1", "ABCDEFGHIJLKMNOP")
# checkInput("A_1", "ABCDEFGhijklmnop")
# checkInput("A_1", "4BCD3F6h1jk1mn0p")
# checkInput("A_1", "4BCD3F6.1jk1mn0p")

a = 'A_ae$$%&.,'

print(any(c.isupper() for c in a))
print(any(c.isdigit() for c in a))
print(any(c == '_' for c in a))

if not any((c.isupper() or c.isdigit() or c == '_') for c in a):
    print("Exception")
else:
    print("OK")

if not any(c.isupper() for c in a) or not any(c.isdigit() for c in a) or not any(c == '_' for c in a):
    print("Exception")
else:
    print("OK")