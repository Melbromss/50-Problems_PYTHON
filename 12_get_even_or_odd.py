n1,n2,n3= [int(e) for e in input().split()]

even = 0
odd = 0

if n1 % 2 == 0:
    even +=1
else:
    odd +=1

if n2 % 2 == 0:
    even +=1
else:
    odd +=1
    
if n3 % 2 == 0:
    even +=1
else:
    odd +=1
    
print("Odd has %d" % odd)
print("Even has %d" % even)