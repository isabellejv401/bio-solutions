# BIO 2002 Round 1
# Question 1
# Lojban

s = input()

new = ''

for i in range(0, len(s), 2):
   if s[i] == 'p': new += '1'
   elif s[i] == 'r': new += '2'
   elif s[i] == 'c': new += '3'
   elif s[i] == 'v': new += '4'
   elif s[i] == 'm': new += '5'
   elif s[i] == 'x': new += '6'
   elif s[i] == 'z': new += '7'
   elif s[i] == 'b': new += '8'
   elif s[i] == 's': new += '9'
   elif s[i] == 'n': new += '0'

print(new)
