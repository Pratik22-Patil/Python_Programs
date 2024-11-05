a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))

if a > b and a > c:
    print(a,"a is greater")
elif b > c and b > a:
    print(b,"b is greater")
else:
    print(c,"c is greater")