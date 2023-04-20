# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
from calculation import accept_user
a = []
for i in range(8):
    a.append(accept_user())
result = filter(lambda i: i < 5, a)
print(list(result)) 
#  #filter function :
#  Time complexity analysis:
# 1.The filter function is used to filter the list of numbers, and 
# it applies the lambda function to each element of the list. 
# The time complexity of the filter function is O(n), where n is the number of elements in the list.
# 2.The time complexity of the lambda function is constant, O(1), 
# since it only performs a single arithmetic operation. 
# Therefore, the overall time complexity of the program is O(n).

#####################################################################################################################
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.

from calculation import my_division,accept_user
num = accept_user()
a=range(1,num+1)
result = filter(lambda i: num % i == 0, a)
    
print(list(result)) 

#######################################################################################################################
# Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Extras:
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
import random
a = []
b = []
for i in range(10):
    a.append(random.randint(0,9))
for i in range(6):
    b.append(random.randint(0,9))
print("b ",b)
print("a", a)
#######################################################################################################################
#Print First 10 natural numbers using while loop
i=1
a=range(10+1)
while i in a:
    print(i)
    i=i+1
#########################################################################################################################
#Exercise 2: Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
i=1
for i in range(6):
    j=1
    for j in range(1,i+1):
        print(j,end=' ')
    print()
    
 #same code with while loop   
while (i<=5):
   
    j=1
    while (j<=i):
        print(j,end=" ")
        j=j+1
    print()
    i=i+1
#########################################################################################################################
# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
num= int(input("Enter the Number: "))
sum=0
for i in range(num+1):
    sum+=i
print("sum",sum)
#########################################################################################################################
#Write a program to print multiplication table of a given number
num= int(input("Enter the Number: "))
for i in range(1,11):
 print("table",i*num)
 #########################################################################################################################
#  Display numbers from a list using loop

# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

# Given:

numbers = [12, 75, 150, 180, 145, 525, 50]
#########################################################################################################################\
#   Exercise 7: Print the following pattern
# Write a program to use for loop to print the following reverse number pattern

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1  

num= int(input("Enter the the number : "))
i=1

while (num>=i):
    j=num
    while(j>=i):
        
        print(j,end=' ')
        j-=1
    print(' ')
    
    num-=1
 
def print_reverse(row):
    for number in range(row,0,-1):
        print(number, end =' ')
    
input_row = int(input("Enter the Number :"))
for row in range(input_row,0,-1):
    print_reverse(row)
    print('')    
#########################################################################################################################\
# Exercise 9: Display numbers from -10 to -1 using for loop
# Expected output:

# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

for i in range(-10,0):
    print(i)
    
#########################################################################################################################
fact = 1
#1 way
for i in range(int(input("Enter number: ")),1,-1):
        fact*=i
print(fact)
#2nd way
num=int(input("Enter number: "))
while i in range(num,0,-1):
        fact*=i
        i+=1
print(fact)


#3rd way
i=1
while(num>=i):
    fact*=num
    num-=1
print(fact)
#############################################################################################################
# Exercise 14: Reverse a given integer number
# Given:

# 76542

# Expected output:

# 24567
number = int(input("Enter the number : "))

def extract_digit_from_end(number):
    new_number = 0
    while(number):
        digit = number % 10
        new_number = (new_number * 10) + digit
        number= number // 10
        
    return new_number

print(extract_digit_from_end(int(input("Enter the number : "))))

#############################################################################################################
# Calculate the cube of all numbers from 1 to a given number
number = int(input("Number"))
for i in range(1,number+1):
    print(f"Current Number is :{i}  and the cube is {i**3}")

#############################################################################################################
# Exercise 18: Print the following pattern
# Write a program to print the following start pattern using the for loop

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


for i in range(1,6):
    
    j=1
    for i in range(j,i+1):
        print("*",end=' ')
    print()
    
for i in range(5,0,-1):
   
    for j in range(i,1,-1):
        print("*",end=' ')
    print()
#################################################################################
# * 
# * *
# * * *
# * *
# *

def triangle(higher):
    i=1
    while(i<=higher):
        print("*",end=' ')
        i=i+1
def reverse_triangle(higher):
    for num in range (higher,0,-1):
        print('*',end=' ')
        
inp_rows = int(input("please enter the number of rows: "))//2
for row in range(1,inp_rows+2):
    triangle(row)
    print('')
for row in range(inp_rows,0,-1):
     reverse_triangle(row)
     print('')
    
#################################################################################    

#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
rows=int(input("Enter the rows: "))
reverse_rows = rows
for i in range(1,rows+1):
    for spaces in range(0,rows-i):
   
        print(" ",end=' ')
    for star in range(0,2*i-1):
        print("*",end=' ')
    print('')
    

for i in range(reverse_rows-1,0,-1):
    for spaces in range(rows-i,0,-1):
    #print(spaces)
    #for j in range(spaces,columns+1):
        print(" ",end=' ')
    for star in range(2*i-1,0,-1):
        print("*",end=' ')
    print('')


