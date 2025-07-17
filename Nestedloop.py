n = 5 
for i in range(n):
  for j in range(n):
      print('*', end=' ')
  print()


n = 5
for i in range(n):
   for j in range(i + 1):
      print('*', end=' ')
   print()

n = 5
for i in range(n, 0, -1):
   for j in range(i):
      print('*', end=' ')
   print()


n = 5
for i in range(n):
  print(' ' * (n - i - 1) + '* ' * (i + 1))


n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
      print(j, end=' ')
    print()



n=7
for row in range(n):
   for col in range (n):
      if col==0 or row==0 or row==n-1 or col==n-1:
         print('*',end=' ')
      else:
         print(' ',end=' ')
   print()


#A
n=7
for row in range (n):
   for col in range (n):
      if col==0 or row==0 or col==n-1 or row==n//2:
          print('*',end=' ')
      else:
         print(' ',end=' ')
   print()   


#B
n=5
for row in range (n):
   for col in range(n):
      if col==0 or row==0 or col==n-1 or row==n-1 or row==n//2:
          print('*',end=' ')
      else:
         print(' ',end=' ')
   print()

#c
for row in range (n):
   for col in range(n):
      if col==0 or row==0 or row==n-1:
          print('*',end=' ')
      else:
         print(' ',end=' ')
   print()

for i in range (0,3):
   for j in range (0,3):
    if (j<=i):
      print(j+1,end=" ")
   print()


for i in range (0,3):
   for j in range (0,3):
    if i==0 <=2:
      print('*',end=" ")
   print()






