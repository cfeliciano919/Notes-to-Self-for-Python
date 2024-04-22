def fnc(arr):
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1] + 1:
            return arr[i]
    else:
        return None

print(fnc([1,2,3,5,6]))

##def find_first_non_consecutive(arr):
##    if len(arr) <= 1:
##        return None
##    
##    for i in range(1, len(arr)):
##        if arr[i] != arr[i-1] + 1:
##            return arr[i]
##    
##    return None
##
### Test the function
##print(find_first_non_consecutive([-1, 0, 1, 2, 4]))  # Output: 4
##print(find_first_non_consecutive([-3, -2, -1, 0, 1]))  # Output: None
##


##print(len([1,2,3,4,5]))
##print(range(1,len([1,2,3,4,5])))
##print(list(range(1,len([1,2,3,4,5]))))
##
##
##why does print(range(1,len([1,2,3,4,5]))) return a value of 5, but print(list(range(1,len([1,2,3,4,5])))) return a value of 4?
##
#
#
#
#
#
#
#
##    This one was another simple one that had me beyond confused. Though I realized that I should identify the individual numbers, I could not figure what to do next.
##    What I've learned thus far is that I need to find the individual integers, and figure a way to see if they are consecutive or non consecutive. Another way to understand that, is whether 'i = [i-1] + 1' or not.
##    The way you can do this is by applying a for loop to the range of the array, starting from indice 1 rather than 0. This is because the first indice, 0, will mess you up when calculating for i != [i-1] + 1
##
##    That being said, here's the correct code, which is also at the top of the file.
##
##    def func(arr):
##        for i in range(1, len(arr)):
##            if arr[i] != arr[i-1] + 1:
##                return arr[i]
##        else:
##            return None
##
##    You want to make sure that when referring to 'i', you are actually telling the computer to look for the i indice. So let's say that the i indice is 5, and the i-1 indice is 3. The code will find [i], and determine that it is not equal to the sum indice[i - 1] plus 1. Or in this case, it is not equal to 3 (this is the indice directly before 5((i)) hence [i-1]) + 1.
##    So 3 + 1 is not 5, which makes the statement 'arr[i] != arr[i-1] + 1' True.
##    Thus, the loop will return the number that is indice [i], --->arr[i]<---
##    Now if arr[i]'s value was 3, and arr[i-1] was 2, then it would make arr[i] != arr[i-1] + 1 False, and would return None.
