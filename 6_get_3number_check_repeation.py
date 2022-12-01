n1,n2,n3 = [int(e) for e in input().split()]

if n1 == n2 and n2 == n3 and n1 == n3:
    print("All same")
    
elif n1 != n2 and n2 != n3 and n1 != n3:
    print("All diffent")
    
else:
    print("Neither")
    