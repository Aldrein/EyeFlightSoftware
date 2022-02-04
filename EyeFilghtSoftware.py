import tkinter as tk

from tkinter import Canvas, ttk
from pathlib import Path
import CanvasImage as cvImg

appWidth = 1024
appHeight = 600

class MapWindow(ttk.Frame):
    """ Main window class """
    def __init__(self, mainframe, path):
        """ Initialize the main Frame """
        ttk.Frame.__init__(self, master=mainframe)
        self.master.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
        self.master.columnconfigure(0, weight=1)
        canvas = cvImg.CanvasImage(self.master, path, appWidth, appHeight)  # create widget
        canvas.movecenter()
        canvas.grid(row=0, column=0)  # show widget

filename = Path(Path(__file__).parent.resolve(), 'OACI_11_L93_E100.png')
win = tk.Tk()
win.geometry(f'{appWidth}x{appHeight}')
mapFrameRoot = ttk.Frame()
mapFrame = MapWindow(mapFrameRoot, path=filename)
mapFrameRoot.place(x=0, y=0)
b1 = ttk.Button(win, text='Quit', width=10, command=win.destroy)
b1.place(anchor='ne',relx=1.0, rely=0.0)
win.overrideredirect(1) #without borders
#win.wm_attributes('-fullscreen', 'True') #fullscreen

if __name__=='__main__':
    win.mainloop()