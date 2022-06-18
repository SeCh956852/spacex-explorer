from __future__ import annotations
import datetime

BASE_FOLDER_LOCATION = "./logs/"
LOG_LOCATION = f"{BASE_FOLDER_LOCATION}log.txt"
ERROR_LOG_LOCATION = f"{BASE_FOLDER_LOCATION}errorlog.txt"
REQUEST_LOG_LOCATION = f"{BASE_FOLDER_LOCATION}requestlog.txt"
TIMESTAMP_FORMAT = "%Y/%m/%d %H:%M:%S"

def writeLogMessage(logMessage : str, fileLocation : str) -> bool:
    timeNow = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
    logMessage =  timeNow + " : " + logMessage + "\n"
    try:
        with open(fileLocation, "a") as logFile:
            logFile.write(logMessage)
        return True
    except:
        return False