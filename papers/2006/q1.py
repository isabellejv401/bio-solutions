# BIO 2006 - Question 1

# 1a) Anagrams (24/24)

s1 = list(input())
s2 = list(input())
anagram = False

if len(s1) == len(s2):
    anagram = True
    for i in range(len(s2)):
        if s2[i] in s1:
            s1.remove(s2[i])
        else:
            anagram = False

    if len(s1) != 0:
        anagram = False

print("Anagrams") if anagram == True else print("Not anagrams")
        

# 1b) 6 (2/2)

# 1c) 21 (0/4) - 'stars and bars' combinatorics problem
