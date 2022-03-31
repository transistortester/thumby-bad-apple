from sys import path as syspath
syspath.append("/Games/BadApple") #fix imports

import thumby
import mvf
import audio
from time import sleep_ms
import gc

thumby.display.setFPS(30) #only needed for menu transition
exit = False

def callback():
    audio.fillbufs()
    if thumby.buttonA.justPressed(): mvf.printmem()
    if thumby.buttonB.justPressed():
        audio.stop()
        mvf.stop()

def transition(colour):
    for frame in range(8):
        for x in range(0, 72+40, 8):
            thumby.display.drawLine(x+frame, 0, x+frame-40, 40, colour)
        thumby.display.update()

transition(0)

while not exit:
    vf = open("/Games/BadApple/badapple.mvf", "rb")
    mvf.load(vf)
    af = open("/Games/BadApple/badapple.zdp", "rb")
    audio.load(af)
    if thumby.audio.enabled: audio.play() #respect the audio setting
    mvf.play(callback=callback)
    
    while audio.playing: #allow audio to finish - the audio is slightly longer than the video
        callback()
        sleep_ms(33)
        gc.collect() #necessary for zlib for some reason
    
    transition(0)
    thumby.display.drawText("A: Main menu", 0, 20-8, 1)
    thumby.display.drawText("B: Replay", 9, 20, 1)
    while True:
        thumby.display.update()
        if thumby.buttonA.justPressed():
            exit = True
            break
        if thumby.buttonB.justPressed():
            break
    transition(0)

print("Exiting...")
#sleep_ms(1000)