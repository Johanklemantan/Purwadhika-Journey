def calc_sum(array, left, right): # ([14, 27, 31, 54, 38], 0, 5)
    # the sum of zero elements is 0
    if left == right: # 0 == 5 False // 0 == 2 False
        return 0    

    # the sum of one-element sub-array is the element
    if left == right - 1: # 0 == 5-1=4 False // 0 == 2-1 False // 0 == 1-1 True
        return array[left]

    # the index of the middle element to divide the array into two sub-arrays
    middle = (left + right) // 2
    #           (0  +  5) // 2 = 2
    #           (0  +  2) // 2 = 1

    # the sum of elements in the left subarray
    left_sum = calc_sum(array, left, middle)
    #                           array       , left, right
    #          calc_sum([14, 27, 31, 54, 38], 0, 2) = 41
    #          middle = 1
    #          left_sum = calc_sum([14, 27, 31, 54, 38], 0, 1)
    #                     return 14
    #          right_sum = calc_sum([14, 27, 31, 54, 38], 1, 2)
    #                     return 27
    #          return left_sum + right_sum = 41

    # the sum of elements in the right subarray
    right_sum = calc_sum(array, middle, right)
    #           calc_sum([14, 27, 31, 54, 38], 2, 5)
    #           middle = 3 
    #           left_sum = calc_sum([14, 27, 31, 54, 38], 2, 3) = 31
    #                      return 31 
    #           right_sum = calc_sum([14, 27, 31, 54, 38], 3, 5) = 92
    #                       middle = 4
    #                       left_sum = calc_sum([14, 27, 31, 54, 38], 3, 4)
    #                                  return 54
    #                       right_sum = calc_sum([14, 27, 31, 54, 38], 4, 5)
    #                                   return 38
    #                       return 54 + 38 = 92
    #            return 92 + 31 = 123

    # the sum of elements in the array
    return (left_sum + right_sum) # 123 + 41 = 164
    
# single_elem_arr = [55]
# sum1 = calc_sum(single_elem_arr, 0, 1) # 55
# print(sum1)

# two_elems_arr = [14, 36]
# sum2 = calc_sum(two_elems_arr, 0, 2) # 50
# print(sum2)

five_elems_arr = [14, 27, 31, 54, 38] 
sum3 = calc_sum(five_elems_arr, 0, 5) # 164
print(sum3)

hasil = 0
for i in five_elems_arr:
    hasil += i
print(hasil)
