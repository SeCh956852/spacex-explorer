from __future__ import annotations
import tkinter as tk
import tkinter.ttk as ttk
import json
import config
import nasarequest


class App(tk.Tk):
    """
    Class for the graphical user interface
    """
    def __init__(self) -> None:
        #initalize attributes
        super().__init__()
        self.windowTitle = "NEOViewer"
        self.favicon = "./images/fav.ico"

        #initial method calls
        #self.overrideredirect(True)
        self.configureTitlebar()
        self.expandFull()

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
        self.menubar = MenuBar(master = self, fill = tk.X)

class MenuBar(ttk.Frame):
    """
    Class for custom menu bar
    """
    def __init__(self, master, fill) -> None:
        #initialize attr
        super().__init__(master = master)
        self.MenubarItemsJson = "./configurations/menubaritems.json"

        #initial method calls
        self.generateMenubarItems()
        
        self.pack(fill = fill)

    def generateMenubarItems(self):
        """
        Generate manu bar items
        file, edit, view, tools, settings, help
        """

        menuItems = json.loads(self.MenubarItemsJson)
        print(json.dumps(menuItems, indent=4))

class MenuBarItem(ttk.Label):
    pass

class Section:
    """
    Class for graphical sections in the application
    """
    def __init__(self, sizeX, sizeY):
        pass



def main():
    root = App()

if __name__ == "__main__":
    main()