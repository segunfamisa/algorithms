'''
    Making Polygons

    https://www.hackerrank.com/contests/w22/challenges/polygon-making
'''
def should_cut(sticks):
    n = len(sticks)
    s = sum(sticks)
    for stick in sticks:
        # check if any stick exists that is longer (or as long as)
        # than the sum of the other sticks put together
        if stick == 0 or stick >= s - stick:
            return True
    return False

def Solution(n, a):
    if n == 1:
        # break 2 times to form a triangle
        print 2
    elif n > 1 and n < 3:
        # essentially 2 sticks. Break one stick to get 3 sticks and then form a triangle
        print 1
    elif n >= 3:
        # determine if you need to cut
        if should_cut(a):
            print 1
        else:
            print 0

n = input()
a = map(int, raw_input().split())

Solution(n,a)
