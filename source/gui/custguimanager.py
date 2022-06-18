from __future__ import annotations
import tkinter as tk
import tkinter.ttk as ttk
import json
from turtle import bgcolor
import managers.jsonmanager as jsonmanager
import managers.logmanager as logmanager
import managers.configmanager as configmanager
import network.nasarequest as nasarequest
import other.genericfuncs as genericfuncs
import gui.menubar as menubar
import gui.app as app

class CustomGuiManager:
    """
    Manages the state of the application or gui
    including:
    - events
    - widgets
    """
    def __init__(self, app : app.App):
        #Init attr
        #Widgets that should be removed when the mouse clicks anywhere in the window except on the widgets specified in the white list
        #List containing a list of whitelisted objects, first object of the inner list is the element to remove is unfocused click
        self.removeOnUnfocusedClickList = [] 

    def removeOnUnfocusedClick(self, event : tk.Event):
        for whiteList in self.removeOnUnfocusedClickList:
            if event.widget not in whiteList:
                whiteList[0].hideWidget()


        
        