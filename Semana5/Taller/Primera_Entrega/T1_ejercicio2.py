#reacciones
from numpy import arange
import numpy as np
from math import cos, sin, sqrt


#AX,AY,Dx
for p in arange(20, 24.5,0.25):
    for angulo in range(0, 180, 10):
            ecuaciones= np.array([
            [0,0,-1],
            [1,0,1],
            [-1,0,0],] )
            resultado= np.array([4*p*cos(angulo),p*cos(angulo),p*sin(angulo)])
    print(resultado)

#AB, BC, CD, DE, AE, AD, BD.
#for resultado [1:18]:
    