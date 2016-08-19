def enc(plaintext, offset):
    """ Caesar encription """
    ciphertext = ""
    for char in plaintext:
        #replace = chr(ord(char) + offset)
        replace = chr((ord(char) + offset) %128)
        ciphertext = ciphertext + replace
        #ciphertext += replace

    return ciphertext
        

def dec(ciphertext, offset):
    """ Caesar decription when we know the offset """ 
    plaintext = enc(ciphertext, -offset)
    return plaintext

def dec2(ciphertext):
    """ Caesar decription when we DON'T know the offset """ 
    for possible_off in range(1, 128):
        possible_plain = dec(ciphertext, possible_off)
        print(possible_off, possible_plain, "\n")


quote = '_`a\x1bn`g`^onjmo#gno$5\x05\x1b\x1b\x1b\x1bjpo\x1b8\x1bVX\x05\x1b\x1b\x1b\x1bi\x1b8\x1bg`i#gno$\x05\x1b\x1b\x1b\x1bajm\x1bd\x1bdi\x1bm\\ib`#i$5\x05\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1bh\x1b8\x1bhdi#gno$\x05\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1bgno)m`hjq`#h$\x05\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1bjpo\x1b8\x1bjpo\x1b&\x1bVhX\x1b\x1ejpo\x1b&8\x1bVhX\x05\x1b\x1b\x1b\x1bm`opmi\x1bjpo'

def dec3(ciphertext, threshold):
    """ Caesar decription when we DON'T know the offset """ 
    common = ["for ", "print(","def ", "return ", " in ", "):"," = "]
    for possible_off in range(1, 128):
        possible_plain = dec(ciphertext, possible_off)
        cnt = 0
        for word in common:
            cnt = cnt + possible_plain.count(word)
        if cnt > threshold:
            print(possible_off,cnt,'\n', possible_plain, "\n")










