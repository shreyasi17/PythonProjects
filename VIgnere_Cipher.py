try:
    import pyperclip # pyperclip copies text to the clipboard.Vigenère Cipher 387
except ImportError:
    pass # If pyperclip is not installed, do nothing. It's no big deal.

# Every possible symbol that can be encrypted/decrypted:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():

    # Let the user specify if they are encrypting or decrypting:
    while True: # Keep asking until the user enters e or d.
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    # Let the user specify the key to use:
    while True: # Keep asking until the user enters a valid key.
        print('Please specify the key to use. \n It can be a word or any combination of letters:')
        response = input('> ').upper()
        if response.isalpha():
            myKey = response
            break

    # Let the user specify the message to encrypt/decrypt:
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # Perform the encryption/decryption:
    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage, myKey)

    print('%sed message:' % (myMode.title()))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass # Do nothing if pyperclip wasn't installed.

def encryptMessage(message, key):
    return translateMessage(message, key, 'encrypt')

def decryptMessage(message, key):
    return translateMessage(message, key, 'decrypt')

def translateMessage(message, key, mode):
    translated = [] # Stores the encrypted/decrypted message string.

    keyIndex = 0
    key = key.upper()

    for symbol in message: # Loop through each character in message.
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not in LETTERS.
            if mode == 'encrypt':
                # Add if encrypting:
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                # Subtract if decrypting:
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS) # Handle the potential wrap-around.

            # Add the encrypted/decrypted symbol to translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # Move to the next letter in the key.
            if keyIndex == len(key):
                keyIndex = 0
            else:
                # Just add the symbol without encrypting/decrypting:
                translated.append(symbol)

    return ''.join(translated)

# If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()
