
print("Homework for Day 2")

name =input("Please enter your name :")
srname =input("Please enter your surname :")
age =input("Please enter your age :")
birth =input("Please enter your date of birth (just year) :")

info = [name,srname,age,birth]

for i in info :
    print(i)

if (int(age))<18 :
    print("You can not go out because it is too dangerous.")
else :
    print("You can go out to the street.")

