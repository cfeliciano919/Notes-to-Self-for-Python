def hero(bullets, dragons):
    return (True if (int(bullets)) >= (int(dragons)*2) else False)
#This was my initial solution to the following problem on codewars.

#A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?
#Return true if yes, false otherwise :)

#There is a better, more eficient way to do this that I found in another user's solution, but first I'll dissect mine.

#This is a pretty simple problem. Basically, in order to kill ONE dragon, he needs TWO bullets.
#In other words, the amount of bullets should always equal the amount of dragons multiplied by two.
# bullets = dragons*2
#however, there is the possibility that maybe the user enters an amount larger than 2*dragons for the bullets.
# That means that we really want bullets >= dragons*2
#Now that we've established that, lets move on to the coding.
#So, we want to code something that determines if the integer amount of bullets equals or is larger than the int amount of dragons times 2, and returns True if yes, and False if no.
#We can do this with another single-line if statement.
# return True if (int(bullets) >= int(dragons)*2) else False
# This can be understood as, 'return True if the amount of bullets is greater than or equal to the amount of dragons times 2. Otherwise, return False.'
# It is not necessary to coerce the bullets or dragons into integers, but the reasoning behind my decision to do so is because if someone were to enter the number of bullets or dragons as a string with '2','5', for example, the program would still be able to understand the input.
# In retrospect, this decision seems like it might be redundant when working on a complex project, because my thoughts are that, at that point, whoever is working on the code probably knows not to enter a string for a number value. However, people make mistakes I suppose, though I think in the future i will omit the coercion unless if absolutely necessary.

#Here is a more efficient way of programming the same function.

def hero(bullets, dragons):
    return bullets >= dragons * 2

#Though at first I didn't understand how this code could have the same function, it made sense to me after reading the discussion attached to it.
#This is pretty clever, because instead of having redundancy in typing out the true false if else statements, this code takes advantage of the comparison operators' own properties.
#Comparison operators will return boolean values, meaning either True or False values, all by themselves.
#Thus, you can take
#   def hero(bullets, dragons):
#       return bullets >= dragons * 2
# and, since it is a part of the hero function, it will return either True or False by replacing the bullets and dragons parameters with whatever is entered when the function is called.
# This completely removes the need for extra code like 'True if ... else False'
# To reiterate, this is because the comparison operator itself (referring to >= in this case) actually already GIVES you a true false response when provided two values.
# Really, once you can grasp the concept, it's pretty straightforward and simple.
# It's good to remember this, because it can save a lot of time when coding while also keeping your code readable/pleasant to look at.
# Especially when getting into complex projects, I am sure that this can be very handy knowledge to keep in mind. Keep it simple.
hero(10,5)
