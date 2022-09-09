"""

Author: Anne Martin

Date: 15 June 2022

I certify that all the code represented in this file is 

either of my own making or given to me as part of the 

assignment.  Nor have I collaborated with anyone on this assignment. 

"""


def main():

    total_points = float(input("Please enter the total number of points on the exam: "))

    scores = enterGrades()

    max_score = getMaxScore(scores)

    min_score = getMinScore(scores)

    avg_score = getAverageScore(scores)

    print("The max score was:",max_score," The min score was:", min_score, " The average score was:", avg_score)

    grades = getGradeCount(scores, total_points)

    printGradeBarchart (grades)





 #YOUR FUNCTIONS HERE

 #Enter Grades
def enterGrades ():
    grades = []
    print("Enter scores earned on exam. Enter -1 to stop.")
    cur_grades = float(input("Enter score for student 1: "))
    counter = 2
    while (cur_grades != -1):
        grades.append(cur_grades)
        cur_grades = float(input("Enter score for student "+ str(counter) + ": "))
        counter = counter + 1
    print("Thank you for entering your scores")
    return grades


#Maximum Score Earned
def getMaxScore(grades):
    temp_max = grades[0]
    for val in grades:
        if val > temp_max:
            temp_max = val
    return temp_max
           
        


#Minimum Score Earned
def getMinScore(grades):
    temp_min = grades[0]
    for val in grades:
        if val < temp_min:
            temp_min = val
    return temp_min


#Average Score Earned
def getAverageScore (grades):
    index = 0
    #counter = 0
    sum = 0
    while (index < len(grades)):
        sum = sum + grades[index]
        index = index + 1
    return round(sum/(len(grades)),2)

#Count the As, Bs, Cs, Ds, and Fs
def getGradeCount(grades, total_points):
    grade_count = [0,0,0,0,0]
    for val in grades:
        if val/total_points >= 0.90: #A
            grade_count[0] = grade_count[0] + 1
        
        if val/total_points < 0.90 and val/total_points >= 0.80: #B
            grade_count[1] = grade_count[1] + 1

        if val/total_points < 0.80 and val/total_points >= 0.70: #C
            grade_count[2] = grade_count[2] + 1

        if val/total_points < 0.70 and val/total_points >= 0.60: #D
            grade_count[3] = grade_count[3] + 1

        if val/total_points < 0.60: #F
            grade_count[4] = grade_count[4] + 1
    print(grade_count)
    return(grade_count)


#Display the Grade Bar Chart
def printGradeBarchart(grade_count):
    star_count_As = ""
    star_count_Bs = ""
    star_count_Cs = ""
    star_count_Ds = ""
    star_count_Fs = ""
    

    index = 0
    
    while (index < len(grade_count)):
        if index == 0:
            star_count_As = returnStars(grade_count[index])

        if index == 1:
            star_count_Bs = returnStars(grade_count[index])
        
        if index == 2:
            star_count_Cs = returnStars(grade_count[index])

        if index == 3:
            star_count_Ds = returnStars(grade_count[index])

        if index == 0:
            star_count_Fs = returnStars(grade_count[index])
    
        index = index + 1



    
    print ("Number of As: ", star_count_As)
    print ("Number of Bs: ", star_count_Bs)
    print ("Number of Cs: ", star_count_Cs)
    print ("Number of Ds: ", star_count_Ds)
    print ("Number of Fs: ", star_count_Fs)

    return star_count_As , star_count_Bs , star_count_Cs , star_count_Ds , star_count_Fs
    
def returnStars (n_stars):
    counter = 0
    stars = ""
    while (counter < n_stars):
        stars = stars + "*"
        counter = counter + 1
    return stars


main()


 