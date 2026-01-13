# BIO 2013 Round 1
# Question 1
# Watching the Clock

fast1 = int(input("How fast is the first clock"))
fast2 = int(input("How fast is the second clock"))

clock1 = clock2 = 0

while True:
   clock1 += 60+fast1
   clock2 += 60+fast2

   clock1 = clock1%(24*60)
   clock2 = clock2%(24*60)

   if clock1==clock2:
      break

hours = clock1//60
mins = clock1%60

if hours < 10:
   hours = '0' + str(hours)
if mins < 10:
   mins = '0' + str(mins)

print("{}:{}".format(hours, mins))

   
