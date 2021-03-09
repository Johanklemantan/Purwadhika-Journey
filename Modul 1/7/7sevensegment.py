# bentuk = {
#     '0': (' _ ', '| |', '|_|'),
#     '1': ('   ', '  |', '  |'),
#     '2': (' _ ', ' _|', '|_ '),
#     '3': (' _ ', ' _|', ' _|'),
#     '4': ('   ', '|_|', '  |'),
#     '5': (' _ ', '|_ ', ' _|'),
#     '6': (' _ ', '|_ ', '|_|'),
#     '7': (' _ ', '  |', '  |'),
#     '8': (' _ ', '|_|', '|_|'),
#     '9': (' _ ', '|_|', ' _|')
# }
# number = (input('Input number :'))
# def seven_segment(x):
#     c = [bentuk[y] for y in str(x)]
#     for i in range(0,3):
#         print("".join(a[i] for a in c))

# seven_segment(number)

bentuk = {
    '0': (' _ ', '| |', '|_|'),
    '1': ('   ', '  |', '  |'),
    '2': (' _ ', ' _|', '|_ '),
    '3': (' _ ', ' _|', ' _|'),
    '4': ('   ', '|_|', '  |'),
    '5': (' _ ', '|_ ', ' _|'),
    '6': (' _ ', '|_ ', '|_|'),
    '7': (' _ ', '  |', '  |'),
    '8': (' _ ', '|_|', '|_|'),
    '9': (' _ ', '|_|', ' _|')
}
number = (input('Input number :'))
tuples_in_list = []
def seven_segment(x):
    for y in str(x):
        tuples_in_list.append(bentuk[y])
    # print(tuples_in_list)
    # c = [bentuk[y] for y in str(x)]

    # for i in range(0,3):
    #     print("".join(a[i] for a in c))

        # print(a[i] for a in c)
    # z=""
    for i in range(0,3):   
        z="" 
        for tuplenya in tuples_in_list:
            # print(i)
            z+=tuplenya[i]
        print(z)
            


seven_segment(number)
# def seven_segment(number):
#     # treat the number as a string, since that makes it easier to deal with
#     # on a digit-by-digit basis
#     digits = [representations[digit] for digit in str(number)]
#     # now digits is a list of 5-tuples, each representing a digit in the given number
#     # We'll print the first lines of each digit, the second lines of each digit, etc.
#     for i in range(5):
#         print("  ".join(segment[i] for segment in digits))


# c = (1,3,4)
# print(c.append(5))

# for i in rnage(0)