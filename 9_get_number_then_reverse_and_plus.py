n = int(input())
s = input()
ones = n % 10
tens = n // 10
n2 = int(str(ones) + str (tens))

if s == '+':
    print("%d %s %d = %d" %(n,s,n2,n+n2))
    
elif s == '*':
    print("%d %s %d = %d" %(n,s,n2,n*n2))