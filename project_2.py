import string
password = input("input password: ")
num = string.digits
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
character = string.punctuation
def check(x):
    has_num = False
    has_upper = False
    has_lower = False
    has_char = False
    for i in range(len(x)):
        i = x[i]
        if i in num:
            has_num = True
        elif i in uppercase:
            has_upper = True
        elif i in lowercase:
            has_lower = True
        elif i in character:
            has_char = True
    if  has_num == True and has_upper == True and has_lower == True and has_char == True:
        return True
    else :
        return False

if len(password) > 7 and check(password):
    print("valid")
else :
    print("not valid")