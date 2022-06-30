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
import gui.launches.topbarlabelitem as topbarlabelitem
import gui.launches.bottomframe as bottomframe
import gui.launches.bottomframeitem as bottomframeitem


class LaunchesWindow(tk.Frame):
    def __init__(self, parent : app.App, launchId : str):
        # init attr
        self.background = "#efefef"
        super().__init__(
            master = parent,
            bg = self.background
        )

        # meta
        self.parent = parent
        self.topbarItemsLoc = "./configurations/gui/launches/topbaritems.json"
        self.bottomItemsLoc = "./configurations/gui/launches/bottomitems.json"

        jsonFile = open(self.topbarItemsLoc)
        self.topbarItems = json.load(jsonFile)
        jsonFile.close()

        jsonFile = open(self.bottomItemsLoc)
        self.bottomItems = json.load(jsonFile)
        jsonFile.close()

        self.topbarItemsGridMap = {
            0 : (0, 0),
            3 : (0, 3),
            1 : (1, 0),
            4 : (1, 3),
            2 : (2, 0),
            5 : (2, 3)
        }

        self.bottomItemsGridMap = {
            0 : (3, 0),
            1 : (3, 3)
        }

        self.launchId = launchId
        self.launchIdName = "id"
        self.childWidgets = []

        self.rows = 12
        self.columns = 6

        # initial method calls
        self.getAssociatedData()
        self.configureGrid()
        self.generateChildWidgets()
        self.displayWidget()

    def displayWidget(self):
        self.pack(
            fill = tk.BOTH,
            expand = True
        )

    def getAssociatedData(self):
        requestManager = self.parent.requestManager
        self.launchData = json.loads(requestManager.getLatestLaunch())

        payloadID = self.launchData["payloads"][0]
        launchpadID = self.launchData["launchpad"]

        self.payloadData = json.loads(requestManager.getPayloadByID(payloadID))
        self.launchpadData = json.loads(requestManager.getLaunchpadByID(launchpadID))

        self.dataMapper = {
            "Payload Details" : self.payloadData,
            "Launch Pad Details" : self.launchpadData
        }

    def generateChildWidgets(self):
        
        # generate labels located at the top of the screen
        for i, obj in enumerate(self.topbarItems):
            content = ""
            name = obj["Name"]
            label = obj["Data"]

            if name == "Status":
                if self.launchData["upcoming"]:
                    content = "Upcoming"
                elif self.launchData["success"]:
                    content = "Success"
                else:
                    content = "Fail"

            else:
                content = self.launchData[label]
        
            content = f"{name}: {content}"

            location = self.topbarItemsGridMap[i]    

            self.childWidgets.append(topbarlabelitem.TopbarLabelItem(self, content, location))    

        # generate bottom frames
        for i, obj in enumerate(self.bottomItems):
            title = obj["Type"]
            content = obj["Content"]
            location = self.bottomItemsGridMap[i]
            data = self.dataMapper[title]
            
            self.childWidgets.append(bottomframe.BottomFrame(self, title, content, data, location))


    def configureGrid(self):
        for i in range(self.columns):
            self.columnconfigure(i, weight=1)

        for i in range(self.rows):
            self.rowconfigure(i, weight=1) 





