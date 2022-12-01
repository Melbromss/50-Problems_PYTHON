y1,m1,d1 = [int(e) for e in input("1 : ").split()]
y2,m2,d2 = [int(e) for e in input("1 : ").split()]

if y1 < y2:
    print("1")
elif y1 > y2:
    print("2")
elif y1 == y2:
    
    if m1 < m2:
        print("1")
    elif m1 > m2:
        print("2")
    elif m1 == m2:
        
        if d1 < d2:
            print("1")
        elif d1 > d2:
            print("2")
        elif d1 == d2 :
            print("equal !")