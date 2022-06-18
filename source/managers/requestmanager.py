from __future__ import annotations
import gui.app as app
from network.nasarequest import NasaRequest
from network.spacexrequest import SpaceXRequest
import json

class RequestManager:
    def __init__(self, parent : app.App):
        self.parent = parent
        self.requestSpaceX = SpaceXRequest(self)
        self.requestNasa = NasaRequest(self)

    
    