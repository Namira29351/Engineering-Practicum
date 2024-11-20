import random

eight_ball_responses = [
    "response 1", 
        "response 2",
        "response 3",
        "response 4", 
        "response 5", 
        "response 6", 
        "response 7", 
        "response 8", 
        "response 9", 
        "response 10", 
    
]

random_number = random.randint(0, 9)

user_input = input("ask your question: ")

response = eight_ball_responses[random_number]

print(response)