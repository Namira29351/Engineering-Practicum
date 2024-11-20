myName = "Namira"

for char in myName:
    print(char)

    myFriends = ["Susan", "Mary", "James", "Fredrick", "Hannah"]

for friend in myFriends:
        print(friend)

grades = [55,29, 30, 30, 50]
print("grades before curve: ", grades)

# each grade in grades is  increased by 25 
for count, grade in enumerate(grades):
    grades[count] = grade + 25

print("grades after curve: ", grades)