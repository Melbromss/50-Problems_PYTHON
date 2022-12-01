count = 0
ls = []
maxs = 0
n1 = int(input())

while True:
    n2 = int(input())
    if n2 ==0:
        break
    else:
        if n2 == n1:
            count +=1
        else:
            ls.append(count)
            count = 0

for i in ls:
    if i > maxs:
        maxs = i
        
print(maxs)