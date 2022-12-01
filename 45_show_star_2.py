n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= n:
        print("*",end="")
        if j == i:
            print("")
        j += 1
    i += 1