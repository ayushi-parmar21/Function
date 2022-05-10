def prime(limit):
    j=1
    while j<=limit:
        count=0
        i=2
        while (i<=j//2):
            if j% i == 0:
                count=count+1
                break
            i+=1
        if count==0 and j!=1:
            print(j,end=",")
        j+=1
prime(int(input("enter a number")))
print()