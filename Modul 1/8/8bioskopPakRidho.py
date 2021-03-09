def tickets(peopleInLine): # [25, 25, 25, 100]
    people_in = [] # [25, 50, 25, 100]
    wallet = {25:0, 50:0, 100:0}
    #        {25:1, 50:0, 100:1}

    for j in peopleInLine: # [25, 50, 25, 100]
        if j == 25:
            wallet[25] += 1
            people_in.append(j)
        elif j == 50 and wallet[25] > 0: 
            wallet[25] -= 1
            wallet[50] += 1
            people_in.append(j)
        elif j == 50 and wallet[25] == 0:
            print('NO')
            break
        elif j == 100 and wallet[50] >= 1 and wallet[25] >= 1:
            wallet[100] += 1
            wallet[50] -= 1
            wallet[25] -= 1
            people_in.append(j)      
        elif j == 100 and wallet[25] >= 3:
            wallet[100] += 1
            wallet[25] -= 3
            people_in.append(j)
        else:
            print('NO')
            break    
        print(wallet)  

    print('Orang yang bisa nonton:', people_in)
    print('Orang yang antri:', peopleInLine)
    if len(people_in) == len(peopleInLine):
        print('YES')

peopleInLine = [25, 50, 50, 100]              
tickets(peopleInLine)