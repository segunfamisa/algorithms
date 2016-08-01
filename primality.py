# Enter your code here. Read input from STDIN. Print output to STDOUT
def Solution():
    n = input()
    for i in range(1,n):
        num = input()
        if is_prime(num):
            print "Prime"
        else:
            print "Not prime"

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n%2 == 0) or (n%3 == 0):
        return False
    i = 5
    while i*i < n:
        if n % i == 0:
            return False
        i += 1
    return True

n = input()
print is_prime(n)
