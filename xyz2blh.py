x = float(input("X coordinate:"))
y = float(input("Y coordinate:"))
z = float(input("Z coordinate:"))

import math
#Parameters of GRS80 ellipsoid
a = 6378137.0
b = 6356752.3141 

def xyz2blh(x,y,z):
     
    #Eccentricity
    e = math.sqrt(1-(b**2)/(a**2))
  
    #Longitude
    λ = math.degrees(math.atan2(y, x))
  
    #Latitude
    h0 = 0
    φ = math.atan((z / math.sqrt(x**2+y**2))*((1-e**2)**(-1)))
  
    while abs(φ - h0) > 10**(-12):
        h0 = φ
        N = a / math.sqrt(1 - e**2 * math.sin(h0)**2)
        φ = math.atan((z / math.sqrt(x**2+y**2))*((1 - (e**2 * N)/(N +h0))**(-1)))
 
    #Height
    N = a / math.sqrt(1 - e**2 * math.sin(φ)**2)
    h = math.sqrt(x**2+y**2) / math.cos(φ) - N 
  
    return λ, math.degrees(φ), h

print(f"Cartesian coordinates (𝑥, 𝑦, 𝑧) to ellipsoidal coordinates (𝜑, 𝜆, ℎ):\n{xyz2blh(x, y, z)}")
