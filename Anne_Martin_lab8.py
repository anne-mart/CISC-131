"""
Author: Anne Martin
Date: 6/27
I certify that all the code represented in this file is 
either of my own making or given to me as part of the 
assignment.  Nor have I collaborated with anyone on this assignment. 
"""

import random
def main():
   
    #Simulation set up phase
    print("Setting up simulation:")
    candidates_and_votes = getCandidateAndInitialVotes()
    num_voters = getNumVoters()
    print(candidates_and_votes,num_voters)

    #Start Voting Simulation
    print("Simulating Election Day")
    simulateVoting(candidates_and_votes, num_voters)
    printVoteTallies(candidates_and_votes)
    declareWinner(candidates_and_votes)

#Your Functions Below


#Getting the candidate names and their initial votes set up
def getCandidateAndInitialVotes():
    candidates = {} 
    user_input = int(input("Enter how many candidates you plan to use in this simulation: "))
    counter = 0
    while counter < user_input:
        cur_name = input("Enter the name for candidate: ")
        while cur_name in candidates:
            print("It looks like you already entered that candidate")
            cur_name = input("Enter the name for candidate: ")
        
        candidates[cur_name] = 0
        counter = counter + 1

    print(candidates)
    return candidates #list of candidates mapping to vote counts


#Get the number of voters to simulate
def getNumVoters (): #does this take any parameters?
    num_voters = int(input("How many voters would you like to simulate?: "))
    while num_voters < 0:
        print("You cannot simulate negative voters. Try again.")
        int(input("How many voters would you like to simulate?: "))

    return num_voters


#Simulate Election Day
def simulateVoting (candidates , num_voters): 
    index = 1 #to track number of voters
    keys = candidates.keys() #turning dictionary into list
    keys = list(keys) #turning dictionary into list

    while index < num_voters+ 1:
        random_candidate = keys[random.randint(0,len(keys)-1)]
        #print(random_candidate)
        candidates[random_candidate] = candidates[random_candidate] + 1 #updates vote value associated to candidate
        print("Voter",index,"voted for: ",random_candidate)
        index = index + 1

    print(candidates)



#Printing the results
def printVoteTallies(candidates_copy):
    print("Your results are: ")
    for candidate in candidates_copy:
        print("\t\t",candidate,"\t\t",candidates_copy[candidate]) #fix so it prints in a nicer format



#Declaring the winner
def declareWinner(candidates_copy):
    keys = candidates_copy.keys()
    keys = list(keys) 
    temp_max_key = keys[0] #gives key
    temp_max =candidates_copy[temp_max_key] #value

    num_voters = 0

    tie = False
    for key in keys:
        if candidates_copy[key] > temp_max:
            temp_max = candidates_copy[key]
            temp_max_key = key
            tie = False
        else:
            if candidates_copy[key] == temp_max and key != temp_max_key:
                tie = True
                tie_key = key
                print("There was a tie.")

        num_voters = num_voters + candidates_copy[key]

    if tie == False:
        print("Winner is: ",temp_max_key,"They won with",((temp_max/num_voters)*100),"% of vote")
        

main()