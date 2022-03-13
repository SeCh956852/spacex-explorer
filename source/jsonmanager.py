from __future__ import annotations
import typing
import os
import json
import logmanager


def loadJson(loc: str) -> typing.Union[dict, bool]:
    try:
        jsonDict = {}
        with open(loc, "r") as jsonFile:
            jsonString = jsonFile.read()
            jsonDict = json.loads(jsonString)

        return jsonDict
    except FileNotFoundError:
        logmanager.writeLogMessage(f"Error: File at location {os.path.abspath(loc)} not found.")
        return False
    

def writeJson(loc: str, jsonDict : dict) -> bool:
    try:
        with open(loc, "w") as jsonFile:
            jsonString = json.dumps(jsonDict, indent = 4)
            jsonFile.write(jsonString)

        return True
    except FileNotFoundError:
        logmanager.writeLogMessage(f"Error: File at location {os.path.abspath(loc)} not found.")
        return False
        

        
