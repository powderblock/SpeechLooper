# Say anything you type, and write anything you say.
# Stops when you say "turn off" or type "turn off".

import speech
import sys
import time

lemon = "lemon"
output = []
current_run = []

waiting = False
hasDetect = False

print "Say something."

def callback(phrase, listener):
    speech.say(phrase)
    print phrase
    lemon = str(phrase)
    hasDetect = True
    waiting = False

listener = speech.listenforanything(callback)

while listener.islistening():
    if not waiting and not hasDetect:
        waiting = True
        speech.say(lemon)
