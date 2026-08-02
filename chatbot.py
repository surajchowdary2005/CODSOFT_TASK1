from datetime import datetime
import random

# List of jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Python is fun to learn!"
]

print("=" * 50)
print("        🤖 RULE-BASED CHATBOT")
print("=" * 50)
print("Type 'bye' to exit the chatbot.\n")

while True:

    user = input("You: ").lower().strip()

    if user == "hi" or user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is RuleBot.")

    elif user == "who created you":
        print("Bot: I was created by Suraj using Python.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions, tell time, date and jokes.")

    elif user == "time":
        print("Bot:", datetime.now().strftime("%I:%M %p"))

    elif user == "date":
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "good morning":
        print("Bot: Good Morning! Have a wonderful day.")

    elif user == "good night":
        print("Bot: Good Night! Sweet dreams.")

    elif user == "help":
        print("Bot: Try these commands:")
        print("- hi")
        print("- hello")
        print("- how are you")
        print("- what is your name")
        print("- who created you")
        print("- what can you do")
        print("- time")
        print("- date")
        print("- joke")
        print("- bye")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")