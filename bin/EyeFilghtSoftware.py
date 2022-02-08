import time
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
    def __init__(self, mainframe: tk.Frame, path: Path, planePath: Path):
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
        self.UIFrame = tk.Frame(master=self.parent)
        self.UIFrame.place(x=0, y=0)
        self.__createUI()

    def __createUI(self):
        self.__buttonPlacement()

    def __buttonPlacement(self):
        #Icons setup
        weatherIcon = tk.PhotoImage(file = 'img//icons//weather.png')
        docIcon = tk.PhotoImage(file = 'img//icons//doc.png')
        navigationIcon = tk.PhotoImage(file = 'img//icons//navigation.png')
        historyIcon = tk.PhotoImage(file = 'img//icons//history.png')
        parametersIcon = tk.PhotoImage(file = 'img//icons//parameters.png')
        mapBackgroundIcon = tk.PhotoImage(file = 'img//icons//mapBackground.png')
        trafficIcon = tk.PhotoImage(file = 'img//icons//traffic.png')
        centerIcon = tk.PhotoImage(file = 'img//icons//center.png')
        northUpIcon = tk.PhotoImage(file = 'img//icons//northUp.png')
        displayIcon = tk.PhotoImage(file = 'img//icons//display.png')

        # Top Menu
        quitButton = tk.Button(self.parent, text='Quit', command=self.parent.destroy)
        quitButton.place(anchor='ne', relx=1.0, rely=0.0, relwidth=.03, relheight=.04)
        weatherButton = tk.Button(self.parent, text='Météo', image=weatherIcon)
        weatherButton.place(anchor='n', relx=0.2, rely=0.0, relwidth=.08, relheight=.1)
        weatherButton.icon = weatherIcon
        docButton = tk.Button(self.parent, text='Documents', image=docIcon)
        docButton.place(anchor='n', relx=0.35, rely=0.0, relwidth=.08, relheight=.1)
        docButton.icon = docIcon
        navigationButton = tk.Button(self.parent, text='Navigation', image=navigationIcon)
        navigationButton.place(anchor='n', relx=0.5, rely=0.0, relwidth=.08, relheight=.1)
        navigationButton.icon = navigationIcon
        historyButton = tk.Button(self.parent, text='Historique', image=historyIcon)
        historyButton.place(anchor='n', relx=0.65, rely=0.0, relwidth=.08, relheight=.1)
        historyButton.icon = historyIcon
        parametersButton = tk.Button(self.parent, text='Paramètres', image=parametersIcon)
        parametersButton.place(anchor='n', relx=0.8, rely=0.0, relwidth=.08, relheight=.1)
        parametersButton.icon = parametersIcon

        # Side Menu
        mapBackgroundButton = tk.Button(self.parent, text='Fond de carte', image=mapBackgroundIcon)
        mapBackgroundButton.place(anchor='e', relx=1.0, rely=.3, relwidth=.08, relheight=.1)
        mapBackgroundButton.icon = mapBackgroundIcon
        trafficButton = tk.Button(self.parent, text='Traffic', image=trafficIcon)
        trafficButton.place(anchor='e', relx=1.0, rely=.4, relwidth=.08, relheight=.1)
        trafficButton.icon = trafficIcon
        centerButton = tk.Button(self.parent, text='Centrer', image=centerIcon, command=self.mapFrame.canvas.centerOnPlane)
        centerButton.place(anchor='e', relx=1.0, rely=.5, relwidth=.08, relheight=.1)
        centerButton.icon = centerIcon
        northUpButton = tk.Button(self.parent, text='Nord en haut', image=northUpIcon)
        northUpButton.place(anchor='e', relx=1.0, rely=.6, relwidth=.08, relheight=.1)
        northUpButton.icon = northUpIcon
        displayButton = tk.Button(self.parent, text='Affichages', image=displayIcon)
        displayButton.place(anchor='e', relx=1.0, rely=.7, relwidth=.08, relheight=.1)
        displayButton.icon = displayIcon


def loop():
    """ Main program loop running alongside Tkinter mainloop """
    currentTime = time.strftime('%H:%M:%S - %d/%m/%Y')
    win.title(f'EyeFlightSoftware {currentTime}')
    win.after(1, loop) # loops the function

if __name__=='__main__':
    win = tk.Tk()
    win.geometry(f'{appWidth}x{appHeight}+{appOffsetX}+{appOffsetY}')
    win.title('EyeFlightSoftware')
    win.configure(bg='black')
    #win.overrideredirect(1) #without borders
    #win.wm_attributes('-fullscreen', 'True') #fullscreen
    EyeFlight(win).pack(side='top', fill='both', expand=True)
    win.after(0, loop)
    win.mainloop()

