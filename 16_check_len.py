n = input()

if len(n) > 5 :
    print("Too long")
    
elif len(n) < 3 :
    print("Too short")
    
else:
    count = 0
    if n[2] == '1' :
        count +=1
    if n[3] == '1':
        count += 1
    if n[4] == '1':
        count +=1
        
    print(count)
    
    