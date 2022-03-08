from __future__ import annotations
import datetime

LOGFILE_LOCATION = "./logs/log.txt"
TIMESTAMP_FORMAT = "%Y/%m/%d %H:%M:%S";

def writeLogMessage(logMessage : str) -> bool:
    timeNow = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
    logMessage =  timeNow + " : " + logMessage + "\n"
    try:
        with open(LOGFILE_LOCATION, "a") as logFile:
            logFile.write(logMessage)

        return True
    except:
        return False