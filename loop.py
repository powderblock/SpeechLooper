# Say anything you type, and write anything you say.
# Stops when you say "turn off" or type "turn off".

import speech
import sys

inputs = ["hi", "foo", "lemon", "hello world"]
output = []
current_run = []

def callback(phrase, listener):
    speech.say(phrase)
    if phrase == "turn off":
        speech.say("Goodbye.")
        listener.stoplistening()
        sys.exit()

print "Anything you type, speech will say back."
print "Anything you say, speech will print out."
print "Say or type 'turn off' to quit."
print

listener = speech.listenforanything(callback)

while listener.islistening():
    for i in range(0, len(inputs)):
        speech.say(str(inputs[i]))

    text = raw_input("> ")
    if text == "turn off":
        listener.stoplistening()
        sys.exit()
    else:
        speech.say(text)
