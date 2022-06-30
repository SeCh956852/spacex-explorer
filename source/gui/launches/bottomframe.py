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
import gui.launches.topbarlabelitem as topbarlabelitem
import gui.launches.bottomframeitem as bottomframeitem


class BottomFrame(tk.Frame):
    def __init__(self, parent : launcheswindow.LaunchesWindow, title : str, content : dict, data : dict, location : tuple):
        
        # init attr
        super().__init__(
            master = parent,
            borderwidth=2,
            relief="groove"
        )

        # meta
        self.rowSpan = 9
        self.columnSpan = 3

        self.rows = 1
        self.columns = 8

        self.parent = parent

        self.content = content
        self.data = data
        self.title = title

        self.childWidgets = []

        # initial method calls
        self.configureGrid()
        self.generateChildWidgets()
        self.displayWidget(location[0], location[1])

    def displayWidget(self, rowIndex, columnIndex):
        self.grid(
            row = rowIndex,
            column = columnIndex,
            columnspan = self.columnSpan,
            rowspan = self.rowSpan,
            sticky="NESW"
        )


    def generateChildWidgets(self):
        titleLocation = (0, 1) # location in the form (row index, row span)
        self.childWidgets.append(bottomframeitem.BottomFrameItem(self, "text", self.title, titleLocation))

        rowCount = 1
        for i, obj in enumerate(self.content):
            rowSpan = obj["RowSpan"]
            contentType = obj["ContentType"]
            content = ""
            location = (rowCount, rowSpan)

            label = obj["Label"]
            if contentType == "text":
                content = f"{obj['Name']}: {self.data[label]}"
            elif contentType == "image":
                content = self.data[label[0]][label[1]][0]

            self.childWidgets.append(bottomframeitem.BottomFrameItem(self, contentType, content, location))
            rowCount += rowSpan


    def configureGrid(self):
        for i in range(self.rows):
            self.columnconfigure(i, weight=1)

        for i in range(self.columns):
            self.rowconfigure(i, weight=1) 


