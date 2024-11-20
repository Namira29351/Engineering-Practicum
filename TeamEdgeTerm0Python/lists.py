#********************************************************************
                                                                  
 #  Team Edge list Challenges!                                     
  
 #  Use this program to learn about Python lists:
    
 #  1. Declare and store data in lists
 #  2. Access list data by index
 #  3. Modify list data by index
 #  4. Multi-dimensional lists (lists inside lists!)
 #  5. List methods: append() and pop()
 #  6. The length of the list - introduce conditionals
 #  7. Strings as sequences - join() split() 
 #  
 #  Follow the -->To Dos ! run the program to test often and debug
 # ***************************************************************





print("------------------- CHALLENGE 1 -------------------")
#This is an empty Python list:
empty_list = []

#this list has 5 Strings. We can print it:
names = ["Sam", "Wolf", "Alex", "Bella", "Shaquan"]
print("names: " + str(names))  

#-->TODO: Declare another list called friends with at least 5 strings inside (if you don't have 5 friends make them up!)
friends = ["Mary", "Susan", "James", "Maria", "Richard"]
print("friends: " + str(friends))

#this list holds numbers
numbers = [12.9, 23.4 , 100, 3.1415 , 500, 1.20]
print("numbers: " + str(numbers)) 

#-->TODO: Declare another list and add in at least 5 numbers. Why five? I don't know. It just feels right.
integers = [13, 14, 15, 16, 23]
print("integers: " + str(integers))
integers.append (43)
print("integers: " + str(integers))

#this list has mixed data types. It's allowed in Python!
random_stuff = ["Aardvark", True, False, 1.23, "Grandpa"]
print("random: " + str(random_stuff))

#-->TODO: Declare and log a list filled with the first 5 things that come into your head, booleans, Strings, numbers are all cool,
rando_things = ["CT", 35, "fire", False, True]
print("rando: " + str(rando_things))

#-->TODO: Declare and log two more lists with whatever you want. 

books = ["Hunger Games", "Harry Potter", "Game of Thrones"]
print("favorites: " + str(books))

elements = ["Fire", "Earth", "Watrer", "Air"]
print("elements: " + str(elements))

print("------------------- CHALLENGE 2 -------------------")
 
#This code logs the first element of the names list:
print("The first name is " + names[0])

#-->TODO: Print the name of your best friend from your friends list
print("Best Friend: " + friends[1])

#-->TODO: Print the first AND last elements of any list you made, or make a brand new one.
print("favorites books: " + books[0] +  " "  + books[2])

print("------------------- CHALLENGE 3 -------------------")
#this code changes the value of the second element of the names list, then we print the list:
names[1] = "Alyssa"
print(names)

#-->TODO: Replace your friends! Modify the list to replace any or all of your friends with new ones.
friends[3] = "Synthia"
print(friends)

#The code below uses the times_ten() function to multiply the first element in our list by 10:
def times_ten(number):
    number = number * 10
    return number

numbers[0] = times_ten(numbers[0])
print(numbers)

#-->TODO: Write another function that multiplies a number by 1000 and print the list, as above 
def times_thousand(integers):
    integers = integers * 1000
    return integers

integers[3] = times_thousand(integers[3])
print(integers)


#-->TODO: Replace your random list elements with anything you want, using the index. 
rando_things[0] = "CND"
print(rando_things)
print("------------------- CHALLENGE 4 -------------------")

#As it turns out, you can also store lists within lists! Declare them and store them as variables.
child_list_1 = ["This", "is" , "a", "meaningless", "list"]
child_list_2 = ["This" ,"list" , "is", "also" , "meaningless"]
parent_list = [child_list_1, child_list_2]
print("This list has babies: " + str(parent_list))

#-->TODO: Store and print all the lists we have worked on thus far in a new parent list
child_list_1 = ["Mary", "Susan", "James", "Synthia", "Richard"]
child_list_2 = [13, 14, 15, 16000, 23, 43]
parent_list = [child_list_1, child_list_2]
print("Random stuff: " + str(parent_list))

print("------------------- CHALLENGE 5 -------------------")

#We can add elements into a list wihtout replacing anything. Using append() adds an element to the END of the list:
movies = ["Toy Story 4", "The Dark Knight", "Parasite"]
print("Movies: " + str(movies))
movies.append("Joker")
movies.append("Black Panther")
print("Movies now has: " + str(movies))

#-->TODO: Declare a list with 5 favorite songs
songs = ["Sorry", "That Should Be Me", "One Time", "Company", "What Do You Mean"]
print("Justine Bieber: " + str(songs))


#-->TODO: Add 2-3 more songs using .append() and print both before and after.
songs.append("Flatline")
songs.append("Cold Water")
print("More Songs: " + str(songs))

#We can also remove elements using .pop(), which removes the last element or the element at the given index. You can store it after it comes out:
cities = ["New York", "Oakland", "Las Vegas", "Topeka"]
print("cities: " + str(cities))
unwanted_city = cities.pop()
print("unwanted city: " + str(unwanted_city))

#-->TODO: remove your last song using .pop() and print the removed element as above
songs = ["Sorry", "That Should Be Me", "One Time", "Company", "What Do You Mean", "Flatline", "Cold Water"]
print("songs: " + str(songs))
bad_songs = songs.pop()
print("bad song: " + str(bad_songs))
#Note: there are more methods to remove and modify list elements. We will cover those later

print("------------------- CHALLENGE 6 -------------------")

#Lists have properties. one of the most important is the size, or length. Here are two examples:
print(f"I have {len(names)} friends")

how_many_cities = len(cities)
print(f"There are {how_many_cities} ciites in my list")

#-->TODO: Print out the number of friends, or other items from other lists using string literals as above


how_many_friends = len(friends)
print(f"There are {how_many_friends} friends in my list")

#The len() function is key, especially in conditionals or to simply count how many times to do something.

if len(numbers) > 3:
    print("There are more than 3 numbers in my list")
else:
    print("I need more numbers in my list!!!")

#-->TODO: Write another if/else statement to check the size of your songs list. If you have 5 of less, add two more songs!
if len(numbers) > 5:
    print("My song list is good")

else:
    print("Fire Boy", "Water Girl")

print("------------------- CHALLENGE 6 -------------------")

#Strings can also be thought of lists:
sentence = "I am a boring sentence."
boring_list = sentence.split(" ") #split the sentence by each space to get a list of words
print("boring sentence as a list: " + str(boring_list))

word = "Abracadabra"
word_split_list = word.split() #split by nothing, and you get each character in the string as its own element.
print("letter by letter: " + str(word_split_list))

#using this you can split strings up by any character!

#-->TODO: Change the name of the person who is late in this sentence and print it.
split_me = "I heard Alex was late to class today."
print(str(split_me))
split_me = "I heard Sam was late to class today."
print(str(split_me))
#-->TODO: Add an exclamation mark to this sentence using split() and append(), then print. (yes, there are other ways, but...)
make_me_exciting = "What a wonderful day"
exciting = make_me_exciting.split("!")
print(str(exciting))
exciting.append("!")
print(str(exciting))

#We can also join our list elements into a string using.....join()!
rejoined = " ".join(boring_list)  #joins it using spaces
print('back in one piece: ' + rejoined)

#-->TODO:  Finally, put the split_me sentence today and the make_me_exciting strings back together and print. You should see a string
rejoined = "".join(split_me + " " + make_me_exciting)
print("back in one: " + rejoined)