def Atbash(string_):
    array = []
    for i in range(len(string_)):
        letras = ord(string_[i])
        array.append(letras)

    new_string_ = ""
    for j in range(len(array)):
        extremes = (max(array) + min(array)) - array[j]
        new_string_+=chr(extremes)

    print(new_string_)

Atbash("zyxwvutsrqponmlkjihgfedcba")
#Você pega a Soma dos extremos e subtrai pelo ultimo
#caractere em letra
#B = y 2
#f = u 6
#a = 97
#z = 122
# 122 - 97 = 25
# 97 + 25 = 122
#122 - 25 = 97
#122+97 = 219
#209 
#elemento[i]  
#84 = T