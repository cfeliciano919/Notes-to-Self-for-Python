##def banjo(name):
##    if name[0].lower() == 'r':
##        print(name + ' plays banjo')
##    else:
##        print(name + ' does not play banjo')
##
##banjo('Robbie')
##banjo('Jessica')
##banjo('Cameron')
##banjo('reggie')
##
##
##def does_banjo(name):
##    print(name +' plays banjo' if name[0].lower() =='r' else name+' does not play banjo')
##
##does_banjo('Cameron')
##does_banjo('Robbie')
##
##smash = ' '.join
##print(smash(['apples', 'bananas', 'and', 'carrots']))


def odd_count(n):
    if n % 2:
        return len(list(range(n-2,0,-2)))
    else:
        return len(list(range(n-1,0,-2)))

print(odd_count(15))

def odd_Count(n):
    odd = len(list(range(n-2,0,-2)))
    even = len(list(range(n-1,0,-2)))
    return odd if n % 2 else even

print(odd_Count(15))

def odd_Count(n):
    return len(list(range(n-2,0,-2))) if n % 2 else len(list(range(n-1,0,-2)))


"""Best most efficient way to type this code..."""

def odd_countt(n):
    return len(range(1,n,2))
print(odd_countt(27))
print(range(1,15,2))
