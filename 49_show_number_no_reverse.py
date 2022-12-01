n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= n:
        print(j,end="")
        if j == n - i + 1:
            print("")
            break
        j += 1
    i += 1