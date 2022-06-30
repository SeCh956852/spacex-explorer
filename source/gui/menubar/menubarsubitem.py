from __future__ import annotations
from pickle import FALSE
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

class MenubarSubItem(tk.Label):
    """
    Labels inside frame when a menu bar item is click
    """
    def __init__(self, parent : menubar.MenubarSubItemFrame, subItemName : str, subItemInfo : dict) -> None:
        # init attr
        self.paddingX = 40
        self.paddingY = 3
        self.unhoveredBackground = "#ffffff"
        self.hoveredBackground = "#c3cceb"
        super().__init__(
            master = parent,
            text = genericfuncs.addStringPaddingBefore(subItemName, 8),
            anchor = tk.W,
            bg = self.unhoveredBackground
        )
        
        # meta
        self.parent = parent

        # init method calls
        self.displayWidget()
        self.bindMouseEnter()
        self.bindMouseLeave()
        

    def displayWidget(self) -> None:
        self.pack(
            fill = tk.X,
            expand = True,
            ipadx = self.paddingX,
            ipady = self.paddingY
        )
    
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