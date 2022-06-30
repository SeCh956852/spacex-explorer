from __future__ import annotations
import tkinter as tk
import tkinter.ttk as ttk
import json
from turtle import bgcolor
import managers.logmanager as logmanager
from managers.configmanager import ConfigManager
from managers.requestmanager import RequestManager
import other.genericfuncs as genericfuncs
import gui.menubar.menubar as menubar
from managers.custguimanager import CustomGuiManager
from gui.launches.launcheswindow import LaunchesWindow


class App(tk.Tk):
    """
    Class for the graphical user interface
    """
    def __init__(self) -> None:
        
        # initalize attributes
        super().__init__()

        # meta
        self.windowTitle = "NEOViewer"
        self.favicon = "./images/fav.ico"
        self.appManager = CustomGuiManager(self)
        self.requestManager = RequestManager(self)
        self.currentWindow = None

        # initial method calls
        self.bindMouseLeftClick()
        self.expandFull()
        self.configureTitlebar()
        self.load()
            

    def start(self):
        print("main loop running")
        self.mainloop()
        

    def expandFull(self) -> None:
        """
        Expand window size to max
        """
        self.state("zoomed")

    def configureTitlebar(self) -> None:
        """
        Configurations for the title bar of the window
        """
        self.iconbitmap(self.favicon)
        self.title(self.windowTitle)

    def generateMenubar(self) -> None:
        """
        Generate menubar at top of the window, below the title bar
        """
        self.menubar = menubar.MenuBar(self)

    def onMouseLeftClick(self, event) -> None:
        self.appManager.removeOnUnfocusedClick(event)

    def bindMouseLeftClick(self) -> None:
        self.bind("<Button-1>", lambda event: self.onMouseLeftClick(event))

    def load(self) -> None:
        """
        Initiate widgets
        """
        self.generateMenubar()
        self.createDefaultWindow()
        self.start()

    def createDefaultWindow(self) -> None:
        """
        Default window is set to the spacex launch window
        Default launch is the latest launc
        """
        defaultID = "latest"
        self.currentWindow = LaunchesWindow(self, defaultID)

    def changeWindow(self, windowClass : tk.Frame) -> None:
        self.currentWindow.destroy()
        self.currentWindow = windowClass(self)