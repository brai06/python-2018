
import random
import time

responses = ["It is certain.", "It is decidedly so.", "Without a doubt.",
             "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
             "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
             "Ask again later.", "Better not tell you now.", "Cannot predict now.",
             "Concentrate and ask again.", "Don't count on it.",
             "My reply is no.", "My sources say no.", "Outlook not so good.",
             "Very doubtful."]

name = input("What is your name?")
question = input("Ask the magic 8 ball a question? " + name + ":")
print(random.choice(responses))
while True:
    question = input("Ask the magic 8 ball a question or type x to quit: ")
    if question.strip() == "x":
        break
    print(random.choice(responses))
