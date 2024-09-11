n = int(input("Enter a Number: "))
print("Digits in reverse order:")

while n>0:
    digit = n % 10
    print(digit, end="")
    n = n//10