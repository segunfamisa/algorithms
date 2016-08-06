'''
    Compare the triplets

    https://www.hackerrank.com/challenges/compare-the-triplets
'''

def Solution():
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())

    scoreA = 0
    scoreB = 0
    for i in range(len(A)):
        if A[i] > B[i]:
            scoreA += 1
        elif A[i] < B[i]:
            scoreB += 1
    print scoreA, scoreB

Solution()
