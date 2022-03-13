from __future__ import annotations
import tkinter as tk
import tkinter.ttk as ttk
from turtle import bgcolor
import jsonmanager
import logmanager
import config
import gui.app as app
import gui.spacex.launches.launches as spacexlaunches



class Section:
    """
    Class for graphical sections in the application
    """
    def __init__(self, sizeX, sizeY) -> None:
        pass

def main():
    root = app.App()
    default = spacexlaunches.SpaceXLaunchesWindow(root)
    root.startEventLoop()

if __name__ == "__main__":
    main()