n = int(input())
x = 0
res = n // 10

print("10 bath = %d" % res)
x = n % 10
res = x // 5

print("5 bath = %d" % res)
x = x % 5
res = x // 2

print("2 bath = %d" % res)
x = x % 2
res = x // 1

print("1 bath = %d" % res)