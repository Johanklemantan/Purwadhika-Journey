import random
kata = ['Nama Kota di Indonesia','Salah Satu Ibu Kota Negara','Judul Film','Tempat Tinggal Spongebob']
jawaban = 'bandung ottawa avengers nanas'.split()

def play(jawaban_random, kata_random): #ottawa
    word_completion = '_ '*len(jawaban_random)
    guessed = False
    guessed_letters = []
    tries = 0
    attempt = 1
    print('****HANGMAN****')
    print(f'{len(jawaban_random)} huruf! {kata_random}')
    print(word_completion)
    print('\n')

    while not guessed and tries < 6:
            
            guess = input(f'Attempts {attempt} : ').lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters and guess in jawaban_random:
                    attempt +=1
                elif guess in guessed_letters and guess not in jawaban_random:
                    attempt +=1
                    tries +=1
                elif guess not in jawaban_random:
                    tries += 1
                    guessed_letters.append(guess)
                    attempt +=1
                else:
                    guessed_letters.append(guess)
                    word_as_list = word_completion.split(" ")
                    indices = [i for i, letter in enumerate(jawaban_random) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = " ".join(word_as_list)
                    attempt +=1
                    if "_" not in word_completion:
                        guessed = True
                        attempt +=1

            elif len(guess) >1  and guess.isalpha():
                print("Enter only 1 character")
                attempt += 1
            else:
                print("Not a valid guess.")
                attempt +=1
            print('\n')
            print(word_completion)
            print(tahapan(tries))
           
    if guessed == True:
        print("YOU ARE SAFE")
    else:
        return


def tahapan(tries):
    tahapan = [
'''
''',
'''
____
''',
'''
____
|  |
''',
'''
____
|  |
|  O
''',
'''
____
|  |
|  O
| /|\\
''',
'''
____
|  |
|  O
| /|\\
| / \\
''',
'''
____ 
|  |
|  O
| /|\\
| / \\
|____
YOU ARE DEAD
    '''    
]
    return tahapan[tries]
def main_lagi():
    w = input("Play Again? (Y/N) ").upper()
    if  w == "Y":
        soal=random.randint(0,3)
        jawaban_random = jawaban[soal]
        kata_random = kata[soal]
        play(jawaban_random, kata_random)
        return main_lagi()
    elif w == "N":
        return
    else:
        print('Invalid Input')
        return main_lagi()
def start():
    soal=random.randint(0,3)
    jawaban_random = jawaban[soal] #ottawa
    kata_random = kata[soal] #ibukota
    play(jawaban_random, kata_random)
    main_lagi()
        
start()

