from __future__ import annotations
import tkinter as tk
import tkinter.ttk as ttk
import gui.app as app

class SpaceXLaunchesWindow(tk.Frame):
    def __init__(self, parent : app.App):
        #init attr
        self.background = "#efefef"
        super().__init__(
            master = parent,
            bg = self.background
        )

        #meta
        self.parent = parent

        #initial method calls
        self.displayWidget()

    def displayWidget(self):
        self.pack(
            fill = tk.BOTH,
            expand = True
        )