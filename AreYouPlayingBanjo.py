def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

#notes to self
#pay attention to the parenthesis () when using methods. If you were to type "if name[0].lower == 'r'" then you would get an error, however if you remember the () after method .lower, it will function properly.
#also, remember to look back to streamline/trim down on code when possible / necessary. for example, instead of adding a whole new element to the return statement for the space ' ', you can just include it at the beginning of the ' does not play banjo' like so
#note:
    #return will not print the result to the console. try printing.

#This is another problem from codewars that goes by the same name as this file name
