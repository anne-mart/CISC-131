"""

Author: Anne Martin

Date: 13 June 2022

I certify that all the code represented in this file is 

either of my own making or given to me as part of the 

assignment.  Nor have I collaborated with anyone on this assignment. 

"""



from ssl import HAS_SNI


def main():

    #LEAP YEAR 

    year = int(input("Enter a year and I'll tell you if it is a leap year: "))

    is_ly = isLeapYear(year)

    if(is_ly):

        print(year,"is a leap year")

    else:

          print(year,"is not a leap year")



    #STRING REVERSE

    my_str1 = input("\nEnter a phrase and I'll show you it backwards: ")

    rev_str = reverseMyString(my_str1)

    print("Your phrase backward is:",rev_str)



    # #PALINDROME CHECK

    my_str2 = input("\nEnter a phrase and I'll tell you if it is a palindrome or not: ")

    is_pal = isPalindrome(my_str2)

    if(is_pal):

        print("You entered a palindrome")

    else:

        print("You did not enter a palindrome")

    

    #PRIME CHECKER

    num1 = int(input("\nEnter a number and I'll tell you if it is prime or not: "))

    is_prime = isPrime(num1)

    if(is_prime):

        print(num1,"is prime")

    else:

        print(num1,"is not prime")

    

    #NEXT PRIME

    num2 = int(input("\nEnter a number and I'll tell you the next number that is prime: "))

    next_prime = nextPrime(num2)

    print("The next prime is",next_prime)

 

 #YOUR FUNCTIONS HERE

 #Leap Year Checker
def isLeapYear (year):
    if ((year % 100 == 0) and (year % 400 == 0)):
        is_ly = True
    else:
        if (year % 4 == 0) and ((year % 100 != 0) and (year % 400 != 0)): 
            is_ly = True
    
        else:
            is_ly = False
    
    return is_ly


#String Reverse
def reverseMyString(my_str1): #come back to this one
    rev_str = ""
    index = len(my_str1) -1 
    while (index > -1): #take note strings and indexes have different starting points
        rev_str = rev_str + my_str1[index]
        index = index - 1


    return rev_str

#Palindrome Check
def isPalindrome(my_str2):
    if reverseMyString(my_str2) == my_str2:
        is_pal = True
    else:
        is_pal = False

    return is_pal



#Prime Checker
def isPrime(num1):
    is_prime = True
    
    if ((num1 % 2) != 0 ): #this tells us that the number is odd
       index = 3
       while (index < num1/2):
            if num1 % index == 0:
                is_prime = False
            index = index + 2 
        
        
    else: 
        if ((num1 % 2)== 0): #this would be an even number
            is_prime = False
            if num1 == 2:
                is_prime = True

    return is_prime


 #NextPrime
def nextPrime (num2):
    index = num2 + 1
    while (isPrime(index) == False):
        index = index + 1
    return index

   
main()