#This file represent the data types in Python

#Data Types in Python
#1. int for integer
#2. float for decimal numbers
#3. str for string 
#4. complex for complex numbers
#5. dict for dictionaries
#6. list for lists
#7. tuples for tuples
#8. boolean for true or false values
#9. range for ranges
#10. set for sets

# name ="sudhaa"
# print(isinstance(name , str))
# age =40.5
# print(isinstance(age , int))


# data = input("please enter a number : ")
# print(data)


# value = int(data)/2
# print(value)

# program to check entered number is even or odd

def check(value):
    #value = int(number)

    if (value %2 == 0):
        return "even"
    else:
        return "odd"
    
e_number = input("please enter a number : ")
test = int(e_number)
result = check (test)
print(f"Given number {e_number} is : " + check (test))
        
