'''
    Bigger is greater

    https://www.hackerrank.com/challenges/bigger-is-greater
'''
def Solution(words):
    for word in words:
        if word == perm(word):
            print "no answer"
        else:
            print perm(word)

def perm(word):
    p = len(word) - 1
    while p > 0 and word[p - 1] >= word[p]:
        p -= 1
    if p <= 0:
        return word

    q = len(word) - 1
    while word[q] <= word[p - 1]:
        q -= 1

    w = list(word)
    tmp = w[p - 1]
    w[p - 1] = w[q]
    w[q] = tmp
    word = ''.join(w)

    word = word[:p:] + word[len(word):p-1:-1]
    return word

# read input
count = input()
words = [''] * count
for i in range(count):
    words[i] = raw_input()
# invoke solution
Solution(words)
