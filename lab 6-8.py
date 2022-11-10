#Prompts the user to give three numerical values
print('Type a numerical value')
a = int(input())
print('Type a numerical value')
b = int(input())
print('Type a numerical value')
c = int(input())
#Puts the numerical values in the list called Nlist
Nlist = [a, b, c]
print(Nlist) 
#Checks if the numbers are all even or odd, and if neither it will print mixed
if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print("Even")
elif a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
    print("Odd")
else: print ("mixed")
