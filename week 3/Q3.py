Str=input("Enter String : ")

print("String according to indexing ")
for i in range(0,len(Str)):
    print("Index ->",i,":",Str[i])
print("String at even index ")
for i in range(0,len(Str),3):
    print("Index ->",i,":",Str[i])