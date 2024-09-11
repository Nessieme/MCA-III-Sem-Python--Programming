n=int(input("Enter a number:"))
print(f"The cube of numbers from 1 to {n} are: ")

for i in range(1,n+1):
    cube = i**3
    print(f"Cube of {i} is {cube}")