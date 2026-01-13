# BIO 2018 Round 1
# Question 1
# Debt Repayment

import math

s = input().split()

interest = int(s[0])
repayment = int(s[1])

debt = 100
total_repaid = 0

def round2(n):
   return ((math.ceil(n*100))/100)
   

while debt > 0:
   interest_amount = round2(debt*(interest/100))
   debt += interest_amount

   percentage_payment = round2(debt*repayment/100)
   payment = max(percentage_payment, 50)

   payment = min(payment, debt)

   debt -= payment
   total_repaid += payment

print(round2(total_repaid))
