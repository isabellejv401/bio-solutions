# BIO 2023 Round 1
# Question 1
# Zeckendorf Representation


n = int(input())

rep = []

fib = [1, 2]

while fib[-1] < 1000000:
    fib.append(fib[-2] + fib[-1]) #Note: next time just generate up to n


def representation(num, fib):
    if num in fib:
        rep.append(num)
        return 0

    else:
        for i in range(len(fib)):
            if fib[i] > num:
                rep.append(fib[i-1])
                return (num-fib[i-1])

left = representation(n, fib)

while left != 0:
    left = representation(left, fib)



print(*rep)
