n1,n2,n3 = [int(e) for e in input().split()]

if n1 < n2 and n1 < n3 and n2 < n3:
    print("Increasing")
    
elif  n1 > n2 and n1 > n3 and n2 > n3:
    print("Declined")
    
else:
    print("Neither")