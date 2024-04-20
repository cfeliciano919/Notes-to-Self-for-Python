#Square Sum
#This exercise is on codewars, called Square(n)Sum
#Complete square sum func so that it squares each num passed into it and then sums the results together.


def square_sum(numbers):        #This func is not going to print anything to the console, but you can replace 'return' with print() and surround the entire line in print's () and it will print the result to the console for you.
    return sum(n**2 for n in numbers)

square_sum([1,2,2])

#notes to self
#Did something similar as the first and last initial kata. 'n**2 for n in numbers' vs 'l[0] for l in name.split()'
#It seems you can set arguments and create a small line of code for a for loop isolated to one line
#n**2 for n in numbers goes one at a time, and grabs each individual number (item in list) and squares it until there are no more numbers present.
#sum is outside of the loop, because you need the sum of the squared numbers(the result of the loop). 
#so to reiterate, you get sum(n**2 for n in numbers), because 'n**2 for n in numbers' is finding the squared versions of all numbers within the 'numbers' list, and then sum is adding all of the results together to get your final answer.
