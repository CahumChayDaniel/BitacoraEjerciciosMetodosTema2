#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from matplotlib import pyplot as plt

def funcion(e):
    i = e
    resultado = ((8*np.exp(-0.5*i))*np.cos((3)*(i)))
    return resultado
vec = np.arange(0.01,1,0.01)
plt.plot(vec,funcion(vec))
plt.show()

def derivada1(x):
    ev = -4*np.exp(-0.5*x)*np.cos(3*x)-24*np.exp(-0.5*x)*np.sin(3*x)
    return ev
def newton(xi, maxiteraciones, cota):
    error = 1
    i = 1
    print("i | xi | fxi |fdxi | xr | error")
    while error > cota:
        xr = xi - (funcion(xi)/derivada1(xi))
        error = np.abs((xr-xi)/xr)
        xi = xr
        i+=1
        print("Raiz:",xr," Error:", error)

newton(0.1,10,0.01)


# In[ ]:




