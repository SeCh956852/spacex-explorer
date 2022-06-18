from __future__ import annotations
from asyncio import base_events
import requests
import asyncio
import json
import gui.app as app


class SpaceXRequest:
    #Base url for spacex api
    BASE_URL = "https://api.spacexdata.com"

    #Launches urls
    LAUNCHES_URL = f"{BASE_URL}/v5/launches"
    LATEST_LAUNCH_URL = f"{LAUNCHES_URL}/latest"
    NEXT_LAUNCH_URL = f"{LAUNCHES_URL}/next"
    UPCOMING_LAUNCHES_URL = f"{LAUNCHES_URL}/upcoming"

    def __init__(self, parent : app.App):
        self.parent = parent      

    def getRequest(self, requestUrl) -> str:
        httpObj = requests.get(requestUrl)
        return httpObj.text

    def getAllLaunches(self) -> str:
        return self.getRequest(self.LAUNCHES_URL)

    def getLatestLaunch(self) -> str:
        return self.getRequest(self.LATEST_LAUNCH_URL)

    def getLaunchByID(self, id) -> str:
        return self.getRequest(f"{self.LATEST_LAUNCH_URL}/{id}")