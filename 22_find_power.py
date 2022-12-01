n = int(input())
ls = []
i = 1

while i <= n:
    x = int(input())
    power = x**x
    ls.append(power)
    i +=1
    
for i in ls:
    print(i)