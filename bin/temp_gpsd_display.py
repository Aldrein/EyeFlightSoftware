from cmath import pi, cos, sin
import os
from gps import *
from time import *
import time
import threading

import numpy as np

points = [47.7191667,
47.7605556,
47.7916667,
47.9750000,
48.0019444,
48.0322222,
48.0536111,
48.0569444, 
48.0719444,
48.4433333, 
48.4472222,
48.4633333,
48.5375000,
48.5447222,
48.5877778,
48.6008333,
48.6608333,
48.7497222,
48.7544444, 
48.9269444,
49.1733333,
49.2033333, 
49.6508333]

values = [7979, 7806, 7925, 7237, 7390, 7463, 7129, 7209, 7297, 6437, 6156, 6030, 6152, 6350, 6120, 5898, 6017, 5880, 5601, 5516, 4949, 4804, 3812]

x = 48.636391
y = np.interp(x, points, values)

#y = 7297 + (48.0322222 - 48.0719444) * 1/20 * (40000/(2*pi)) * sin(48.0719444)

print("y = ", y)

"""gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
 
      os.system('clear')
 
      print
      print (' GPS reading')
      print ('----------------------------------------')
      print ('latitude    ' , gpsd.fix.latitude)
      print ('longitude   ' , gpsd.fix.longitude)
      print ('time utc    ' , gpsd.utc,' + ', gpsd.fix.time)
      print ('altitude (m)' , gpsd.fix.altitude)
      print ('eps         ' , gpsd.fix.eps)
      print ('epx         ' , gpsd.fix.epx)
      print ('epv         ' , gpsd.fix.epv)
      print ('ept         ' , gpsd.fix.ept)
      print ('speed (m/s) ' , gpsd.fix.speed)
      print ('climb       ' , gpsd.fix.climb)
      print ('track       ' , gpsd.fix.track)
      print ('mode        ' , gpsd.fix.mode)
      print
      print ('sats        ' , gpsd.satellites)
 
      time.sleep(5) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print ("\nKilling Thread...")
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print ("Done.\nExiting.")

  #print
      #print (' GPS reading')
      #print ('----------------------------------------')
      #print ('latitude    ' , gpsd.fix.latitude)
      #print ('longitude   ' , gpsd.fix.longitude)
      #print ('time utc    ' , gpsd.utc,' + ', gpsd.fix.time)
      #print ('altitude (m)' , gpsd.fix.altitude)
      #print ('eps         ' , gpsd.fix.eps)
      #print ('epx         ' , gpsd.fix.epx)
      #print ('epv         ' , gpsd.fix.epv)
      #print ('ept         ' , gpsd.fix.ept)
      #print ('speed (m/s) ' , gpsd.fix.speed)
      #print ('climb       ' , gpsd.fix.climb)
      #print ('track       ' , gpsd.fix.track)
      #print ('mode        ' , gpsd.fix.mode)
      #print
      #print ('sats        ' , gpsd.satellites)"""