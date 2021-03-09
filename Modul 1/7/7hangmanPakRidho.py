import random

hangman = ['_____\n',
           '|   |\n',
           '|   O\n',
           '|  /|\\ \n',
           '|  / \\ \n',
           '|____'
]
con = True

while con == True:
    i = random.randint(0,2) # 0
    att = 1
    punish = ''
    false_answer = 0
    questions = ['4 huruf! Temannya Zebra', '5 huruf! Tempat tinggal', '4 huruf! Minuman khusus bayi']
    answer = ['kuda', 'rumah', 'susu']
    print(f"\n ****** HANGMAN ****** \n {questions[i]}")
    secret = answer[i]
    blank = ('_ '*len(secret)).split() # ['_', '_', '_', '_', '_']
    # ['_____']

    while att <= 1000:
        ans = input(f'Attempts {att}: ')
        if len(ans) > 1:
            print('Only one character at the time.')
            ans = input(f'Attempts {att}: ')
        if ans in secret: # ans = r /// secret = rumah
            for i in range(0,len(secret)): # [0,1,2,3,4]
                #  secret[4] == 'u'
                if secret[i] == ans: # r u m a h
                    blank[i] = ans #  [r u _ _ _ ]
            print(' '.join(blank))
            print(punish)
            if '_' not in blank:
                print('YOU ARE SAFE!')
                play = input("Do you want to play again? (y/n): ")
                if play == 'n':
                    con = False
                    break
                elif play == 'y':
                    con = True
                    break
            else:
                att += 1
        else:
            false_answer += 1
            if false_answer == 1:
                print(' '.join(blank))
                punish += hangman[false_answer-1]
                print(punish)
                att += 1
            elif false_answer == 2:
                print(' '.join(blank))
                punish += hangman[false_answer-1]
                print(punish)
                att += 1
            elif false_answer == 3:
                print(' '.join(blank))
                punish += hangman[false_answer-1]
                print(punish)
                att += 1
            elif false_answer == 4:
                print(' '.join(blank))
                punish += hangman[false_answer-1]
                print(punish)
                att += 1
            elif false_answer == 5:
                print(' '.join(blank))
                punish += hangman[false_answer-1]
                print(punish)
                att += 1
            elif false_answer == 6:
                print(' '.join(blank))
                punish += hangman[false_answer-1]
                print(punish)
                print('YOU ARE DEAD\n')
                play = input("Do you want to play again? (y/n): ").lower()
                if play == 'n':
                    con = False
                    break
                elif play == 'y':
                    con = True
                    break
                else:
                    con = False
                    break
    # print(blank)




























