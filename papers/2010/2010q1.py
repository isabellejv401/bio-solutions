# BIO 2010 Round 1
# Anagram Numbers

num = int(input())

digits = []

for i in range(2, 10):
    if sorted(str(num)) == sorted(str(num*i)):
        digits.append(str(i))

    else:
        pass

if len(digits) == 0:
    print('NO')

else:
    print(' '.join(digits))
