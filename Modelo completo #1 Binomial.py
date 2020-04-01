# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:24:55 2020

@author: Joaco
""" 
#Limpia la pantalla

import os
os.system("cls")

# importando modulos necesarios
import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
from math import factorial


#Datos Para graficar
var = "clear"
print("__________Ejercicio de Modelo #1____________")
N=int(input("¿Numero total de eventos?: - "))
p=float (input("¿Probabilidad de Exito en decimales?: - "))
n=int(input("¿Numero de eventos con exitos a evaluar: - "))

# parametros de forma 
binomial = stats.binom(N,p) 
# Distribución
x = np.arange(binomial.ppf(0.01), binomial.ppf(0.9999))
fmp = binomial.pmf(x) 

# Graficando Binomial
# Función de Masa de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
# Respuesta
print("\n\n Respuesta:\n\n La probabilidad es de:")

# Calculo 
res=(N-n)
res2=(1-p)
Cal1=((factorial(N))/((factorial(n))*factorial(res)))
Cal2=((p)**n)

binom=(Cal1*Cal2*(res2**res))
print(" -",binom*100)


R=float(binom*100)
if (R>50<70):
    print(" - La probabilidad es probable")
elif (R<20):
    print(" - La probabilidad no es tan Faborable")
elif (R>=70):
    print(" - La probabilidad es Muy Probable")
elif (R<50):
    print(" - La probabilidad es Faborable")
