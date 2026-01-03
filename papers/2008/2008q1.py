# BIO 2008 Round 1
# Question 1
# Goldbach Conjecture

import math

num = int(input())
count = 0


def isPrime(n):
    if n < 2:
        prime = False
    else:
        prime = True
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            prime = False
    return prime

for i in range(num-(num//2)+1):
    a = i
    b = num-i

    if (isPrime(a) == True and isPrime(b) == True):
        count += 1


print(count)

# 1b) 3, 43 and 5, 41 and 17, 29 and 23, 23

# 1c) 9
