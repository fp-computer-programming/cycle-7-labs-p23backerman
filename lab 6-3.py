#Puts my top 4 colors in a list stored as the colors value
colors = ["Yellow", "Purple", "Red", "Orange" ]
#Extends the list to have the values Blue, Green, and Pink at the end of the list
colors.extend(["Blue", "Green", "Pink"])
#Inserts the value black at the end of the list, and inserts the value “Brown” to the 3rd index of the list
colors.insert(7, "black")
colors.insert(2, "brown")
#Makes a copy of colors
Colors_Copy = colors

#Prints the variable colors before we change Colors_ Copy
print(colors)
#These lines remove the values from the variable
Colors_Copy.remove("Yellow")
Colors_Copy.remove("Blue")
Colors_Copy.remove("Green")
Colors_Copy.remove("Pink")
Colors_Copy.remove("black")
Colors_Copy.remove("brown")
Colors_Copy.remove("Purple")
Colors_Copy.remove("Red")
Colors_Copy.remove("Orange")
print(Colors_Copy)
