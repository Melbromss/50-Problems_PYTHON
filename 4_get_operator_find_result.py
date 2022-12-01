n1,n2 = [int(e) for e in input().split()]
op = int(input())

if op == 1:
    print(n1+n2)

elif op == 2:
     print(n1-n2)

elif op == 3:
     print(n1*n2)
     
elif op == 4:
     print(n1/n2)
     
elif op == 5:
     print(n1%n2)

elif op == 6:
     print(n1*n2*n1*n2)
     
elif op == 7:
     print((n1+n2) /2)
     
else:
    print("ERROR !!!!")