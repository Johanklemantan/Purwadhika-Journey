def encryptor(word):
    abjad = list('abcdefghijklmnopqrstuvwxyz')
    words = word.lower() # ridho
    encrypt = ''
    for c in words: # ridho => r
        if c != ' ':
            #          (8 + 2)%26
            #           10
            index = (abjad.index(c) + 2)%len(abjad) # 19
            encrypt += abjad[index]
        else:
            encrypt += ' '
    return encrypt

# print((8 + 2)%26)
# print(len(list('abcdefghijklmnopqrstuvwxyz')))


message = input('masukkan kata: ')
result_encrypt= encryptor(message)
print(f'Encrypt {message.upper()} to {result_encrypt.upper()}')
