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
import gui.menubar.menubaritem as menubaritem
import gui.menubar.menubarsubitem as menubarsubitem
import gui.menubar.menubar as menubar

class MenubarSubItemFrame(tk.Frame):
    """
    Frame to be visible when a menu bar item is clicked
    """
    def __init__(self, master : app.App, parent : menubaritem.MenubarItem, itemInfo : dict):
        # Initialize attr
        self.background = "#ffffff"
        super().__init__(
            master = master,
            bg = self.background
        )
        #meta
        self.parent = parent
        self.itemInfo = itemInfo
        self.subItems = self.generateMenubarSubItems(self.itemInfo)
        

        # Initial method calls
        self.addToRemoveOnUnfocusedClickList(self.subItems)
        
    def addToRemoveOnUnfocusedClickList(self, subItems) -> None:
        listToAdd = [self, self, self.parent]
        listToAdd.extend([subItem for subItem in subItems.values()])
        self.parent.parent.parent.appManager.removeOnUnfocusedClickList.append(listToAdd)

    def displayWidget(self, relativeTo : menubaritem.MenubarItem) -> None:
        self.place(
            in_ = relativeTo,
            bordermode = "outside",
            anchor = tk.NW,
            relx = 0,
            rely = 1.0,
        )
        self.lift()

    def hideWidget(self) -> None:
        self.place_forget()

    def generateMenubarSubItems(self, itemInfo : dict) -> dict:
        subItems = {}
        for subItemName in itemInfo["SubOrder"]:
            subItems[subItemName] = menubarsubitem.MenubarSubItem(self, subItemName, itemInfo["SubItems"][subItemName])
        
        return subItems
