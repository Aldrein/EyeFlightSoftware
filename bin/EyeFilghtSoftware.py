import tkinter as tk
from pathlib import Path
import CanvasImage as cvImg

# Window size and position variables
appWidth = 1024
appHeight = 600
appOffsetX = 250
appOffsetY = 100

# Project path
projectPath = Path(__file__).parents[1].resolve()
print(projectPath)

class MapWindow(tk.Frame):
    """ Main window class """
    def __init__(self, mainframe, path, planePath):
        """ Initialize the main Frame """
        tk.Frame.__init__(self, master=mainframe)
        self.master.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
        self.master.columnconfigure(0, weight=1)
        self.canvas = cvImg.CanvasImage(self.master, path, planePath, appWidth, appHeight)  # create widget
        self.canvas.movecenter()
        self.canvas.drawPlane(3500, 3500, 0)
        self.canvas.grid(row=0, column=0)  # show widget

class EyeFlight(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        filename = Path(projectPath, 'img//OACI_11_L93_E100.png')
        planePath = Path(projectPath, 'img//aircraft.png')
        mapFrameRoot = tk.Frame(master=self.parent)
        self.mapFrame = MapWindow(mapFrameRoot, path=filename, planePath=planePath)
        mapFrameRoot.place(x=0, y=0)
        self.buttonFrame = tk.Frame(master=self.parent)
        self.buttonFrame.place(x=0, y=0)
        self.__buttonPlacement()

    def __buttonPlacement(self):
        # Top Menu
        quitButton = tk.Button(self.parent, text='Quit', command=self.parent.destroy)
        quitButton.place(anchor='ne', relx=1.0, rely=0.0, relwidth=.03, relheight=.04)
        weatherButton = tk.Button(self.parent, text='Météo')
        weatherButton.place(anchor='n', relx=0.2, rely=0.0, relwidth=.08, relheight=.1)
        docButton = tk.Button(self.parent, text='Documents')
        docButton.place(anchor='n', relx=0.35, rely=0.0, relwidth=.08, relheight=.1)
        navigationButton = tk.Button(self.parent, text='Navigation')
        navigationButton.place(anchor='n', relx=0.5, rely=0.0, relwidth=.08, relheight=.1)
        historyButton = tk.Button(self.parent, text='Historique')
        historyButton.place(anchor='n', relx=0.65, rely=0.0, relwidth=.08, relheight=.1)
        parameterButton = tk.Button(self.parent, text='Paramètres')
        parameterButton.place(anchor='n', relx=0.8, rely=0.0, relwidth=.08, relheight=.1)

        # Side Menu
        mapBackgroundButton = tk.Button(self.parent, text='Fond de carte')
        mapBackgroundButton.place(anchor='e', relx=1.0, rely=.3, relwidth=.08, relheight=.1)
        trafficButton = tk.Button(self.parent, text='Traffic', command=self.testPlane)
        trafficButton.place(anchor='e', relx=1.0, rely=.4, relwidth=.08, relheight=.1)
        centerButton = tk.Button(self.parent, text='Centrer', command=self.mapFrame.canvas.centerOnPlane)
        centerButton.place(anchor='e', relx=1.0, rely=.5, relwidth=.08, relheight=.1)
        northUpButton = tk.Button(self.parent, text='Nord en haut')
        northUpButton.place(anchor='e', relx=1.0, rely=.6, relwidth=.08, relheight=.1)
        displayButton = tk.Button(self.parent, text='Affichages')
        displayButton.place(anchor='e', relx=1.0, rely=.7, relwidth=.08, relheight=.1)

    def testPlane(self):
        self.mapFrame.canvas.drawPlane(2000, 2000, 0)

if __name__=='__main__':
    win = tk.Tk()
    win.geometry(f'{appWidth}x{appHeight}+{appOffsetX}+{appOffsetY}')
    win.title('EyeFlightSoftware')
    win.configure(bg='black')
    #win.overrideredirect(1) #without borders
    #win.wm_attributes('-fullscreen', 'True') #fullscreen
    EyeFlight(win).pack(side='top', fill='both', expand=True)
    win.mainloop()