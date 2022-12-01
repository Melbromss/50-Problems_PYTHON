s1=input()
s2=input()
s3=input()

l1= len(s1)
l2= len(s2)
l3= len(s3)

if l1 == l2 and l1 == l3 and l2 == l3:
    print("all same")

elif l1 != l2 and l1 == l3:
    print("Neither")

elif l2 != l1 and l2 == l3:
    print("Neither")

else:
    
    if l1 > l2 and l1 > l3:
        print(l1)
    elif l2 > l1 and l2 > l3:
        print(l2)
    elif l3 > l1 and l3 > l2:
        print(l3)