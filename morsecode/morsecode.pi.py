
MORSE_CODE_DICT = {'A':'*---', 'B':'---***','C':'---*---*','D':'---**',
            'E':' *','F':'**---*', 'G':'------*', 'H':'****', 'I':'**', 'J':'*---------', 'K':'---*---', 'L':'*---**',
            'M':'------', 'N':'---*', 'O':'---------','P':'*------*','Q':'------*---','R':'*---*','S':'***','T':'---',
            'U':'**---','V':'***---','W':'*------','X':'---**---','Y':'---*------','Z':'------**','1':'*------------',
            '2':'**---------','3':'***------','4':'****---','5':'*****','6':'---****','7':'------***','8':'---------**','9':'------------*','0':'---------------' }


def encrypt(message):
    cipher = ' '
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            print("cipher in progress:  ", cipher)
    return cipher


def decrypt(message):
    message += ' '
    # i = 0
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                dict_idx = list(MORSE_CODE_DICT.values()).index(citext)
                decipher += list(MORSE_CODE_DICT.keys())[dict_idx]
                citext = ''
                dict_idx = ''
    return decipher


cleartextmessage = input("Please enter the text you want to encrypt: ")

secretmessage = encrypt(cleartextmessage.upper())
print(secretmessage)

decryptmessage = decrypt(secretmessage)
print(decryptmessage)








