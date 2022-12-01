sum = 0
ls = []

while True:
    n = int(input())
    if n == 5:
        break
    else:
        if n == 1:
            ls.append("Apple")
            sum += 100
        elif n == 2:
            ls.append("Papaya")
            sum += 120
        elif n == 3:
            ls.append("Banana")
            sum += 200
        elif n == 4:
            ls.append("Orange")
            sum += 60
            
for i in ls:
    print("You choose" + i)
    
print("Bye Bye")
print("Total CAlories" + str(sum))