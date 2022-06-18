from __future__ import annotations
import tkinter as tk
import tkinter.ttk as ttk
import gui.app as app
import managers.jsonmanager as jsonmanager

class SpaceXLaunchesWindow(tk.Frame):
    def __init__(self, parent : app.App, launchId : str):
        #init attr
        self.background = "#efefef"
        super().__init__(
            master = parent,
            bg = self.background
        )

        #meta
        self.parent = parent
        self.topbarItemsLoc = "./configurations/gui/spacex/launches/topbaritems.json"
        self.topbarItems = jsonmanager.loadJson(self.topbarItemsLoc)
        self.launchId = launchId
        self.launchIdName = "id"
        self.data = self.getAssociatedData()
        self.childWidgets = []

        #initial method calls
        self.displayWidget()

    def displayWidget(self):
        self.pack(
            fill = tk.BOTH,
            expand = True
        )

    def getAssociatedData(self):
        requestManager = self.parent.requestManager
        self.data = requestManager.requestSpaceX.getLatestLaunch()


    def generateChildWidgets(self):
        content = self.data

        for number, contentDict in self.topbarItems:
            self.topbarItems.append(TopbarLabelItem(self, 1))

class TopbarLabelItem(tk.Label):
    def __init__(self, parent : SpaceXLaunchesWindow, content : str):
        #init attr
        super().__init__(
            master = parent,
            bg = "#eeeeee",
            text = content
        )

        #meta
        self.parent = parent
        self.displayWidget(self)

    def displayWidget(self):
        self.grid(
            row = 0,
            column = 0,
        )

    def generateContent(self):
        name = self.contentDict["Name"]
        dataIdentifier = self.contentDict["Data"]

        

        self.config(
             
        ) 

