n = int(input("Enter the Number:"))
fact = 1

while n > 1:
    fact = fact * n
    n = n - 1
    
print(fact)