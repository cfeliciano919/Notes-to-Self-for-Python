#def fake_bin(x):
#    print(''.join('1' if int(c)>= 5 else '0' for c in x))

def fake_bin(x):
    print(''.join('0' if int(c) < 5 else '1' for c in x))


fake_bin('12333666787333')

#notes to self
#remind yourself of how to utilize .join
#if you are having an issue with, lets say, finding and replacing every 1 in a long string of numbers, try to instead break it down further.
#break down further when having trouble and reapproach the problem. in this case, I was focusing on how to replace all of the numbers in the string, but viewing the string as a whole rather than many individual parts of a whole.
#view the individual parts of the whole. How can you, lets say, replace one individual part of the whole if it is less than 5?
#well, I can say that for number in numberString, if the number is less than five, return a '0'. otherwise, return a 1.
#to type this out properly, we need to rearrange it a little bit, and we will also have to coerce the strings into integers so that we can apply comparison operators. simple enough, using int(number) within our if statement.
#we need the if/else statements to be on the same side of the for loop -- more specifically, we need them located before the for loop, since they are two individual parts of a whole.
#thus we get        return '0' if int(number) < 5 else '1'      if we left it like this we would get an error, so we need to add the for loop in order to specify 'where number resides(?)'
#now we add the for loop to the end. This tells the computer that it needs to do this command for every number within the string, until there are no more characters left.
# return '0' if int(number) < 5 else '1' for number in numberString     leaving it like this will also not give us the desired output. We need to join everything together to make is cohesive, using, of course, the .join method.
# by assigned all of the code after 'return' to the .join method, we can create one cohesive string. We need to specify that we want to join each individual number with NO space, or in other words, we want the result to be a long string of numbers that are physically touching each other without any spaces in between them.
#thus, we type out      return ''.join('0' if int(number) < 5 else '1' for number in numberString)
