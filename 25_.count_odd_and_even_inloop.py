even = 0
odd = 0

while True:
    n = int(input())
    if n == -1:
        break
    else:
        if n % 2 == 0:
            even +=1
        else:
            odd +=1

print(even)
print(odd)