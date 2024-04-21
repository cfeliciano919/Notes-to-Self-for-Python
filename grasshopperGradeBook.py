# Another kata from codewars
# Problem asked to make a func that can return the value of three grades, as a letter grade.
# The grades are A(100->90) B(89->80) C(79->70) D(69->60) F(60->0)


import statistics
def get_grade(s1, s2, s3):
    if statistics.mean([s1,s2,s3]) >= 90:
        return 'A'
    elif 90 > statistics.mean([s1,s2,s3]) >= 80:
        return 'B'
    elif 80 > statistics.mean([s1,s2,s3]) >= 70:
        return 'C'
    elif 70 > statistics.mean([s1,s2,s3]) >= 60:
        return 'D'
    elif 60 > statistics.mean([s1,s2,s3]):
        return 'F'
    
#The above is my first solution. Attempt to shorten the code is below.

def grade(s1, s2, s3):
    mean = statistics.mean([s1,s2,s3])
    print('A') if mean >= 90 elif 

grade(88, 84, 85)
""" Code above is further complicating something rather than simplifying it, and will remain unfinished for a reminder"""
#Instead of making overly complex code, another user's solution is similar to as follows.

def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3
    if m >= 90:
        return 'A'
    elif 90 > m >= 80:
        return 'B'
    elif 80 > m >= 70:
        return 'C'
    elif 70 > m >= 60:
        return 'D'
    else:
        return "F"

#Here, I created a local variable for the average/mean WITHIN the function as opposed to wasting all of that time and code on importing statistics, and typing out the statistics.mean([]) every time I needed it.
    # By making a local variable, I can save all of that time, space and code. It makes for a much more readable and efficient program.
