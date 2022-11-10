
#puts numbers in a list
numbers = [1, 2, 3, 4, 6, 9, 9,]

#Sorts the numbers in the list in reverse order
numbers.sort(reverse=True)
#if the first index is the same as the last index, it will print that tbere was an error. if this is not the case, then it will print the first and last variable in the newly sorted list so it prints the highest and lowest variable
if numbers[0] == numbers[-1]:
    print("error:list does not meet specifications")
else : 
    print(numbers[0])
    print(numbers[-1])