import engine_main
import engine
import engine_io
from engine_resources import FontResource
from engine_nodes import Text2DNode, CameraNode
from engine_math import Vector2

from sys import path as syspath
syspath.insert(0, "/Games/BadApple/")
import mvf
import audio
import gc
from os import stat
from time import sleep_ms

videopath = "/Games/BadApple/badapple-128x96.mvf"
audiopath = "/Games/BadApple/badapple-15625Hz-EQ.ima"
audiorate = 15625

camera = CameraNode()

def callback():
    audio.fillbufs()
    if engine_io.A.is_just_pressed: mvf.printmem()
    if engine_io.B.is_just_pressed:
        audio.stop()
        mvf.stop()
    if engine_io.RB.is_just_pressed:
        fps.toggle()
    if engine_io.LB.is_just_pressed:
        mvf.capframerate = False

font = FontResource("/Games/BadApple/Portfolio6x8.bmp")
class FPStext(Text2DNode):
    def __init__(self):
        super().__init__(self)
        self.font = font
        self.visible = False
        self.opacity = 0
        self.position = Vector2(0,-59)
        self.frame = 0
        self.total = 0
        self.windowsize = 5
    
    def tick(self, dt):
        if self.opacity > 0:
            if self.frame == self.windowsize:
                self.text = f"{self.total / self.windowsize} FPS"
                self.frame = 0
                self.total = 0
            self.frame += 1
            self.total += engine.get_running_fps()
    
    def toggle(self):
        if self.visible:
            self.opacity = 0
        else:
            self.opacity = 1
        self.visible = not self.visible

fps = FPStext()

vf = open(videopath, "rb")
mvf.load(vf)
af = open(audiopath, "rb")
audiosamples = stat(audiopath)[6] * 2 #sample count is filesize * 2
audio.load(af, audiorate, audiosamples) #raw IMA files don't contain any metadata, so sample rate and sample count have to be specified
audio.play()
mvf.play(callback=callback)

while audio.playing: #allow audio to finish if the audio is longer than the video
    callback()
    sleep_ms(33)
    gc.collect()


print("Exiting...")