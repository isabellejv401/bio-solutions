#BIO 2006 Question 3
#Drats

# 3(a)

L = input().split(' ')
s = int(L[0])
d = int(L[1])


dp = [[0]*(s+1) for _ in range (d)]
dp[0][0] = 1 #Define base case because of DP

for i in range(1, d):
    for t in range(s + 1):
        for v in range(1, 21):
            if t - v >= 0:
                dp[i][t] += dp[i-1][t-v]


answer = 0
for x in range(1, 20):
    if s - 2*x >= 0:
        answer += dp[d - 1][s - 2*x]


print(answer)
print(dp)
