"""
Author: Anne Martin
Date: 25 May 2022
I certify that all the code represented in this file is 
either of my own making or given to me as part of the 
assignment.  Nor have I collaborated with anyone on this assignment. 
"""


import math
import string


# PART 1 VARIABLE VALUE ROTATION
# Below: prompt the user to enter three numbers and save them to variables named var1, var2, var3

var1 = input("enter var1 number: ")
var2 = input("enter var2 number: ")
var3 = input("enter var3 number: ")


# Do not edit this print statement
print("Original values: ", var1, var2, var3)

# Now swap (or rotate) the values of the variables so that 
# var2 has the value of orginal var1, 
var_a = var1
var_b = var2
var_c = var3

var2 = var_a


# var3 has the value of orginal var2, and 
var3 = var_b

# var1 has the value of orginal var3 
var1 = var_c

# Do not edit this print statement
print("Values after first swap: ", var1, var2, var3)
# Now rotate the values one more time

var1 = var_b
var2 = var_c
var3 = var_a


# Do not edit this print statement
print("Values after final swap: ", var1, var2, var3)
# END PART 1



# PART 2 TIP CALCULATOR
# Prompt the user to enter the amount of their bill.

bill_total = input("Please enter your bill: ")
bill_total = float(bill_total)


# Then you should calculate tips for 10%, 15%, and 20% and
tip_10 = round((bill_total * 0.10),2)
print("This is a 10% tip:  $",float(tip_10))


tip_15 = round((bill_total * 0.15),2)
print("This is a 15% tip:  $",float(tip_15))

tip_20 = round((bill_total * 0.20),2)
print("This is a 20% tip:  $",float(tip_20))


# report the tip amount and the bill+tip total.
print("This is the bill with a 10% tip: $", (float(bill_total + tip_10)))
print("This is the bill with a 15% tip: $", (float(bill_total + tip_15)))
print("This is the bill with a 20% tip: $", (float(bill_total + tip_20)))

# END PART 2



# PART 3
# Prompt the user to enter a 4 digit integer.  Using only the primitive)
# Python math operations (=,+,-,*,/,**,//,%) reverse the number they 
# entered, add 1 to it and print the result.
# END PART 3

enter_int = input("enter a four digit integer: ")
enter_int = int(enter_int)
print(enter_int)

num_1 =int(enter_int%10)

num_2 = int(enter_int%100)

num_3 = int(enter_int%1000)

num_4 = int(enter_int%10000)

pos_num_2 = ((num_3 - num_2) //100)  #will give 2 (if 1234)

pos_num_3 = ((num_2 - num_1) //10)  #will give 3 (if 1234)

pos_num_1 = ((num_4 - num_3) //1000)  #will give 1 (if 1234)

pos_num_4 = num_1 #will give 1 (if 1234)

#Reverse numbers
digit_1 = pos_num_4 * 1000 #will bring fourth number to first position
digit_2 = pos_num_3 * 100 #will bring third number to second position
digit_3 = pos_num_2 * 10 #will bring second number to third position
pos_num_1 #first number

reversed_digits = int(digit_1 + digit_2 + digit_3 + pos_num_1)
print("These are the digits reveresed:" , reversed_digits)


#Add one to reversed numbers
print("This is the reversed intergers plus one:" , reversed_digits + 1 )