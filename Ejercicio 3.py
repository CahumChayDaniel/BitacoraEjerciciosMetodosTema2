#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
from matplotlib import pyplot as plt

def fx(t):
    c = (1.4*(1/100000))*np.power(t, 1.5) +         1.15 * (1/100000)*np.power(t, 2)-0.01962
    return c
vec = np.arange(30, 40, 0.001)
plt.plot(vec, fx(vec))
plt.grid("X")
plt.grid("Y")
plt.show()

def biseccion(a, b, cota):
    error = 1
    i = 1
    listar = [1, 9]
    if fx(a)*fx(b) < 0:
        while error > cota:
            xr = (a+b)/2
            fxr = fx(xr)
            fxa = fx(a)
            if fxr * fxa < 0:
                b = xr
            elif fxr * fxa > 0:
                a = xr
            else:
                break
            listar.append(xr)
            xract = xr
            if(len(listar) >= 2):
                xrant = listar[-2]
                error = np.abs((xract-xrant)/xract)
            else:
                error = 1
            i += 1
    else:
        print("NO EXISTE SOLUCIÓN")
    return listar
raices = biseccion(30, 40, 0.001)
print(raices)
print("X:", raices[-1])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




