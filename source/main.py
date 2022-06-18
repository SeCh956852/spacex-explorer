from __future__ import annotations
import tkinter as tk
import tkinter.ttk as ttk
from turtle import bgcolor
import managers.jsonmanager as jsonmanager
import managers.logmanager as logmanager
import managers.configmanager as configmanager
import gui.app as app
import gui.spacex.launches.launches as spacexlaunches
import traceback


def main():
    try:
        root = app.App()
    except Exception as e:
        logmanager.writeLogMessage(traceback.format_exc(), logmanager.ERROR_LOG_LOCATION)


if __name__ == "__main__":
    main()