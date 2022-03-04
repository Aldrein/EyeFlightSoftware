
# DONE: Create class to handle GPS data retrieving and processing
# TODO: - getData() -> string
# DONE: - translateGPStoImage(string) -> (float x, float y)
# TODO: - translateImagetoGPS(float x, float y) -> string
# DONE: - calculate linear regression in __init__ to provide the translation matrix
# TODO: - getAlt() -> float
# TODO: - getLat() -> float 
# TODO: - getLong() -> float

from cmath import pi, sin, cos, sqrt, log, tan, exp
import gpsd

import numpy as np

class GpsUtils():
  
  longitudesWS84 = [-2.7233336, -3.4400004, -1.6436111, -4.1677778, -2.3786112, -0.7427778, -3.6641666, -2.9233333, -1.7322223, -2.1033335, -4.4216667, -5.0636111, -2.8566667, -0.3850000, -2.0800000, -3.8166664, -1.4058333, -0.5947223, -3.4719445, -0.1447222, -0.4500000, -1.5047223, -1.4752778]
  latitudesWS84 = [47.7191667, 47.7605556, 47.7916667, 47.9750000, 48.0019444, 48.0322222, 48.0536111, 48.0569444, 48.0719444, 48.4433333, 48.4472222, 48.4633333, 48.5375000, 48.5447222, 48.5877778, 48.6008333, 48.6608333, 48.7497222, 48.7544444, 48.9269444, 49.1733333, 49.2033333, 49.6508333]
  
  longitudesRGF93 = []
  latitudesRGF93 = []

  longitudespixels = [4025, 2961, 5650, 1919, 4584, 7023, 2682, 3782, 5555, 5057, 1639, 699, 3961, 7604, 5112, 2561, 6114, 7317, 3095, 7993, 7570, 6038, 6136]
  latitudespixels = [7979, 7806, 7925, 7237, 7390, 7463, 7129, 7209, 7297, 6437, 6156, 6030, 6152, 6350, 6120, 5898, 6017, 5880, 5601, 5516, 4949, 4804, 3812]

  a = 6378137       #demi-grand axe de l'éllipsoïde (m)
  e = 0.08181919106 #première exentricité à l'origine
  x0 = 700000       #coordonnées à l'origine
  y0 = 6600000      #coordonnées à l'origine

  def access(self):
    gpsd.connect()
    packet = gpsd.get_current()
    print(packet.position())

    for i in range(len(self.longitudesWS84)):
      longRGF93, latRGF93 = self.conversionWS84toRGF93(self.longitudesWS84[i], self.latitudesWS84[i])
      self.longitudesRGF93.append(longRGF93)
      self.latitudesRGF93.append(latRGF93)

    while True:
      latWS84, lonWS84 = gpsd.get_current().position()
      print("Latitude : ", latWS84, "Longitude : ", lonWS84)
      lonRGF93, latRGF93 = GpsUtils().conversionWS84toRGF93(lonWS84, latWS84)
      lonP, latP = GpsUtils().interpolation(lonRGF93, latRGF93)
      return lonWS84, latWS84, lonP, latP
    #self.longitudesRGF93, self.latitudesRGF93 = self.conversionWS84toRGF93(self.longitudesWS84, self.latitudesWS84)

  """def transformation(latitudesWS84, longitudesWS84):
    crs = CRS.from_proj4("+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ")
    inProj = Proj('epsg:4326')
    outProj = Proj(crs)
    longitudesRGF93, latitudesRGF93 = transform(inProj, outProj, latitudesWS84, longitudesWS84)
    return longitudesRGF93, latitudesRGF93"""

  def deg2rad(self, angle):
    return angle * pi/180

  def conversionWS84toRGF93(self, longitudeWS84, latitudeWS84):
    l0 = self.deg2rad(3)
    lc = self.deg2rad(3)
    phi0 = self.deg2rad(46.5)    # latitude d'origine en radian
    phi1 = self.deg2rad(44)      # 1er parallele automécoïque
    phi2 = self.deg2rad(49)      # 2eme parallele automécoïque

    phi = self.deg2rad(float(latitudeWS84))
    l = self.deg2rad(float(longitudeWS84))

    #calcul des grandes normales
    gN1 = self.a / sqrt(1 - self.e * self.e * sin(phi1) * sin(phi1))
    gN2 = self.a / sqrt(1 - self.e * self.e * sin(phi2) * sin(phi2))

    #calculs des latitudes isométriques
    gl1 = log(tan(pi / 4 + phi1 / 2) * ((1 - self.e * sin(phi1)) / (1 + self.e * sin(phi1))) ** (self.e / 2))
    gl2 = log(tan(pi / 4 + phi2 / 2) * ((1 - self.e * sin(phi2)) / (1 + self.e * sin(phi2))) ** (self.e / 2))
    gl0 = log(tan(pi / 4 + phi0 / 2) * ((1 - self.e * sin(phi0)) / (1 + self.e * sin(phi0))) ** (self.e / 2))
    gl = log(tan(pi / 4 + phi / 2) * ((1 - self.e * sin(phi)) / (1 + self.e * sin(phi))) ** (self.e / 2))

    #calcul de l'exposant de la projection
    n = (log((gN2 * cos(phi2)) / (gN1 * cos(phi1)))) / (gl1 - gl2)

    #calcul de la constante de projection
    c = ((gN1 * cos(phi1)) / n) * exp(n * gl1)
    
    #calcul des coordonnées
    ys = self.y0 + c * exp(-1 * n * gl0)
    unknonwnRGF93_long = self.x0 + c * exp(-1 * n * gl) * sin(n * (l - lc))
    unknonwnRGF93_lat = ys - c * exp(-1 * n * gl) * cos(n * (l - lc))

    return unknonwnRGF93_long.real, unknonwnRGF93_lat.real

  def interpolation(self, longitudeRGF93, latitudeRGF93):
      print("longitudeRGF93 = ", longitudeRGF93, "latitudeRGF93 = ", latitudeRGF93)
      unknown_longPi = np.interp(longitudeRGF93, self.longitudesRGF93, self.longitudespixels) 
      unknown_latPi = np.interp(latitudeRGF93, self.latitudesRGF93, self.latitudespixels)
      return unknown_longPi, unknown_latPi