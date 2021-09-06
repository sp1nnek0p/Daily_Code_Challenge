def lowest_missing_integer(arr):
    testlst = [i for i in range(min(arr), max(arr) + 2)]

    for x in testlst:
        if x not in arr and x > 0:
            return x

# Test to see if the function is working
print(str(lowest_missing_integer([3, 4, -1, 1])) + " - is the lowest missing integer from your list")
print(str(lowest_missing_integer([1, 2, 0])) + " - is the lowest missing integer from your list")
print(str(lowest_missing_integer([-2, -3, 10, 9, 8, 6, 5, 4, 3, 1])) + " - is the lowest missing integer from your list")
print(str(lowest_missing_integer([3, 4, -2])) + " - is the lowest missing integer from your list")
