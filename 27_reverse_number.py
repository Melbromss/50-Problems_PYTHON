n = int(input())
i = n
res = ""

while i > 0:
    x = i % 10 
    res  += str(x)
    i //= 10
print(res)
    
        