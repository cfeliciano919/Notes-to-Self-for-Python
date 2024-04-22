## This is another kata from codewars, 8 kyu, titled Flick Switch.
## The problem states that you should create a function that acts as a toggle switch, returning True for each element in an array until coming across the element 'flick', which at that point should return False until once again detecting the word 'flick', in which case would once again return the opposite (True)
## I had a hard time understanding and could not complete it on my own at first.
## I found other user's solutions but didn't quite understand them, so I looked to ChatGPT to help supplement my understanding of the code.
## From there, I was able to figure out how the code works.



def flick_switch(lst):
    if not lst: return []   #This is ensuring that nothing will be returned if lst is empty
    result = []     ##Here I assign an empty array to the variable 'result'. This will be where my bools will be stored so that I can return an array of values.
    switch = True   #Now I have created the actual 'light switch' itself. It must start in the on position for this problem so that it will automatically default to returning True until the conditions that I will later set are met.
    for word in lst:
        if word == 'flick':
            switch = not switch     #At this point I am creating the act of flipping the switch. The switch needs to flip to return False, and so this code is written.
        result.append(switch)       #Now I am taking the value returned for each element and adding it to the 'result' array.
    return result                   #Finally, I am returning the result, which will be the full array of bools.
    


print(flick_switch(['greens','beans','flick','potatoes', 'flick', 'tomatoes']))
