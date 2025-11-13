# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.****************

a = 3 #assigning values
b = 4

print(a == b)   # False seeing whether a is equal to b. since it is not, output is False. 
print(a != b)   # True. saying a is NOT equal to b. since this is true, output is true. 
print(a > b)    # False output says a is not greater than b. 
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5 #true
7 == 2 * 3 + 1 #true
8 != 8 #false
4 <= 2 + 2 #true

# Write 3 examples that result in True and 3 that result in False.
a= 12
b= 12

print (a==b) #true 
print (a<=b) #true
print (a>=b) #true

print (a>b) #false
print (a<b) #false
print (a!=b) #false



# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.
grade = int(input("Enter your score:"))
if grade >= 60:
        print("You passed the test!")
else: 
        print("You did not pass the test")


# # The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"

password = input ("Enter your passwrod: ")
if len(password) >= 8 and any(char.isdigit() for char in password): #for any character in password, if any character is a digit, print that
    print("Password is valid.")
else:
       print ("Password is invalid")
