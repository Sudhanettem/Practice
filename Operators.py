#1. Assignment operators

a= 2
b=5
name = "Sudha"
#2. Arithemetic operators
1+1 #2
3-2 #1
6/3 #2
4*3 #12
10/2 #5
4%2 #0
5//2 #2
#3. boolean operators
condition1 = True
condition2 = False

not condition1 #false
condition1 and condition2 
condition1 or condition2

#4. Bitwise operators
#& binary end operator
10&3
#| binary or operator
# ~ binary not operator
# ^ binary XOR oprator
# << left shift
# >> right shift 

#Ternary oprator

age = input("Please enter age : ")

def agecheck(age):
    data = int(age)
    return "Adult" if data > 18 else "child"
result = agecheck(age)
print(result)