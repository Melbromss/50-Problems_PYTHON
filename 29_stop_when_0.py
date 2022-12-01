maxeven = 0
maxodd = 0

while True:
    n = int(input())
    if n <=0:
        break
    else:
        if n % 2 == 0:
            if n > maxeven:
                maxeven = n
        else:
            if n > maxodd:
                maxodd = n

print(maxodd)
print(maxeven)

if maxeven > maxodd:
    print(maxeven-maxodd)
    
elif maxeven < maxodd:
    print(maxodd-maxeven)