from __future__ import annotations
import gui.app as app
import json
from asyncio import base_events
import requests

class RequestManager:
    # base url for spacex api
    BASE_URL = "https://api.spacexdata.com"

    # launches urls
    LAUNCHES_URL = f"{BASE_URL}/v5/launches"
    LATEST_LAUNCH_URL = f"{LAUNCHES_URL}/latest"
    NEXT_LAUNCH_URL = f"{LAUNCHES_URL}/next"
    UPCOMING_LAUNCHES_URL = f"{LAUNCHES_URL}/upcoming"

    # launchpad urls
    LAUNCHPAD_URL = f"{BASE_URL}/v4/launchpads"

    # payload urls
    PAYLOAD_URL = f"{BASE_URL}/v4/payloads"


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

    def getPayloadByID(self, id) -> str:
        return self.getRequest(f"{self.PAYLOAD_URL}/{id}")

    def getLaunchpadByID(self, id) -> str:
        return self.getRequest(f"{self.LAUNCHPAD_URL}/{id}")

    
    