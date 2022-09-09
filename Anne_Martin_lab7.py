"""
Author: 
Date:
I certify that all the code represented in this file is 
either of my own making or given to me as part of the 
assignment.  Nor have I collaborated with anyone on this assignment. 
"""

from itertools import count
from typing import Counter


def main():
    entered_list = getAList()
    sorted_list = entered_list[:] #make a copy of the original list
    sawinsBubbleSort(sorted_list)
    print("Testing that the order is correct:")
    is_ordered= isOrdered(sorted_list)
    if(not is_ordered):
        print("\tShoot! Doesn't look like the list is in order:")
        print("\t",sorted_list)
    else:
        print("\tSeems to be in order: Here it is:")
        print("\t",sorted_list)
        
    print("Testing that all the orginal values are still in place:")
    has_original_vals = equalExceptOrder(entered_list, sorted_list)
    if(not has_original_vals):
        print("\tShoot! Looks like the list isn't the same:")
        print("\tOriginal List: ",entered_list)
        print("\tSorted List:   ",sorted_list)  
    else:
        print("\tThe lists seems intact:")
        print("\tOriginal List: ",entered_list)
        print("\tSorted List:   ",sorted_list)
    

    print("Lets find the most common value in the list: ")
    most_common_info = getMostCommonValue(sorted_list)
    print("\tThe most common value in the list is",most_common_info[0],"it appears",most_common_info[1],"times.")


def sawinsBubbleSort(list): #modify this fxn
    while isOrdered(list) == False:
        index_outer = 0
        while(index_outer < len(list)): 
            index_inner = 1
            while(index_inner < (len(list) - index_outer)):
                if(list[index_inner - 1] > list[index_inner]): 
                    temp = list[index_inner -1]
                    list[index_inner -1] = list[index_inner]
                    list[index_inner ] = temp
                index_inner = index_inner + 1
            index_outer = index_outer + 1
    
    return
 
 #YOUR FUNCTIONS HERE

#Get Values
def getAList ():
    index = 0
    entered_list = []
    num_val = int(input("Enter the number of values you would like to enter: "))
    while (index < num_val): #<= ??
        val = str(input("Enter a value: "))
        entered_list.append(val)
        index = index + 1

    return entered_list


#Check Order
def isOrdered(entered_list):
    counter = 0
    while(counter < len(entered_list) - 1):
        if entered_list[counter] > entered_list[counter+1]:
            return False
        counter = counter + 1
    return True

#Check that lists have all the same values
def equalExceptOrder(entered_list , sorted_list): #must use pop in this problem
    sorted_copy = sorted_list[:]
    index = 0
    while (index < len(entered_list)):
        counter = 0
        value_found = False
        while (counter < len(sorted_copy) and value_found != True):
            if entered_list[index] == sorted_copy[counter]:
                sorted_copy.pop(counter)
                value_found = True
            counter = counter + 1

        index = index + 1

        if value_found != True:
            return False

    return True
            





#Find the Most Common Value
def getMostCommonValue(entered_list):
    most_common = [0,0]
    distinct_values = [] #will hold distinct values within the entered list
    num_times = [] #this will hold the number of times it appears


    #most_common[0] = 0 #placeholder for most commonly repeated number
    #most_common[1] = 0 #placeholder for number of times the most common value appeared
    #first list has the values and the second list has the number of times it appears
        
    for index in range(len(entered_list)): #Loop over index of entered_list
  
        has_duplicate = False
        
        for Counter in range(len(distinct_values)):
            if entered_list[index] == distinct_values[Counter]:
                has_duplicate = True
                num_times[Counter] = num_times[Counter] + 1

        if has_duplicate == False:
            distinct_values.append(entered_list[index])
            num_times.append(1)

    index = 0       
    temp_max = index #finding the max in num times
    
    while index < len(num_times):
        if num_times[index] > num_times[temp_max]:
            temp_max = index   
        index = index + 1

    most_common[0] = distinct_values[temp_max]
    most_common[1] = num_times[temp_max]
    
        
    return most_common

main()