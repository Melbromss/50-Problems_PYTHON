n = input()
count_c = 0
count_s = 0
au = ['a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','q','w','e','r','t','y','u','i','o','p']
aw = ['A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','Q','W','E','R','T','Y','U','I','O','P']

for i in range(len(n) - 1):
    
    if n[i] in aw:
        count_c +=1
    
    if n[i] in au:
        count_s +=1
        
if count_c == 4:
    print("capital letter")
    
elif count_s == 4 :
    print("small letter")
    
else :
    print("Mix")