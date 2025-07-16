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





n=int(input())
n=5
for i in range(n):
   for j in range(n):
      if i==3 or i==4 or j==3:
       print('*',end=' ')
   print()

n=int(input("Enter the number:"))
for row in range(n):
   for col in range (n):
      if col==0 or row==0 or row==n-1 or col==n-1:
         print('*',end='  ')
   print()
