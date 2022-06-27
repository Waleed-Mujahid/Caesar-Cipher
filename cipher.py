def cipherFunc(code, shift, str, places):
    places = int(places)
    if (code == 'decode'):
        if (shift == 'left'):
            shift = 'right'
        else :
            shift = 'left'

    temp = ""
    for i in range(len(str)):
        char = str[i]
        if (str[i].isspace()) :
            temp += ' '
        elif shift == "left":
            if char.isupper() == True:
                temp += chr((ord(char) - 65 - places) % 26 + 65)
            else :
                temp += chr((ord(char) - 97 - places) % 26 + 97)
        else:
            if char.isupper() == True:
                temp += chr((ord(char) - 65 + places) % 26 + 65)
            else :
                temp += chr((ord(char) - 97 + places) % 26 + 97)

    return temp