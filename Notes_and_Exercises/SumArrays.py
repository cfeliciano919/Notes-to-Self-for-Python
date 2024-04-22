#Another problem I tried on codewars

#Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer.
#If the array does not contain any numbers then you should return 0.

#This one is relatively straightforward, thought I found yet another solution that was much simpler than my own, similar to the 'willHeSurvive' problem.
#First I'll show my own solution.

def sum_array(a):
    return sum(a) if a != '' else 0

#This works perfectly fine, but has redundant code.
#Here I'm returning the sum of all contents of 'a', so long that 'a' is not empty.
#If 'a' IS empty, then I am returning 0.
#Simple enough, though, 90% of the code can simply be removed because it is not required to function properly.

def sum_array(a):
    return sum(a)

#This is all that is needed to reach the solution to this problem.
#If a has any contents, then it will simply return the sum of them all.
#If there aren't any contents, then it will simply return 0, because there is nothing there to begin with.
#Not much to go over, other than making an effort to remember the built-in functionality of basic functions.
#In other words, sum already returns 0 if nothing is present. Just like how comparison operators will automatically provide a boolean value. If you want said values returned, then you must call them with return

#edit reminder
"""REMEMBER. Wherever there is a comparison, there is a boolean."""
