for i in range(0,5):
   print('*',end=" ")
print()

print("==========")
 
for j in range(0,5):
   print("*",end=" ")
   print()

print("==========")

for i in range (6):
   for j in range (7):
      if (i==0 and j %3!=0) or (i==0 and j%3==0) and (i==0 and j%3==0) or (i-j==0 and i+j==8) :
         print("*",end=' ')
   print() 
