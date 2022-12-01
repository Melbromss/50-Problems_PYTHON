n = input()
min = 100000
i = 1

while i <= n:
    x = int(input())
    
    if x < min:
        min = x
    i +=1
    
print(min)