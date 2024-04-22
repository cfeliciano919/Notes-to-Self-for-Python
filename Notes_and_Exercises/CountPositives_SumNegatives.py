def count_positives_sum_negatives(arr):
    
        
count_positives_sum_negatives((1,2,3,4,5,6,7,8,-1, -2, -3, -4))



#Isolate the individual number. How do I count that this number is greater than one.
# if number >1: return .count()


#Here is someone else's solution, I struggled to find one on my own.
def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]
#Basically, you begin by stating if not arr: return[]
# This means, if arr does not contain anything, instead of returning an array of [0,0], it will return nothing at all.
#Next you are setting positive and negative variables for the problem.
#
