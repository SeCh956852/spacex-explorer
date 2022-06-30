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
import gui.menubar.menubarsubitemframe as menubarsubitemframe

class MenuBar(tk.Frame):
    """
    Class for menu bar - below title bar
    """
    def __init__(self, parent : app.App) -> None:
        # initialize attr
        self.background = "#ffffff"
        super().__init__(
            master = parent,
            bg = self.background
        )
        # meta
        self.parent = parent
        self.MenubarItemsJsonLoc = "./configurations/gui/menubaritems.json"
        self.menubarItems = self.generateMenubarItems()

        # initial method calls
        self.displayWidget()
        

    def displayWidget(self):
        self.pack(
            fill = tk.X
        )

    def generateMenubarItems(self) -> dict:
        """
        Generate manu bar items
        file, edit, view, tools, settings, help
        """
        jsonFile = open(self.MenubarItemsJsonLoc)
        menuItems = json.load(jsonFile)
        jsonFile.close()

        menubarItems = {}
        
        for itemName in menuItems["Order"]:
            menubarItems[itemName] = menubaritem.MenubarItem(self, itemName, menuItems["Items"][itemName])

        return menubarItems


