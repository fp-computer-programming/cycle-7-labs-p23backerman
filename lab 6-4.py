
#Stores the values math, english, and science in a list as the variable Classes
Classes = ['math', 'english', 'science']
#Adds the value history to the end of the list in Classes
Classes.append('history')

#prints the third value in Classes, which is science
print(Classes[2])

#.sort sorts the values in the variable Classes in Alphabetical Order
Classes.sort()
sorted_classes = Classes
print(sorted_classes)

#Makes a new variable c_Classes as a copy of Classes
c_Classes = Classes.copy()

print (c_Classes)

#Sorts the values in c_Classes in reverse alphabetical order
c_Classes.sort(reverse=True)

print(c_Classes)