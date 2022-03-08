from __future__ import annotations
import tkinter as tk
import tkinter.ttk as ttk
import json
from turtle import bgcolor
import jsonmanager
import logmanager
import config
import nasarequest


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

        #initial method calls
        #self.overrideredirect(True)
        self.expandFull()
        self.configureTitlebar()
        self.generateMenubar()
        

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
        self.menubar = MenuBar(self)

class MenuBar(tk.Frame):
    """
    Class for menu bar - below title bar
    """
    def __init__(self, parent : App) -> None:
        #initialize attr
        self.background = "#dddddd"
        super().__init__(
            master = parent,
            bg = self.background
        )
        #meta
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
        self.unhoveredBackground = "#dddddd"
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
        self.subItemFrame = MenubarSubItemFrame(self, self.itemInfo)

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
        pass

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
    def __init__(self, parent : MenubarItem, itemInfo : dict):
        #Initialize attr
        super().__init__(
            master = parent
        )
        #meta
        self.itemInfo = itemInfo
        self.subItems = self.generateMenubarSubItems(self.itemInfo)

        #Initial method calls
        

    def displayWidget(self) -> None:
        self.pack(

        )

    def hideWidget(self) -> None:
        self.pack_forget()

    def generateMenubarSubItems(self, itemInfo : dict) -> dict:
        subItems = {}
        for subItemName in itemInfo["SubOrder"]:
            subItems[subItemName] = MenubarSubItem(self, subItemName, itemInfo["SubItems"][subItemName])
        
        return subItems

class MenubarSubItem(tk.Label):
    def __init__(self, parent : MenubarSubItemFrame, subItemName : str, subItemInfo : dict) -> None:
        #init attr
        super().__init__(
            master = parent,
            text = subItemName
        )

        #init method calls

    def displayWidget(self) -> None:
        self.pack(
            
        )

class Section:
    """
    Class for graphical sections in the application
    """
    def __init__(self, sizeX, sizeY) -> None:
        pass




def main():
    root = App()

if __name__ == "__main__":
    main()