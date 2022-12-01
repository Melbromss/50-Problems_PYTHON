a,b = [int(e) for e in input().split()]

sum = 0
i = a

while i <= b:
    if i % 2 != 0:
        print("%d" % i,end="")
        sum +=1
    i +=1
    
print("")
print(sum)