# BIO 2010 Round 1
# Anagram Numbers ALTERED FOR QUESTION 1C

digits = []
count = 0
anagram = False

for k in range(100000, 1000000):
    anagram = False
    num = k

    for i in range(2, 10):
        if sorted(str(num)) == sorted(str(num*i)):
            anagram = True

    if (anagram == True) and (len(list(str(num))) == len(list(set(str(num))))):
        count += 1


print(count)
