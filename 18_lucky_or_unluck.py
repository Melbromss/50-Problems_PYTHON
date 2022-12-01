n = int(input())

ln = len(n)

if n[0] == n[ln - 1]:
    print("Lucky")
    
elif (n[0] == 5 and n[ln - 1] == 5) or (n[0] ==9 and n[ln - 1] == 9):
    print("Veru lucky !!!")
    
else:
    print("Unsal")    