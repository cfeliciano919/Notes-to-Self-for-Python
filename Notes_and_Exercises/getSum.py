def get_sum(a,b):
    if a < b:
        return sum(range(a,b+1))
    else:
        return sum(list(range(a,b-1,-1)))


    
print(get_sum(5,3))
print(list(range(5,2)))


def get_Sum(a,b):
    if a > b:
        return sum(list(range(a,b-1,-1)))
    else:
        return sum(range(a,b+1))

print(get_Sum(1,3))
print(get_Sum(3,1))


def Sum(a,b):
    return sum(list(range(a,b-1,-1))) if a > b else sum(range(a,b+1))

print(Sum(2,4))
print(Sum(4,2))


# Overcomplicated code by forcing a to be the start and b to be the stop
# Could have done code like this instead, avoiding redundancy...
#
#
#
#
# Example 1
#
##def sum(a,b):
##    if a > b:
##        return sum(range(b, a + 1))
##    else:
##        return sum(range(a, b + 1))
#
#
#
#
# Example 2, ternary
#
##def sum(a,b):
##    return sum(range(a, b+1)) if a < b else sum(range(b, a + 1))
