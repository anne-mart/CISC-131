/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
/*
Author: 
Date:
I certify that all the code represented in this file is 
either of my own making or given to me as part of the 
assignment.  Nor have I collaborated with anyone on this assignment. 
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    //Variables
    int user_input; //Will hold user input of 1,2, or 3
    char junk_new_line;
    int rand_int; //will hold computer's number
    int win_count; //will hold number of times user won
    int loss_count; //will hold number of times user lost
    int tie_count; //will hold number of ties
    char y_or_n;
    int num_rounds;
    
    win_count = 0;
    loss_count = 0;
    tie_count = 0;
    num_rounds = 0;
   
   
printf("Would you like to play rock paper scissors? Enter y for yes and n for no");
printf("\n");
scanf("%c",&y_or_n);
scanf("%c",&junk_new_line);

while (y_or_n == 'y'){
   printf("Please enter 1 for rock, 2 for paper, or 3 for scissors: ");
   scanf("%i",&user_input);
   scanf("%c",&junk_new_line);
 
 //If user_input != 1,2, or 3
 while ((user_input < 1)||(user_input > 3)) {
        printf("Sorry, that was not a valid entry");
        printf("\n");
        printf("Please enter 1 for rock, 2 for paper, or 3 for scissors: ");
        scanf("%i",&user_input);
        scanf("%c",&junk_new_line);
   }
       

    //If user_input = 1
    if (user_input == 1){
        printf("You chose rock");
    }
    
    
    //If user_input = 2
    if (user_input == 2){
        printf("You chose paper");
    }
    
    //If user_input = 3
    if (user_input == 3){
        printf("You chose scissors");
    }
   
   //Computer randomly generated value
    srand(time(NULL)); //time(NULL) sends see to CPU
    rand_int = rand(); //will return positive integer
    rand_int = ((rand_int % 3)+1);
    printf("\n");
    //a = num-1%3 will return 0
    //(num%3 + 1) return 1,2,or 3 USE THIS
    
    
    //If computer generates 1 (rock)
    if (rand_int == 1){
        printf("The computer chose rock");
        printf("\n");
    }
    
    //If computer generates 2 (paper)
    if (rand_int == 2){
        printf("The computer chose paper");
        printf("\n");
    }   
        
    //If computer generates 3 (scissors)
    if (rand_int == 3){
        printf("The computer chose scissors");
        printf("\n");
    }
    
    
    
    //Results
    if ((user_input == 1) && (rand_int == 2)){
        printf("You lost!");
        printf("\n");
        loss_count = loss_count + 1;
    }
    
    if ((user_input == 1) && (rand_int == 3)){
        printf("You won!");
        printf("\n");
        win_count = win_count + 1;
    }
    
    if ((user_input == 1) && (rand_int == 1)){
        printf("You tied!");
        printf("\n");
        tie_count = tie_count + 1;
    }
    
    if ((user_input == 2) && (rand_int == 1)){
        printf("You won!");
        printf("\n");
        win_count = win_count + 1;
    }
    
    if ((user_input == 2) && (rand_int == 2)){
        printf("You tied!");
        printf("\n");
        tie_count = tie_count + 1;
    }
    
    if ((user_input == 2) && (rand_int == 3)){
        printf("You lost!");
        printf("\n");
        loss_count = loss_count + 1;
    }
    
    if ((user_input == 3) && (rand_int == 1)){
        printf("You lost!");
        printf("\n");
        loss_count = loss_count + 1;
    }
    
    if ((user_input == 3) && (rand_int == 2)){
        printf("You won!");
        printf("\n");
        win_count = win_count + 1;
    }
   
    if ((user_input == 3) && (rand_int == 3)){
        printf("You tied!");
        printf("\n");
        tie_count = tie_count + 1;
    }
    

    
    
    num_rounds = num_rounds + 1;
    
    printf("Would you like to play rock paper scissors again? Enter y for yes and n for no");
    printf("\n");
    scanf("%c",&y_or_n);
    scanf("%c",&junk_new_line);
}
   
   
//Displaying wins and losses 
printf("The game is now over");
printf("\n");
//Display wins, losses, and ties
printf("You won %i times",win_count); 
printf("\n");
printf("You lost %i times",loss_count); 
printf("\n");
printf("You ties %i times",tie_count); 
printf("\n");





    return 0;
}
