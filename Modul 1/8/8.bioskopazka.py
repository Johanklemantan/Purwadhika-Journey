# peopleinline
def tickets(bills):
    wallet = 0
    bill25 = 0
    bill50 = 0
    for bill in bills:
        # print(bill)
        change = bill - 25
        if change > wallet:
            sell = 'NO'
            break
        else:
            if bill == 50:
                if bill25 == 0:
                    sell = 'NO'
                    break
                else:
                    bill25 -= 1
                    bill50 += 1
            elif bill == 100:
                if bill25 >= 1 and bill50 >= 1:
                    bill25 -= 1
                    bill50 -= 1
                elif bill25 >= 3:
                    bill25 -= 3
                else:
                    sell = 'NO'
                    break
            elif bill == 25:
                bill25 += 1
            sell = 'YES'
            wallet -= change
        wallet += bill
    #     print(f'bill25: {bill25}')
    #     print(f'bill50: {bill50}')
    # print(f'wallet: {wallet}')
    
    return print(sell)

tickets([100,25,50,50,100])
