def sum_of_list(lst, num):
    for n in lst:
        for x in lst:
            if n != x and n + x == num:
                return True
    return False
    
print(sum_of_list([10, 15, 3, 7], 17))
            