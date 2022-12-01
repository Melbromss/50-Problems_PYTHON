p = input()
count = 0
n = [0,1,2,3,4,5,6,7,8,9]
ln = ['0','1','2','3','4','5','6','7','8','9']
au = ['a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','q','w','e','r','t','y','u','i','o','p']
aw = ['A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','Q','W','E','R','T','Y','U','I','O','P']

if p[0] in ln:
    print(p,((int(p[0]) + 9) % 5))
    
elif p[0] in au:
    
    for i in len(p):
        if p[i] in n:
            count +=1
    print(p,(count + 2) % 3)
    
elif p[0] in aw:
    if p[3] in ln or p[3] in aw:
        print(p,p[0].lower)
    elif p[3] in au:
         print(p,p[0].upper)