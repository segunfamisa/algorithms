'''
    Save the prisoner

    https://www.hackerrank.com/challenges/save-the-prisoner
'''

def Solution(N, M, S):
    id = (S - 1) + M % N
    print N if id is 0 else id

count = input()
for test_case in range(count):
    N, M, S = map(int, raw_input().split())
    Solution(N,M,S)
