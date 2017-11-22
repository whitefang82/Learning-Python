from sys import argv

script, user_name, place, com = argv
sign = '+ '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(sign)

print(f"Where do you live, {user_name}?")
lives = input(sign)

print("What kind of computer do you have?")
computer = input(sign)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where {place} is.
And you have a {computer}. Nice.
""")

#DO NOT forget f in print for variable
