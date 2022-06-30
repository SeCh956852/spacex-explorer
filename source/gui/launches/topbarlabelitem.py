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
import gui.launches.bottomframeitem as bottomframeitem

class TopbarLabelItem(tk.Label):
    def __init__(self, parent : launcheswindow.LaunchesWindow, content : str, location : tuple):
        # init attr
        self.fontSize = 14
        super().__init__(
            master = parent,
            bg = "#efefef",
            text = content,
            font = (None, self.fontSize),
            borderwidth=2,
            relief="groove"
        )

        # meta
        self.parent = parent
        self.columnSpan = 3

        # initial method calls
        self.displayWidget(location[0], location[1])

    def displayWidget(self, rowIndex, columnIndex):
        self.grid(
            row = rowIndex,
            column = columnIndex,
            columnspan = self.columnSpan,
            sticky="NWSE",
        )