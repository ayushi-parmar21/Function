k = int(input())
n = int(input())
l = []

for i in range(0, n):
    p = int(input())
    l.append(p)
    
def SumOfNumbers(l,n,k):
    l.sort()
    i=0
    while i<len(l):
        if i==k-1:
            min=l[i]
        i+=1
    l.reverse()
    j=0
    while j<len(l):
        if j==k-1:
            max=l[j]
        j+=1
    sum=max+min
    return sum
result = SumOfNumbers(l,n,k)
print(result)


