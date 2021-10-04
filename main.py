import pygame
from pygame import mixer
from tkinter import *
from tkinter import filedialog

class MusicPlayer:

    def __init__(self, window ):
        self.window = window
        self.window.geometry('320x100');
        self.window.title('IMplayer');
        self.window.resizable(0,0)

        Load = Button(window, text = 'Load' , width = 10,font = ('Times',10),command = self.load)
        Play = Button(window, text = 'play', width = 10, font = ('Times',10), command =self.play)
        Pause = Button(window, text='pause', width=10, font=('Times', 10), command=self.pause)
        stop = Button(window, text='stop', width=10, font=('Times', 10), command=self.stop)
        Load.place(x=00,y=20)
        Play.place(x=110,y=20)
        Pause.place(x=220,y=20)
        stop.place(x=110,y=60)
        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state=False
    def stop(self):
        mixer.music.stop()
root = Tk()
MusicPlayer(root)
root.mainloop()