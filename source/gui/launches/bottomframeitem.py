from __future__ import annotations
from email.mime import image
import enum
import tkinter as tk
import tkinter.ttk as ttk
from urllib import request
import gui.app as app
import json
import base64
import requests
import gui.launches.launcheswindow as launcheswindow
import gui.launches.bottomframe as bottomframe
import gui.launches.topbarlabelitem as topbarlabelitem


class BottomFrameItem(tk.Label):
    def __init__(self, parent : bottomframe.BottomFrame, contentType : str, content : str, location : tuple):
        # init attr
        if contentType == "text":
            self.fontSize = 14
            super().__init__(
                master = parent,
                text = content,
                font = (None, self.fontSize)
            )

        elif contentType == "image":
            print(content)
            """
            imageWeb = requests.get(content).content
            with open("lol.png", "wb") as f:

            imageWeb = base64.b64encode(imageWeb)
            f.write(imageWeb)

            self.image = tk.PhotoImage(
                format = "PNG",
                file = "lol.png",
            )
            """
            
            super().__init__(
                master = parent,
                #image = self.image
            )

            

        self.parent = parent

        # initial method calls 
        self.displayWidget(location[0], location[1])
        

    def displayWidget(self, rowIndex, rowSpan):
        self.grid(
            row = rowIndex,
            column = 0,
            columnspan = rowSpan
        )