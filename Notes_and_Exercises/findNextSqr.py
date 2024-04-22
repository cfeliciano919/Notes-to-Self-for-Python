def find_next_square(sq):
    if sq**0.5 != int(sq**0.5):      #if sq is not a perfect sq, return -1
        return -1
    else:
        return int((sq**0.5 + 1)**2)        #otherwise, return the square of ((the square root of sq) + 1)^2
    
# samples
print(find_next_square(4))
print(find_next_square(5))
print(find_next_square(121))
print(find_next_square(625))


# remember that int() will round a float down to the nearest whole number. It always rounds down, never up.
# even if you called int(3.9999999) it will still round down to 3, not 4.

#   It is also possible to place sq**0.5 inside of a variable, and then call var.is_integer() on it.
#   This will look at the float value and determine whether it is technically a whole number or not, returning a bool.
#   You could apply this like this ...    if root.is_integer(): return (root+1)**2 



##if (sq**0.5) % 2:
##        return -1:
##    else:
##        return 


5
7
9
11
13
15
17


##x = 4
##sqrt = x**0.5
##nextSq = (sqrt(x)+1)**2
##print(((4**0.5)+1)**2)
