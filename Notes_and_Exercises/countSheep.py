def count_sheeps(sheep):
    if not sheep: return []
    c = 0
    for e in sheep:
        if e == True:
            c = c + 1
    return c

print(count_sheeps([True,True,True,True,False,True]))


def sheeps(sheep):
    return count.sheep(True)
    

print(sheeps([True,True,True,True,False,True]))


# There's often times more than one way to solve a problem.
# Instead of jumping straight to loops, think if theres a command or method that already does what you want by itself in some regard
#
# Example, here we want to return the number of True values in array sheep.
#
# We could start a loop and say "If e in sheep == True, then add +1 to a new variable that will store the amount of Trues"
# However, it would be much simpler to just call .count(True) on the array.
#
# Once again, step back and think to yourself.
# I need to find the amount of x something in y. Does anything already do that for me?
#
# 'Does anything already do that for me?' step back and ask yourself this every time.
