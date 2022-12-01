n = int(input ("Number : "))

ln = ["I","II","III","IV","V","VI","VII","VII","IX"]

if n < 0:
    print("ERROR : please fill in positive number")

elif n > 9:
    print("ERROR : Out of range")
    
else :
    print(ln[n - 1])