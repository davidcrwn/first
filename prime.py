n =int(input("enter a string\n"))
su=0
for i in range(1,n+1):
    if n%i==0:
      su=su+1
if su==2:
    print("prime")
else:
   print("not a prime")