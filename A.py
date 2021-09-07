n,m = map(int,input().split())

if m>=n:
    if n%2!=0:
        print("Akshat")
    elif n%2==0:
        print("Malvika")
elif n>m:
    if m%2!=0:
        print("Akshat")
    elif m%2==0:
        print("Malvika")