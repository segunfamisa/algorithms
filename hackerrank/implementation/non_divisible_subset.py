'''
    Non divisible subset

    https://www.hackerrank.com/challenges/non-divisible-subset
'''
def Solution():

    n,k = map(int, raw_input().split())
    s = map(int, raw_input().split())
    rem = [0] * k
    for i in range(n):
        rem[s[i] % k] += 1

    count = min(rem[0], 1)
    for i in range(1, k/2 + 1):
        if i != k-i:
            count += max(rem[i], rem[k-i])

    if k % 2 == 0:
        count += 1
    print count

Solution()
