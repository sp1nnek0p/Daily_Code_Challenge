def list_product(lst):
    x = 0
    returnlist = list()
    while x < len(lst):
        y = lst.copy()
        y.pop(x)
        result = 1
        for item in y:
            result *= item
        returnlist.append(result)
        x += 1
    return returnlist

print(list_product([1, 2, 3, 4, 5])) 
print(list_product([3, 2, 1]))
