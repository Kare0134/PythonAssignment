#Assignment 1

print("KAREENA, 22108008, META")
print("\n")
      
################ 1st Program ################################################################################################

print("      First program")

#********Input from user***********
numb1=int(input("Enter the first number \n"))
numb2=int(input("Enter the second number \n"))
numb3=int(input("Enter the third number \n"))

#*******Formula***********
avg=(numb1+numb2+numb3)/3

print("The avg of number is: \n",avg)
print("\n")
print("\n")


################ 2nd Program ################################################################################################

print("      Second Program")

Tax_Rate = 0.20                    #Tax rate is 20%
Standard_Deduction = 10000         #It is in Dollor ($)
Dependent_Deduction = 3000         #It is in Dollor ($)

#********Input from user***********
Gross_Income = int(input("Enter your Gross Income in $ to the nearest penny: \n"))
Number_of_Dependents = int(input("Enter the number of dependents: \n"))

#***********Formula****************
Taxable_Income = Gross_Income-Standard_Deduction-(Dependent_Deduction*Number_of_Dependents)

Tax = Taxable_Income*Tax_Rate

if Tax<0:
    print("Your income tax is 0$")
else:
    print("Your tax is: \n",Tax)
    
print("\n")
print("\n")


################ 3rd Program ################################################################################################

print("      Third Program")

a = int(input("Enter number of seconds : \n"))
b = a//60
c = a%60
print(b,"minutes","and", c ,"seconds \n")

print("\n")
print("\n")

################ 4th Program ################################################################################################

print("      Fourth Program")

a = int(input("Enter a integer : \n"))
b = str(input("Enter a string : \n"))
c = float(input("Enter a float : \n"))

d = a+int(b)+int(c)

print(str(d))

print("\n")
print("\n")

################ 5th Program ################################################################################################

print("      Fifth Program")

import math
from math import *

for i in range(0,346,15):
    j = math.radians(i)
    print(i,"---",sin(j),cos(j) + "\n")
      

print("\n")
print("\n")
