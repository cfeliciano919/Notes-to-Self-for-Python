##def abbrev_name(name):
##    first_initial = name[0]
##    for letter in range(len(name)):
##        if name[letter] == " ":
##            last_initial = name[letter + 1]
##
##    return (first_initial.upper() + "." + last_initial.upper())
##print(abbrev_name('Cameron Feliciano'))






##def abbrev_name(name):
##    first_initial = name[0]
##    for letter in range(len(name)):
##        if name[letter] == " ":
##            last_initial = name[letter+1]
##    return (first_initial.upper() + "." + last_initial.upper())
##print(abbrev_name('Jefferey Smith'))



def abbrev_name(name):
    return '.'.join(l[0] for l in name.split()).upper()
    
    #notes to self on how this code works, NOT reading from left to right.
    #first, you should isolate the first and last names as individual items in a list. this is done by splitting the input 'name' with name.split(), which also removes the spaces at the same time.
    #we now have a list that looks something like ['Sam', 'Harris']
    #the 'next' step is to isolate the first letter in both the first and last names(Sam and Harris respectively).
    #to do this you can create a for loop that picks out the first indice of each item in the list. The loop allows you to pick the first indice out of ALL items in the list, not just the first item.
    #^^this is done by first identifying the first indice using a temporary variable of your choice. for me, I chose 'l' for 'letter'. 
    #^^^ (l[0] for l in name.split())    EXPLANATION BELOW
    #^^^^ l[0] picks the first indice, and  'for l in name.split()'  sets up the loop so that you can pick the first indice from each item.
    #Now we have both first intitials, but they have not been joined together with a period(.) yet, nor have they been capitalized. Instead, their current state looks something like ['S', 'H']
    #This is where we wrap up the code outside of (l[0] for l in name.split())
    #^ We can start at the left side of the code, by joining the two (or however many) initials with a period.
    #^^ '.'.join is added at the start.
    #^^^ '.'.join(l[0] for l in name.split())
    #^^^^ This code now gives us something like "S.H" as its output. However, the code is still not finished. If the code is left like this and one of the names happens to be, for example, "patrick feenan", then you will end up with "p.f" as your result.
    # We need to ensure that even a name entered entirely in lowecase letters will be capitalized when the code runs.
    # Do this by adding the .upper() method at the end of the code, outside of the parenthesis. Final code with the return command will look like this...
    # return '.'.join(l[0] for l in name.split()).upper()
    
    
    # Maybe try logical thinking if can't figure out the correct code immediately. Figure out some steps that you would have to take to achieve your result if there were no code involved.
    # Example, this Kata. "Convert a name into initials. The result should have the first and last initials, capitalized, and separated by a single period."
    # Well, first we need to identify the first and last names. Next we need to separate them from each other. After that, we should find the first letters in the first and last name. Next, we should be joining the first and last initials with a period. Finally, we should make sure that these initials are always capitalized.
    # Once you figure out what you need to do, you can try to follow these steps within the actual coding process. How can I find the first and last names? How can I separate them? Etc.
    # It will still likely be confusing for a while, but 'reverse engineering', if you will, can help make sense of what it is that's going on rather than just seeing a bunch of nonsensical(at the moment) letters, numbers, and symbols
