n=int(input())
i=1
flag=0
while(i<=n):
    if(n%i==0):
        flag+=1
    i+=1
if(flag==2):
    print(f"the {n} is prime number")
else:
    print(f"the {n} is not prime number")
    