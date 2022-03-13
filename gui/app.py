from __future__ import annotations
import tkinter as tk
import tkinter.ttk as ttk
import json
from turtle import bgcolor
import jsonmanager
import logmanager
import config
import genericfuncs
import gui.menubar as menubar
import gui.custappmanager as custappmanager

class App(tk.Tk):
    """
    Class for the graphical user interface
    """
    def __init__(self) -> None:
        
        #initalize attributes
        super().__init__()

        #meta
        self.windowTitle = "NEOViewer"
        self.favicon = "./images/fav.ico"
        self.appManager = custappmanager.CustomApplicationManager(self)

        #initial method calls
        #self.overrideredirect(True)
        self.expandFull()
        self.configureTitlebar()
        self.generateMenubar()
        self.bindMouseLeftClick()


    def startEventLoop(self):
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
        self.appManager.checkRemoveOnUnfocusedClick(event)

        """
        object_methods = [method_name for method_name in dir(event)
                  if not callable(getattr(event, method_name))]
        for attrName in object_methods:
            print(f"{attrName} : {getattr(event, attrName)}")
        """


        

    def bindMouseLeftClick(self) -> None:
        self.bind("<Button-1>", lambda event: self.onMouseLeftClick(event))