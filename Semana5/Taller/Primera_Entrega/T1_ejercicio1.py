"""codigo"""
#2190170
"""datos"""
# L=20
#F.S a esfuerzo ultimo =1.20
#F.S a esfuerzo de fluencia =1.23
"""posibilidades de falla"""
"""barras a carga axial"""
#a esfuerzo de fluencia--------P=6597.640 N
#a esfuerzo ultimo-------------P=10555.350 N
"""cortante en pernos A Y B"""
#-------------------------P=29645.114 N
"""cortante en pernos C, B, D"""
#-------------------------P=14828.072 N
"""el mas critico es el Esfuerzo a fluencia por lo cual la carga maxima p debera ser P=6597.640 N o P=6.56 kN
por lo cual cada barra llevara esa fuerza"""
L=20
Modulo=200
from cmath import sqrt
from math import cos, sin, sqrt
import numpy as N
#barra rigida
#-By*L-w*L/2-=0
#Ax-Bx=0
#Ay-w-By=0
#barras
angulo1=sin(40)
angulo2=cos(50)
#Bx+Cx-Ex*=0
#By-Dy-Cy-Ex=0
a=6597.640
Ex=a*angulo1
Ey=a*angulo2
Dy=a
Cx=a*angulo1
Cy=a*angulo2
By=+Dy+Cy+Ex
Bx=-Cx+Ex

"""Ay, Ax, W"""

matriz= N.array(  [
    [0,0,-L/2],
    [0,1,0],
    [1,0,-1,],
])

vector=N.array([By,Bx,By])
solucion=N.linalg.solve(matriz,vector)
W=solucion[-1]/L
Ax=solucion[0]
Ay=solucion[1]

print("el valor maximo de W Es ", W)
"""parte 2"""
#reacciones [N]

E=sqrt(Ex**2+Ey**2)
C=sqrt(Cx**2+Cy**2)
B=sqrt(Bx**2+By**2)
D=Dy
print("la reaccion Ax es ", Ax)
print("la reaccion Ay es ", Ay)
print("la reaccion en E es ", E)
print("la reaccion en C es ", C)
print("la reaccion en D es ", D)
print("la reaccion en Bx es ", Bx)
print("la reaccion en By es ", By)
print("la fuerza EB es ", a)
print("la fuerza CB es ", a)
print("la fuerza DB es ", a)
#Deformaciones
eEB=a/Modulo

print("la deformacion de todos los cables es la misma ",eEB, )


