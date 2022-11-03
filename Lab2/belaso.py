"""
For the Belaso Cipher you need:
    encrypt:    plaintext and key => encrypted text
    decrypt:    encrypted text and key => plaintext

You basically take every letter from the plaintext and shift the degree
of that letter with an index.
That index corresponds with the degree of the letter in the keyword.

plaintext:  MICHIGAN TECHNOLOGICAL UNIVERSITY
keyword:    HOUGHTON HOUGHTONHOUGH TONHOUGHTO
encrypted:  TWWNPZOA ASWNUHZBNWWGS NBVCSLYPMM

M => 12 |
        | => 19 => T
H => 7  |

"""


def encrypt(plainText, key):
    encryptedText = ''
    # keep an index to parse the keyword while we also parse the plaintext
    keyIndex = 0
    # parse the plaintext letter by letter
    for letter in plainText:
        # skip spaces and add them to the encrypted text
        if letter == ' ':
            encryptedText += ' '
        else:
            # reset the index when we finish the keyword
            if keyIndex == len(key):
                keyIndex = 0
            currentKeyLetter = ord(key[keyIndex]) - ord("a")
            currentTextLetter = ord(letter) - ord("a")
            # compute the encrypted letter
            encryptedLetter = currentTextLetter + currentKeyLetter
            # if the letter is out of the bound of the alphabet we subtract
            if encryptedLetter > 25:
                encryptedLetter -= 26
            encryptedText += chr(encryptedLetter + ord('a'))
            keyIndex += 1
    return encryptedText

def decrypt(encryptedText, key):
    plainText = ''
    # keep an index to parse the keyword while we also parse the encrypted text
    keyIndex = 0
    # parse the plaintext letter by letter
    for letter in encryptedText:
        # skip spaces and add them to the encrypted text
        if letter == ' ':
            plainText += ' '
        else:
            # reset the index when we finish the keyword
            if keyIndex == len(key):
                keyIndex = 0
            currentKeyLetter = ord(key[keyIndex]) - ord("a")
            currentTextLetter = ord(letter) - ord("a")
            # compute the decrypted letter
            decryptedLetter = currentTextLetter - currentKeyLetter
            # if the letter is out of the bound of the alphabet we add
            if decryptedLetter < 0:
                decryptedLetter += 26
            plainText += chr(decryptedLetter + ord('a'))
            keyIndex += 1
    return plainText

print(encrypt("michigan technological university", "houghton"))
print(decrypt("twwnpzoa aswnuhzbnwwgs nbvcslypmm", "houghton"))
