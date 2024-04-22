#   Some notes to myself about the .replace() method.
#   I decided to write this down after finding .replace() as a good alternative to "''.join(x.split())" which was a simple, single line solution to a problem asking for a string of random characters have any spaces between them removed.
#
##    In Python 3, the .replace() method can create a new string by replacing occurrences of a specific substring(or characters) with another substring(or characters) WITIN a GIVEN string.
##    In more basic terms, it makes a whole new string by, literally, replacing whatever is in a string with something entirely new.
##
##    the syntax looks like this
##
##    new_string = old_string.replace(old_substring, new substring, count)
##    where
##    * 'old_string' : the original string where replacements will be made
##    * 'old_substring': the substring to be replaced
##    * 'new_substring': The substring to replace occurences of 'old_substring'.
##    * 'count' (optional): Specifies the max number of replacements to perform. If not provided, ALL OCCURRENCES are REPLACED.
##
##
##    here's an example.
##
##    original_string = "Hello World! Hello, Python!"
##    new_string = original_string.replace("Hello", "Hi")         This replaces instances of 'Hello' with 'Hi'
##    print(new_string) # Output: "Hi, World! Hi Python!"
#
#
##      if we use the optional 'count' parameter, only the first 'count' occurrences of 'old_substring' will be replaced.
##
##      here's an example of THIS^^
##
##      original_string = 'aaaabbbbcc'
##      new_string = original_string.replace("a", "x", 2)
##      print(new_string)     # Output: "xxaabbbbcc"
      
