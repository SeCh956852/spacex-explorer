from __future__ import annotations
from pickle import FALSE
import tkinter as tk
import tkinter.ttk as ttk
import json
from turtle import bgcolor
import jsonmanager
import logmanager
import config
import nasarequest
import genericfuncs
import gui.app as app

class MenuBar(tk.Frame):
    """
    Class for menu bar - below title bar
    """
    def __init__(self, parent : app.App) -> None:
        #initialize attr
        self.background = "#ffffff"
        super().__init__(
            master = parent,
            bg = self.background
        )
        #meta
        self.parent = parent
        self.MenubarItemsJsonLoc = "./configurations/menubaritems.json"
        self.menubarItems = self.generateMenubarItems()

        #initial method calls
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

        menuItems = jsonmanager.loadJson(self.MenubarItemsJsonLoc)

        menubarItems = {}
        
        for itemName in menuItems["Order"]:
            menubarItems[itemName] = MenubarItem(self, itemName, menuItems["Items"][itemName])

        return menubarItems


class MenubarItem(tk.Label):
    """
    Labels for menu bar at top of window, below title bar
    """
    def __init__(self, parent : MenuBar, itemName : str, itemInfo : dict) -> None:
        
        #initialize attr
        #related to widget display
        self.unhoveredBackground = "#ffffff"
        self.hoveredBackground = "#c3cceb"
        super().__init__(
            master = parent, 
            text = itemName,
            bg = self.unhoveredBackground
        )
        self.paddingX = 13
        self.paddingY = 7

        #widget meta
        self.itemName = itemName
        self.itemInfo = itemInfo
        self.parent = parent
        self.subItemFrame = MenubarSubItemFrame(self.parent.parent, self, self.itemInfo)
        self.dontHide = True

        #inital method calls
        #bind events
        self.bindMouseLeftClick()
        self.bindMouseEnter()
        self.bindMouseLeave()

        #display widget
        self.displayWidget()

    def displayWidget(self) -> None:
        self.pack(
            ipadx = self.paddingX,
            ipady = self.paddingY,
            side = tk.LEFT
        )

    def onMouseLeftClick(self) -> None:
        #print("Called")
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


class MenubarSubItemFrame(tk.Frame):
    """
    Frame to be visible when a menu bar item is clicked
    """
    def __init__(self, master : app.App, parent : MenubarItem, itemInfo : dict):
        #Initialize attr
        self.background = "#ffffff"
        super().__init__(
            master = master,
            bg = self.background
        )
        #meta
        self.parent = parent
        self.itemInfo = itemInfo
        self.subItems = self.generateMenubarSubItems(self.itemInfo)
        self.isHovered = False
        

        #Initial method calls
        self.addToRemoveOnUnfocusedClickList(self.subItems)
        self.bindMouseEnter()
        self.bindMouseLeave()
        
    def addToRemoveOnUnfocusedClickList(self, subItems) -> None:
        listToAdd = [self, self, self.parent]
        listToAdd.extend([subItem for subItem in subItems.values()])
        self.parent.parent.parent.appManager.removeOnUnfocusedClickList.append(listToAdd)

    def onMouseEnter(self) -> None:
        self.isHovered = True

    def bindMouseEnter(self) -> None:
        self.bind("<Enter>", lambda event: self.onMouseEnter())

    def onMouseLeave(self) -> None:
        #print("leaving")
        self.isHovered = False

    def bindMouseLeave(self) -> None:
        self.bind("<Leave>", lambda event: self.onMouseLeave())
        

    def displayWidget(self, relativeTo : MenubarItem) -> None:
        #print("displaying! ")
        self.place(
            in_ = relativeTo,
            bordermode = "outside",
            anchor = tk.NW,
            relx = 0,
            rely = 1.0,
        )

    def hideWidget(self) -> None:
        #print("Hiding")
        self.place_forget()

    def generateMenubarSubItems(self, itemInfo : dict) -> dict:
        subItems = {}
        for subItemName in itemInfo["SubOrder"]:
            subItems[subItemName] = MenubarSubItem(self, subItemName, itemInfo["SubItems"][subItemName])
        
        return subItems

class MenubarSubItem(tk.Label):
    """
    Labels inside frame when a menu bar item is click
    """
    def __init__(self, parent : MenubarSubItemFrame, subItemName : str, subItemInfo : dict) -> None:
        #init attr
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
        
        #meta
        self.parent = parent

        #init method calls
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