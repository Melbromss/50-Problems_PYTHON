t = input()
n = int(input())

if t == 'H' and n == 4567:
    print("safe unlocked")

elif t != 'H' and n == 4567:
    print("change char")
    
elif t == 'H' and n != 4567:
    print("change digits")
    
else :
    print("safe locked")