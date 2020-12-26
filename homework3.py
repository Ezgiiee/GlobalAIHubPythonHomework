# RULES
# You can only try wrong character one more than the number of characters of the selected word.For example word is İstanbul. You have (8+1) guesses.

import random

print("Homework for Day 4")

name =input("Enter your name :")
print("Welcome {}".format(name.capitalize()))


x = random.randint(0,9)   # the number to determine word
words = ["İstanbul","İzmir","Ankara","Manisa","Çanakkale",
        "Sinop","Hatay","Antalya","Mugla","Tekirdag"]

chosen_word = words[x].lower()
wrong_guess = len(chosen_word)+1

guesses = ""

while wrong_guess > 0 :
    
    failed = 0
    for i in chosen_word :
        
        if i in guesses:
            print(i)
        else:
            print("-")    
            failed += 1

    if failed == 0:
            print("Congarts..You win..Game over.")    
            print("The secret word was ---> ",chosen_word)
            break

    guess = input("Enter a character : ")
    guesses += guess 

    if guess not in chosen_word :
        wrong_guess -= 1
        print("Wrong Guess.")
        print("You have", + wrong_guess, 'more guesses')
       
        if wrong_guess == 0:
            print("You Loose.Game over.")

