# Sherlock and Squares
# url: https://www.hackerrank.com/challenges/sherlock-and-squares?h_r=next-challenge&h_v=zen
# Sample input:
# 2
# 3 9
# 17 24

# Sample output:
# 2
# 0
from math import floor, sqrt, pow, ceil

def count_square_numbers(lower, upper):
    start = int(ceil(sqrt(lower)))
    end = int(ceil(sqrt(upper)))
    count = 0
    for i in range(start, end+1):
        if i**2 <= upper:
            count += 1
        else :
            break
    return count

test_cases = int(raw_input())
# read lines
for i in range(test_cases):
    # read line and split items
    test_case = raw_input().split()
    lower = long(test_case[0])
    upper = long(test_case[1])
    print(count_square_numbers(lower, upper))
