seven_segment_dict = {
#           0         1       2         3       4       5         6         7       8        9
    0 : [[' _ '], ['   '], [' _ '], [' _ '], ['   '], [' _ '], [' _ '], [' _ '], [' _ '], [' _ ']],
    1 : [['| |'], ['  |'], [' _|'], [' _|'], ['|_|'], ['|_ '], ['|_ '], ['  |'], ['|_|'], ['|_|']],
    2 : [['|_|'], ['  |'], ['|_ '], [' _|'], ['  |'], [' _|'], ['|_|'], ['  |'], ['|_|'], [' _|']]
}
nums = input('Input number: ')
#   0
for i in range(3): #[0,1,2]
    #   2
    for num in nums: #[1, 2]
        print(seven_segment_dict[i][int(num)][0], end=' ')
        #     _
        #  |  _|
        #  | |_
    print()