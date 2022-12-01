n = int(input())
i = 1
ls = []
s = ""

while i <= n:
    x = int(input())
    y = int(input())
    
    if x > y:
        ls.append(x)
    else:
        ls.append(y)
    
    i +=1
    
for i in range(len(ls)):
    if i != len(ls) - 1:
        s += str(ls[i])
        s += " + "
    else:
        s += str(ls[i])
        s += " = "
    sum += ls[i]
    
print(s + str(sum))