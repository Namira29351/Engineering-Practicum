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
print("ask the magic 8 ball a question and it will give you an answer")
# prompt the user to ask a question
player_question = input("ask a question:")
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

  # -------------------------------------------- 
rand_int = random.randint(0,19)


if rand_int == 0:
    print("It is certain.")
elif rand_int == 1:
    print("It is decidedly so.")
elif rand_int == 2:
	print("Yes - Definetly.")
elif rand_int == 3:
	print("Without a doubt.")
elif rand_int == 4:
	print("You may rely on it.")
elif rand_int == 5:
	print("As I see it, yes.")
elif rand_int == 6:
	print("Most Likely")
elif rand_int == 7:
	print("Outlook good.")
elif rand_int == 8:
	print("Yes.")
elif rand_int == 9: 
	print("Signs point to yes.")
elif rand_int == 10:
	ptiny("Really hazy, try again.")
elif rand_int == 11:
	print("Ask again later.")
elif rand_int == 12:
	print("Better not tell you no.")
elif rand_int == 13:
	print("Cannot predict now.")
elif rand_int == 14:
	print("Concentrate and ask again.")
elif rand_int == 15:
	print("Dont' count on it.")
elif rand_int == 1:
	print("My reply is no.")
elif rand_int == 17:
	print("My sources say no.")
elif rand_int == 18:
	print("Outlook not so good.")
elif rand_int == 19:
	print("Very doubtful.")
else:
    print("expected answer to question")

















# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 

















