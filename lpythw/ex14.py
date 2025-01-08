from sys import argv

script, use_name = argv
prompt = '>>>'

print(f"Hi {use_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {use_name}?")
likes = input(prompt)

print(f"Where do you live {use_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. No sure where that is. 
And you have a {computer} computer. Nice.
""")
