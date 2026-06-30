def decode(string_):
    if string_ != str:
        return "Input is not a String"
    
    for i in string_:
        if i.isupper():
            s+=chr(155-ord(i))
        elif i.islower():
            s+=chr(219-ord(i))
        elif i.isascii():
            s+=chr(ord(i))
    return s
decode("Hvv? R'n mlg gszg wifmp, r xzm hgroo gzpv nb xolgsvh luu")

#155
#219
#32 - 48 caracteres especiais
#32+48 = 80

'''
def decode(string_):
    s = ""
    for i in string_:
        if i.isupper():
            s+=chr(155-ord(i))
        elif i.islower():
            s+=chr(219-ord(i))
        elif i.isascii():
            s+=chr(ord(i))
    return s
'''