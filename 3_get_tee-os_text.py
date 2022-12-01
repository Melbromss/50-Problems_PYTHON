s1= input()
count = 1
s2 =' '
for i in range(len(s1)):
    
    if i != len(s1) - 1:
        
        if s1[i] == s1[i+1] :
            count +=1
        
        else:
            s2 += str(count)
            s2 += s1[i]
            count = 1
            
    elif i == len(s1) - 1:
        s2 += str(count)
        s2 +=s1[i]

print(s2)
         