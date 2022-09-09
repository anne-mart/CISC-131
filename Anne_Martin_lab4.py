"""

Author: Anne Martin

Date: 12 June 2022

I certify that all the code represented in this file is 

either of my own making or given to me as part of the 

assignment.  Nor have I collaborated with anyone on this assignment. 

"""
print("\t\t\t\tWelcome to Only Clean Words!")
def FindDarn (phrase): #finding darn
    index = 0
    has_darn = False
    while (index < len(phrase) and (has_darn == False)): 
        
       
        if len(phrase) <= index + 3:
            has_darn = False 

        else:
            char1 = phrase[index]
            char2 = phrase[index + 1]
            char3 = phrase[index + 2]
            char4 = phrase[index + 3]

            test_string = char1 + char2 + char3 + char4
        
            if index == 0:
                if test_string =="darn":
                    has_darn = True 
                    if len(phrase) > index + 4: #lengths start at 1 and indexes start at 0, so have to add -1
                       if phrase[index+4] != chr(32):
                            has_darn = False 
                       
            else:
                if test_string =="darn" and (phrase[index-1]) == chr(32):
                    has_darn = True
                    if len(phrase) > index + 4:
                       if phrase[index+4] != chr(32):
                            has_darn = False
                
        index = index +1
        
    return has_darn



user_input = input("Please enter your phrase: ")
user_phrase = user_input #if message is clean
phrase = FindDarn(user_input)



def censorDarn (phrase):
    index = 0
    new_phrase = ""
    has_darn = False
    while (index < len(phrase) and (has_darn == False)): 
        
       
        if len(phrase) <= index + 3:
            has_darn = False 

        else:
            char1 = phrase[index]
            char2 = phrase[index + 1]
            char3 = phrase[index + 2]
            char4 = phrase[index + 3]

            test_string = char1 + char2 + char3 + char4
        
            if index == 0:
                if test_string =="darn":
                    has_darn = True 
                    if len(phrase) > index + 4: #lengths start at 1 and indexes start at 0, so have to add -1
                       if phrase[index+4] != chr(32):
                            has_darn = False 
                       
            else:
                if test_string =="darn" and (phrase[index-1]) == chr(32):
                    has_darn = True
                    if len(phrase) > index + 4:
                       if phrase[index+4] != chr(32):
                            has_darn = False
                
        index = index +1

    star = index -1

    index = 0
    while (index < len(phrase)):
        
        if (index >= star) and (index <= star +3): 
            new_phrase = new_phrase + "*"
        else: 
            new_phrase = new_phrase + phrase[index]


        index = index + 1

    return new_phrase
    


if (phrase):
    print("Oh no! Your message contained explicit language.")
    print("Your censored message is", )
    print(censorDarn(user_input))
    


else:
    print("Good job. Your message contained polite language. Here is what you entered:")
    print (user_phrase)
