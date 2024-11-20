import random

# -------------------------------------------- 

	# You've just learned about variables, conditionals.
	# Just from knowing those two topics, you can do so much!
	
	# Let's try to make a simple program that responds to the user.
	# We're going to recreate the Magic 8 Ball!!!
			
			# Never heard of it? That's ok!

					# You got this!

  # -------------------------------------------- 

	# How a Magic 8 Ball Works:

	# The user asks a question and vigoriously shakes the ball. 
	# Then the ball will respond with one of twenty responses, chosen at random. 

	# That's pretty simple right?

 # -------------------------------------------- 

	# Part 1: 
	# Print instructions on the screen and 
	# prompt the user to ask a question
print("Welcome to the magic 8 ball...\n Please ask a question, then your fortune will be told")
Prompt = input("What is your buring question?: ")

	

  # --------------------------------------------















# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19 
	# Use that to select from the following responses:
		# 0 - It is certain.
		# 1 - It is decidedly so.
		# 2 - Without a doubt.
		# 3 - Yes - definitely.
		# 4 - You may rely on it.
		# 5 - As I see it, yes.
		# 6 - Most likely.
		# 7 - Outlook good.
		# 8 - Yes.
		# 9 - Signs point to yes.
		# 10 - Reply hazy, try again.
		# 11 - Ask again later.
		# 12 - Better not tell you now.
		# 13 - Cannot predict now.
		# 14 - Concentrate and ask again.
		# 15 - Don't count on it.
		# 16 - My reply is no.
		# 17 - My sources say no.
		# 18 - Outlook not so good.
		# 19 - Very doubtful.

	# Look up random.rand_int to see how you can use it to select a random number.
x = random.randint
print(random.randint(0, 19))

if x == 0:
	print("It is certain.")
elif x == 1:
	print("It is decidedly so.")
elif x == 2:
	print("Without a doubt.")
elif x == 3:
	print("Yes - definitely.")
elif x == 4:
	print("You may rely on it.")
elif x == 5:
	print("As I see it, yes.")
elif x == 6:
	print("Most likely.")
elif x == 7:
	print("Outlook good.")
elif x == 8:
	print("Yes.")
elif x == 9:
	print("Signs point to yes.")
elif x == 10:
	print("Reply hazy, try again.")
elif x == 11:
	print("Ask again later.")
elif x == 12:
	print("Better not tell you now.")
elif x == 13:
	print("Cannot predict now.")
elif x == 14:
	print("Concentrate and ask again.")
elif x == 15:
	print("Don't count on it.")
elif x == 16:
	print("My reply is no.")
elif x == 17:
	print("My sources say no.")
elif x == 18:
	print("utlook not so good.")
elif x == 19:
	print("Very doubtful.")
  # -------------------------------------------- 




















# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 

















