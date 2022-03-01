from cmath import pi, cos, sin, tan
import os
from gps import *
from time import *
import time
import threading

import numpy as np

Latitudes = [
  6750963.88,
  6759681.42,
  6753694.92,
  6788103.10,
  6780495.83,
  6776814.49,
  6793520.54,
  6789495.23,
  6785176.44,
  6828087.29,
  6842100.89,
  6848529.80,
  6842389.53,
  6832520.39,
  6843999.75,
  6855085.05,
  6849124.16,
  6855971.57,
  6869969.60,
  6874250.35,
  6902560.21,
  6909764.42,
  6959350.57]

"""[47.7191667,
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
49.6508333]"""

Longitudes = [
  271270.03,
  218072.21,
  352520.42,
  165912.09,
  299190.22,
  421139.34,
  204081.20,
  259128.67,
  347762.87,
  322842.59,
  151974.52,
  104913.37,
  268039.38,
  450219.96,
  325596.95,
  198004.85,
  375681.37,
  435792.05,
  224730.77,
  469632.39,
  448479.64,
  371849.61,
  376812.49,]

"""[-2.7233336,
-3.4400004,
-1.6436111,
-4.1677778,
-2.3786112,
-0.7427778,
-3.6641666,
-2.9233333,
-1.7322223,
-2.1033335,
-4.4216667,
-5.0636111,
-2.8566667,
-0.3850000,
-2.0800000,
-3.8166664,
-1.4058333,
-0.5947223,
-3.4719445,
-0.1447222,
-0.4500000, 
-1.5047223,
-1.4752778]"""

Xpixels = [4025, 2961, 5650, 1919, 4584, 7023, 2682, 3782, 5555, 5057, 1639, 699, 3961, 7604, 5112, 2561, 6114, 7317, 3095, 7993, 7570, 6038, 6136]

Ypixels = [7979, 7806, 7925, 7237, 7390, 7463, 7129, 7209, 7297, 6437, 6156, 6030, 6152, 6350, 6120, 5898, 6017, 5880, 5601, 5516, 4949, 4804, 3812]

Lat_point = 6801308.33 #48.332655=6824038.55 #48.541797=6834651.05 #48.187548 #48.636391=6846845.28
Lon_point = 297173.05 #-3.602486=211250.51 #-1.088229=398354.06 #-2.424753 #-1.510278=367846.21

#XMStM = (LonMStM * cos(4.134855927) + LatMStM * sin(4.134855927)) * 1/20 * (40000/(2*pi))
#YMStM = (LatMStM * cos(4.134855927) - LonMStM * sin(4.134855927)) * 1/20 * (40000/(2*pi))

Ypixels_point = np.interp(Lat_point, Latitudes, Ypixels) #* (cos(4.134855927 * pi/180) + sin(4.134855927* pi/180))
Xpixels_point = np.interp(Lon_point, Longitudes, Xpixels) #* (cos(4.134855927 * pi/180) + sin(4.134855927 * pi/180))

#y = 7297 + (48.0322222 - 48.0719444) * 1/20 * (40000/(2*pi)) * sin(48.0719444)

print("Xinconnu =", Xpixels_point)
print("Yinconnu =", Ypixels_point)

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