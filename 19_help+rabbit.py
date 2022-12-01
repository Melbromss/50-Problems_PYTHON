s = input()
x = 0
h = 0

for i in range(len(s)):
    if s[i] == 'H':
        h = i
    if s[i] == 'X':
        x = i

if h < x:
    print("L" + str(x - h))
elif h > x:
    print("R" + str(h - x))