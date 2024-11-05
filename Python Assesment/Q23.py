password = (input("Enter the Password: "))

ucount = 0
lcount = 0
dcount = 0

for char in password:
    if char.isupper():
        ucount += 1
    elif char.islower():
        lcount += 1
    elif char.isdigit():
        dcount += 1

if len(password) >= 8 and ucount > 0 and lcount > 0 and dcount > 0:
    print("valid.")
else:
    print("invalid.")
