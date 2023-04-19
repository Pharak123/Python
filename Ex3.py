# Solve the following using either while/do while loops
# 1) Take a number from the user and print sum from 1 to that number 

from calculation import accept_user
num= accept_user()
print(num)
sum=0
i=0
while (i<=num):
    sum+=i
    i+=1
print(sum)

####################################################################################################################

#2) Take a number from the user and print all prime numbers from 1 to that number 
# from calculation import accept_user

def is_prime_number(number):
   
    for i in range(2,(number//2)+1):
    
        if number%i == 0:
            return print("not prime number ",number)
            
    return print("prime number",number)
    
    


for i in range(1,accept_user()+1):
     
     is_prime_number(i)
     
####################################################################################################################
# 3) Take a number from the user and print all Odd numbers from 1 to that number 

from calculation import accept_user
def odd_number(iteration_number):
    if i%2 != 0:
        print (iteration_number," is Odd number")

for i in range(accept_user()+1):
    odd_number(i)
#4) Take a number from the user and print all Even numbers from 1 to that number  
from calculation import accept_user
def even_number(iteration_number):
    if i%2 == 0:
        print (iteration_number," is even number")

for i in range(accept_user()+1):
    even_number(i)      
####################################################################################################################
# 5) Take a number from the user and print fibonacci sequence till that number
# 	eg : fibonnaci sequence for 5 is 0,1,1,2,3,5
from calculation import accept_user

x=1
y=0
sum=0
num = accept_user()
#accept_user()
for i in range(-1,num+1):
         
        if sum > num:
            break 
        print(sum) 
        
        sum=x+y  
        x=y
        y=sum

    
   
