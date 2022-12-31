import pyttsx3

engine = pyttsx3.init()

lyrics = [
    "Mary had a little lamb,",
    "Its fleece was white as snow,",
    "And everywhere that Mary went,",
    "The lamb was sure to go."
]

for line in lyrics:
    engine.say(line)

engine.runAndWait()