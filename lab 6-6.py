#Asks the user for 5 words and is stored as a variable
print("type a word")
a = input()
print("type a word")
b = input()
print("type a word")
c = input()
print("type a word")
d = input()
print("type a word")
e = input()

#Variables are put in the list
ulist = [a, b, c, d, e]
#Gets the length of the words the user put in and stores it as a new variable
La = len(a)
Lb = len(b)
Lc = len(c)
Ld = len(d)
Le = len(e)
#Puts the corresponding variables in the same spots as the previous ones in a new list
Llist = [La, Lb, Lc, Ld, Le]
print(Llist)