#Challenge 026 - The Power of Libraries in Games
from replit import audio
import os, time

def play():
    source = audio.play_file('audio.wav')
    source.paused = False
    while True:
        stop_audio = int(input("Press 2 anytime to stop the audio: "))
        if stop_audio == 2:
            source.paused = True
            return
        else:
            continue

while True:
    os.system("clear")
    print("My Music Player")
    time.sleep(1)
    print("1. Play")
    print("2. Exit")
    song = int(input())
    if song == 1:
        play()
    elif song == 2:
        exit()
    else:
        print("That's not a valid option.")
        time.sleep(3)