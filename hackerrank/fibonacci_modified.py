# https://www.hackerrank.com/challenges/fibonacci-modified
# 0 1 5
def fib_mod(t1, t2, n):
    if n == 0:
        return t1
    elif n == 1:
        return t2
    else:
        i = 2
        s = [0] * n
        s[0] = t1
        s[1] = t2
        tn = 0
        while i < n:
            tn = s[i-2] + (s[i-1] ** 2)
            s[i] = tn
            i += 1

        return tn

def Solution():
    inp = raw_input().split()
    t1 = int(inp[0])
    t2 = int(inp[1])
    n = int(inp[2])

    print fib_mod(t1, t2, n)


Solution()
