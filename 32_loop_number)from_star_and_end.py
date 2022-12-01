sum = 0
x = int(input())
y = int(input())
i = x

while i <= y:
    print("%d" % i,end="")
    if i % 2 !=0:
        sum += i
    i += 1
print("")
print(sum)
    
