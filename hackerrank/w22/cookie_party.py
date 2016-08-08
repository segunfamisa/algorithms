'''
    Week of code 22
    Cookie Party
    https://www.hackerrank.com/contests/w22/challenges/cookie-party
'''
def Solution():
    n,m = map(int, raw_input().split())
    if n > m:
        print n - m
    elif n == m:
        print 0
    else:
        print n - m % n

Solution()
