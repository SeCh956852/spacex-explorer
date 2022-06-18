from __future__ import annotations
import requests
import gui.app as app

class NasaRequest:
    """
    Class for api requests to nasa
    """
    def __init__(self, parent : app.App):
        self.parent = parent

    