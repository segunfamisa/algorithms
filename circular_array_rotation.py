'''
Circular Array Rotation
https://www.hackerrank.com/challenges/circular-array-rotation

'''
def rotate(arr, k):
    l = len(arr)
    out = [0] * l
    tmp = 0
    for i in range(l):
        newI = (i + k) % l
        out[newI] = arr[i]
    return out

def Solution():
    n, k, q = raw_input().split();
    n = int(n)
    k = int(k)
    q = int(q)
    arr = [int(a) for a in raw_input().split()]

    arr = rotate(arr, k)
    for i in range(q):
        query = input()
        print arr[query]

def SolutionImproved():
    n, k, q = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    # for cases where k > n, basically to cycle
    k %= n
    arr = arr[n-k:] + arr[: n-k]
    for i in range(q):
        query = input()
        print arr[query]
# Solution()
SolutionImproved()
