# BIO 2025 Round 1
# Question 1
# Palindromic Sums

# case 1: n is a palidrome already
# case 2: n is sum of 2 palindromes - check if i and n-i in palindrome set
# case 3: n is sum of 3 palindromes - nested for loop


n = int(input())

palindromes = []

for i in range(1000000):
   if str(i) == str(i)[::-1]:
      palindromes.append(i)

palindromeset = set(palindromes)

if n in palindromes:
   print(n)
   quit()

else:
   found = False
   for i in palindromes:
      if (n-i) in palindromeset:
         found = True
         print(i, n-i)
         quit()

   for i in palindromes:
      for j in palindromes:
         if (n-i-j) in palindromeset:
            print(i, j, n-i-j)
            quit()
