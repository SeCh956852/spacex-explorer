from __future__ import annotations
import tkinter as tk
import tkinter.ttk as ttk
from turtle import bgcolor
import managers.logmanager as logmanager
import managers.configmanager as configmanager
import gui.app as app
import gui.launches.launcheswindow as spacexlaunches
import traceback


def main():
    try:
        root = app.App()
    except Exception as e:
        print(traceback.format_exc())
        logmanager.writeLogMessage(traceback.format_exc(), logmanager.ERROR_LOG_LOCATION)


if __name__ == "__main__":
    main()