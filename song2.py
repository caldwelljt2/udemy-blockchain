import pyttsx3

engine = pyttsx3.init()

lyrics = [
    "Mary had a little lamb,",
    "Its fleece was white as snow,",
    "And everywhere that Mary went,",
    "The lamb was sure to go."
]

# Set the rate and pitch of the voice
rate = 150
pitch = 100
engine.setProperty('rate', rate)
engine.setProperty('pitch', pitch)

# Set the melody for the first line
engine.setProperty('voice', 'english-us+f2')
engine.say(lyrics[0])

# Set the melody for the second line
engine.setProperty('voice', 'english-us+f3')
engine.say(lyrics[1])

# Set the melody for the third line
engine.setProperty('voice', 'english-us+f4')
engine.say(lyrics[2])

# Set the melody for the fourth line
engine.setProperty('voice', 'english-us+f5')
engine.say(lyrics[3])

engine.runAndWait()