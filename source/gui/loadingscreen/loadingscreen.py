from __future__ import annotations
import tkinter as tk
import gui.app as app
from time import sleep

class LoadingScreen(tk.Frame):
    def __init__(self, parent : app.App):
        super().__init__(
            master = parent,
            bg = "#000000"
        )
        #meta
        self.loadingGifLocation = "./images/loadingscreen/loadinganimation.gif"
        self.loadingGif = LoadingGif(self, self.loadingGifLocation)
        self.parent = parent
        self.displayWidget()

        self.bind("<Button-1>", self.test)
        """
        self.parent.update()
        print(self.winfo_width())
        print(self.winfo_height())
        """

    def test(self, event):
        print("clicked")
        

    def displayWidget(self):
        self.pack(
            expand = True,
            fill = tk.BOTH
        )
        

class LoadingGif(tk.Label):
    def __init__(self, parent : LoadingScreen, loadingGifLocation : str):
        super().__init__(
            master = parent,
            bg = "#eeeeee"
        )
        self.parent = parent
        self.loadingGifLocation = loadingGifLocation
        self.loadingGif = None
        self.loadingGifFrames = 29
        self.loadingGifRefreshRate = int(0.01 * 1000)
        
        self.displayWidget()

    def displayWidget(self):
        self.pack(
            expand = True,
            fill = tk.BOTH
        )

    def configGif(self, frameNumber : int):
        print("running :", frameNumber)
        self.loadingGif = tk.PhotoImage(
            file = self.loadingGifLocation,
            format = f"gif -index {frameNumber}"
        )
        self.config(
            image = self.loadingGif
        )
        self.displayWidget()

    
    def runGif(self, currentFrameCount : int):
        currentFrameCount = currentFrameCount if currentFrameCount < 29 else 0
        self.configGif(currentFrameCount)
        self.parent.parent.after(self.loadingGifRefreshRate, lambda : self.runGif(currentFrameCount + 1))
        
