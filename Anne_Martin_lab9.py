"""
Author: Anne Martin
Date: 6/28
I certify that all the code represented in this file is 
either of my own making or given to me as part of the 
assignment.  Nor have I collaborated with anyone on this assignment. 
"""

import random
def main():
    #Get values for power calculations
    print("Wahoo Power Problem")
    base = onlyNumbersBetween3and18()
    exp = onlyNumbersBetween3and18()
    #calculate and print power
    ans = wahooPower(base,exp)
    print(base,"raise to the",exp,"is",ans)

    print("\nBandsaw Sequence")
    #gets value for bandsawSequence
    num = onlyNumbersBetween3and18()
    #calculate bandsaw sequence
    ans =bandsawSequence(num)
    print("The Bandsaw Sequence of",num,"is",ans)
    print("\nRandom List")


    #get length of the list to randomly fill
    list_len = onlyNumbersBetween3and18()
    #create list and randomly fill it
    my_list = []
    fillWithRandomVls(my_list,list_len)
    print("Here is the list:",my_list)
    print("\nSearch random list")

    #get a value to search for
    search_val = onlyNumbersBetween3and18()
    #search the list created above
    num_times = howManyTimesIn(my_list,search_val)
    print(search_val,"is in",my_list,num_times,"times.")


#My functions


#Get user input
def onlyNumbersBetween3and18():
    user_num = int(input("Enter a number between 3 and 18 (inclusive): "))
    if user_num >= 3 and user_num <=18:
        return user_num
    
    else:
        print("That is outside of input bounds. Please try again.")
        user_num = onlyNumbersBetween3and18()
        return user_num



#Wahoo Power Function
def wahooPower(base,exp):
    if exp == 0:
        return 1

    if exp % 2 == 0: #even
        sqrt_res = wahooPower(base, exp / 2)
        return sqrt_res * sqrt_res


    else:
        sqrt_res = wahooPower(base, (exp - 1 )/ 2)
        return sqrt_res * sqrt_res * base


#Bandsaw sequence
def bandsawSequence(pos_num):
    #basecase
    if pos_num == 1:
        return 1
    
    #even numbers
    if pos_num % 2 == 0:
        print(pos_num)
        if pos_num // 2 != 1 and pos_num % 2 == 0:
            pos_num = bandsawSequence(pos_num//2)
            return pos_num

        if pos_num // 2 != 1 and pos_num % 2 != 0:
            pos_num = bandsawSequence((pos_num*3)+1)
            return pos_num
        
        if pos_num == 2:
            return 1

        
        else:
            return pos_num
    
    #odd numbers
    if pos_num % 2 != 0:
        print(pos_num)
        if pos_num / 2 != 1:
            pos_num = bandsawSequence((pos_num*3)+1)
            return pos_num
        else:
            return pos_num



#Fill a list with Random Values
def fillWithRandomVls (lst,des_len):
    if len(lst) == des_len:
        return lst
    
    else:
        lst.append(random.randint(3,26))
        return fillWithRandomVls(lst,des_len)


#Search List
def howManyTimesIn(lst,val):
    copy_lis = lst[:]
    my_list = copy_lis
   
    if len(lst)==0:
        return 0
    
    else:
        if lst.pop(0) == val: 
            return howManyTimesIn(lst,val)+1 

        else:
            return howManyTimesIn(lst,val)


main()