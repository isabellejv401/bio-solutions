# BIO 2009 Round 1
# Question 3
# Child's Play

# BIO 2009 Round 1
# Question 3
# Child's Play

# dynamic programming

s = input().split(' ')

n = int(s[1])
s = int(s[0])

def count_ways(s, n):

    # counts ways of making a number and memoises
    dp = [0]*(s+s)
    dp[0] = 1
    
    for i in range(1, s+1):
        for x in range(1, 10):
            if i - x >= 0:
                dp[i] += dp[i-x]

    

    remaining = s
    result = []

    while remaining > 0:
        # d is the digit you're finding
        for d in range(1, 10):
            if d > remaining:
                break

            count = dp[remaining-d]
            if n > count:
                n -= count

            else:
                remaining -= d
                result.append(d)
                break

    return(result)

print(*count_ways(s, n))
                
