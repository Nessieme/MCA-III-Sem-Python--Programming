numbers= []

print("Enter 20 Numbers:")
for _ in range(20):
    number= int(input())
    numbers.append(number)
    
print("Numbers divisible by 5 are: ")
for number in numbers:
    if number%5 == 0 :
        
        print(number)