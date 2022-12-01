s = input()

ls = ["2","3","4","5","6","7","8","9","10"]

if s[0] in ls:
    print(s[0] + " of ")
    
elif s[0] == "A":
    print("Ace of ")
elif s[0] == "J":
    print("Jack of ")
elif s[0] == "Q":
    print("Queen of ")
elif s[0] == "K":
    print("King of ")
    
if s[1] == "D":
    print("Diamond")
elif s[1] == "H":
    print("Hearts")
elif s[1] == "C":
    print("Clubs")
elif s[1] == "S":
    print("Spades")
    
if len(s) == 3 :
    if s[:2] in ls :
        print(s[:2] + " of ",end="")
        if s[2] == "D":
            print("Diamond")
        elif s[2] == "H":
            print("Hearts")
        elif s[2] == "C":
            print("Clubs")
        elif s[2] == "S":
            print("Spades")
    