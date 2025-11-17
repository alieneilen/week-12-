# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

#Collectios are used to store multiple items in a single cariable 
#lists are ordered colletios of items
# lists are mutable, meaning you can change their content
# lists are created using square bracket []


list_of_fruits = ["apple", "banana", "cherry", "date"] 
print (list_of_fruits) # ['apple', 'banana', 'cherry', 'date']
print (type(list_of_fruits)) #<class 'list'>
#access items in list
print (list_of_fruits[0]) #apple
print (list_of_fruits[1]) #banana
print (list_of_fruits[-1]) #date
print (list_of_fruits[1:3]) # ['banana', 'cherry']
#reverse the list
list_of_fruits.reverse() 
print (list_of_fruits) #['date', 'cherry', 'banana', 'apple']
print (list_of_fruits [::-1])#['apple', 'banana', 'cherry', 'date']
#appending items to a list
list_of_fruits.append("elderberry") #add items to the end of the list 
print (list_of_fruits) #['date', 'cherry', 'banana', 'apple', 'elderberry']
#add two random
list_of_fruits.append("strawberry")
print (list_of_fruits) #['date', 'cherry', 'banana', 'apple', 'elderberry', 'strawberry']
list_of_fruits.append("blackberry")
print(list_of_fruits) #['date', 'cherry', 'banana', 'apple', 'elderberry', 'strawberry', 'blackberry']
# IF YOU DONT WANT TO HAVE TO DO MORE THAN TWO LINES TO ADD TO THE LIST, USE EXTEND--------------------------------------------------
list_of_fruits.extend (["fig", "grape", "honeydew"])
print (list_of_fruits)#['date', 'cherry', 'banana', 'apple', 'elderberry', 'strawberry', 'blackberry', 'fig', 'grape', 'honeydew']

list_of_fruits.reverse()
print(list_of_fruits) #['honeydew', 'grape', 'fig', 'blackberry', 'strawberry', 'elderberry', 'apple', 'banana', 'cherry', 'date']

popped_item = list_of_fruits.pop()
# remocs and returns the last item
print(popped_item) #date RETURNED
print(list_of_fruits) #['honeydew', 'grape', 'fig', 'blackberry', 'strawberry', 'elderberry', 'apple', 'banana', 'cherry'] NEW LIST




#+instering items at a specific index
list_of_fruits.insert(1, "blueberry")
print (list_of_fruits)
#removed a specific item by value
list_of_fruits.remove("banana") 
print(list_of_fruits)

list_of_fruits.insert(3," banana")
list_of_fruits.sort() #sorts the list to ascending order
print(list_of_fruits)
#why use lists and not variable?
#imagine you have 100 items to manage
list_of_items = list(range(1, 101)) #creates a list of numbers
print (list_of_items)
print(len(list_of_items))



#---------------------------------------------------------------------------------------------------------------------------------
# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.