#puts the values of "Vishnu" and "Colin" in store in the variable my_row
my_row = ["Vishnu", "Colin"]
#Adds the value "Ben" after the value "Colin" in the variable my_row
my_row[3:3] = ["Ben"]
#Sets the variable my_row2 to be equal to the variable my_row
my_row2 = my_row

print(my_row2)
#deletes the first value in the list of my_row
del my_row[0]


print(my_row)
# I noticed that the first value in the list was deleted like told. this happened because I deleted the first index with del
