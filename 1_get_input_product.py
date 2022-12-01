unit = int(input("Unit : "))
price = int(input("Price : "))
member = input("Are you member ? (y/n) : ")
total = unit * price
sale = 0

# ! member
if member == 'y':
    if total <=500:
        sale = total * 0.1
    elif total >=500 and total <1000:
        sale = total *0.15
    else:
        sale = total * 0.2
        
# todo not member
elif member == 'n':
     if total <=500:
        sale = total * 0.05
     elif total >=500 and total <1000:
        sale = total *0.1
     else:
        sale = total * 0.15
 
new_price = total - sale
        
print("Total %.2f" % total)
print("Discount %.2f" % sale)
print("Amount %.2f" % new_price)