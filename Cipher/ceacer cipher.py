import enchant

d = enchant.Dict("en_US")

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWUXYZ"


def encrypt(msg, key):
    counter = 0
    # Makes it so counter is set to zero, dont know what counter is
    num = 0
    # sets num to zero, dont know what it is
    ciphertext = ''
    # Leaves ciphertext blank, dont know what cipher text is
    while counter < len(msg):
        # counts the number of letters in the message and checks if it is less than counter or zero
        symbol = msg[counter]
        # set symbol to msg[counter] dont know what msg[counter] is
        if symbol in LETTERS:

            num = LETTERS.find(symbol)
            # sets num as number of the letter
            num = num + key
            # sets num as num plus key, ????
            if num >= len(LETTERS):
                # if num has more numbers than Letters does
                num = num - len(LETTERS)
                # subtract the number of LETTERS from num
            ciphertext = ciphertext + LETTERS[num]
            # Set cipher text to Cipher text plus
        else:
            ciphertext = ciphertext + symbol
        counter += 1
    return ciphertext


text = input("Enter message to be encrypted: ")

shift = input("Enter shift: ")

cipher = encrypt(text.upper(), int(shift))
print(cipher)


def decrypt(msg):
    possible_solutions = []
    for i in range(26):
        deciphertext = ''
        for symbol in msg:
            num = LETTERS.find(symbol) + i
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            deciphertext += LETTERS[num]
        if d.check(deciphertext):
            possible_solutions.append(deciphertext)
    return possible_solutions


decipher = decrypt(cipher)
print(decipher)
