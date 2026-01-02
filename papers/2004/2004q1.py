# BIO 2004 Round 1
# Question 1 - Mayan Calendar

date = input().split(' ')

for i in range(len(date)):
    date[i] = int(date[i])

ndays = 0
year = 2000
month = 1
day = 1

ndays += 20 * 20 * 18 * 20 * (date[0]-13)
ndays += 20 * 18 * 20 * (date[1]-20)
ndays += 18 * 20 * (date[2]-7)
ndays += 20 * (date[3]-16)
ndays += date[4]-3

while ndays >= 31:
    if ndays >= 31:
        month += 1
        ndays -= 31

    if (year%4 == 0):
        if ndays >= 29:
            month += 1
            ndays -= 29

    else:
        if ndays >= 28:
            month += 1
            ndays -= 28

    if ndays >= 31:
        month += 1
        ndays -= 31

    if ndays >= 30:
        month += 1
        ndays -= 30

    if ndays >= 31:
        month += 1
        ndays -= 31

    if ndays >= 30:
        month += 1
        ndays -= 30

    if ndays >= 31:
        month += 1
        ndays -= 31

    if ndays >= 31:
        month += 1
        ndays -= 31

    if ndays >= 30:
        month += 1
        ndays -= 30

    if ndays >= 31:
        month += 1
        ndays -= 31

    if ndays >= 30:
        month += 1
        ndays -= 30

    if ndays >= 31:
        month = 1
        ndays -= 31
        year += 1

day += ndays
print(day, month, year)


