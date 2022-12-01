f_name = input()
l_name = input()
age = input()
password = ""

if len(f_name) > 5 and len(l_name) > 5:
    password += f_name[:2]
    password += l_name[-1]
    password += age[-1]
    
else:
    password += f_name[0]
    password += age
    password += l_name[-1]
    
print(password)
    
    