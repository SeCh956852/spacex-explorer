from __future__ import annotations
from pickle import FALSE
from re import S
import tkinter as tk
import tkinter.ttk as ttk
import json
from turtle import bgcolor
import managers.logmanager as logmanager
import managers.configmanager as configmanager
import other.genericfuncs as genericfuncs
import gui.app as app
import gui.menubar.menubar as menubar
import gui.menubar.menubarsubitem as menubarsubitem
import gui.menubar.menubarsubitemframe as menubarsubitemframe

class MenubarItem(tk.Label):
    """
    Labels for menu bar at top of window, below title bar
    """
    def __init__(self, parent : menubar.MenuBar, itemName : str, itemInfo : dict) -> None:
        
        # initialize attr
        # related to widget display
        self.unhoveredBackground = "#ffffff"
        self.hoveredBackground = "#c3cceb"
        super().__init__(
            master = parent, 
            text = itemName,
            bg = self.unhoveredBackground
        )
        self.paddingX = 13
        self.paddingY = 7

        # widget meta
        self.itemName = itemName
        self.itemInfo = itemInfo
        self.parent = parent
        self.subItemFrame = menubarsubitemframe.MenubarSubItemFrame(self.parent.parent, self, self.itemInfo)
        self.dontHide = True

        # inital method calls
        # bind events
        self.bindMouseLeftClick()
        self.bindMouseEnter()
        self.bindMouseLeave()

        # display widget
        self.displayWidget()

    def displayWidget(self) -> None:
        self.pack(
            ipadx = self.paddingX,
            ipady = self.paddingY,
            side = tk.LEFT
        )

    def onMouseLeftClick(self) -> None:
        self.subItemFrame.displayWidget(self)

    def bindMouseLeftClick(self) -> None:
        self.bind("<Button-1>", lambda event: self.onMouseLeftClick())

    def onMouseEnter(self) -> None:
        self.config(
            bg = self.hoveredBackground
        )

    def bindMouseEnter(self) -> None:
        self.bind("<Enter>", lambda event: self.onMouseEnter())

    def onMouseLeave(self) -> None:
        self.config(
            bg = self.unhoveredBackground
        )

    def bindMouseLeave(self) -> None:
        self.bind("<Leave>", lambda event: self.onMouseLeave())



