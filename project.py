# Final Project
import random

name = "Ezgi"
surname = "Eyice"

lessons = []
grades = {}
testing = 3
while testing>0 :
    
    x = (input("Please Enter Your Name (be careful about the capitalization)   : "))
    y = (input("Please Enter Your Surname (be careful about the capitalization): "))
    print()
    if (x == name and y == surname) :
        print("Welcome Ezgi.")

        for i in range(5):
            a = input("Enter the lesson to create : ")
            lessons.append(a)

        print()
        print("******LESSONS******")
        for i in range(5) :
            print((i+1),"-",lessons[i])

        print()
        print("You must choose at least 3 of the lessons above.")
        taken_lessons = []
        taken = 0
        program = True
        
        while program :
            
            select = int(input("Enter the number of lesson you want to select : "))
            taken += 1
            
            taken_lessons.append(lessons[select-1])
            if taken < 3 :
                print("You have to select three lessons.")

            if taken > 2 :
                print("You don't have to select lesson anymore.Do you want to contunie? (yes or no) : ")
                ans = input()
                if ans == "no" :
                    program = False
        
        print()
        print("The SELECTED LESSONS") 
        for i in range(len(taken_lessons)) :
            print((i+1),"-",taken_lessons[i])

        
        chse = int(input("Choose the lesson for grades. Enter the number : "))

        chsen_lesson = taken_lessons[chse-1]

        midterm = random.randint(0,100)
        final = random.randint(0,100)
        project = random.randint(0,100)

        grades["midterm"] = midterm
        grades["final"] = final
        grades["project"] = project

        average = midterm*0.3 + final*0.5 + project*0.2
        print()

        if average>90 :
           print("Your letter grade is AA") 
        elif 70<average<90:
            print("Your letter grade is BB")
        elif 50<average<70:
            print("Your letter grade is CC")
        elif 30<average<50:
            print("Your letter grade is DD")
        else:
            print("Your letter grade is FF - You Failed")              

        print("Your average is ",average, " for ",chsen_lesson) 
        print()
        print("Do you want to exit? (yes or no)")
        f = input()
        if f == "yes":
            testing = -1

    elif (x == name and y != surname) :
        print("Wrong Surname. ")
        testing = testing - 1
    elif (x != name and y == surname) :
        print("Wrong Name. ")
        testing = testing - 1
    else :
        print("Wrong Name and Surname. ")
        testing = testing - 1

    if testing == 0 :
        print("Please try again later. ")


print()
print("You exit.")
    