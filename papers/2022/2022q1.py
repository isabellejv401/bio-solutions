# Enter your solution below. Use input() 
# and print() for I/O, and do not output
# any prompts, because the grader will not work.

# BIO 2022 Round 1
# Question 1
# Decrypt

cipher = list(input())

def decrypt(cipher):
    cipher = cipher[::-1]

    for i in range(len(cipher)-1):
        left = ord(cipher[i])
        right = ord(cipher[i+1])
            
        new = (left-64)-(right-64)

        if new <= 0:
            new += 26
        if new > 26:
            new -= 26

        new += 64
        cipher[i] = chr(new)

    print(''.join(cipher[::-1]))


decrypt(cipher)
