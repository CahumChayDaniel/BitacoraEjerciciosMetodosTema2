#!/usr/bin/env python
# coding: utf-8

# In[21]:


from tkinter import Y
import numpy as np
from matplotlib import pyplot as plt
def fx(t):
    return (t+np.power(t, 0.5))*(20-t + np.power(20-t, 0.5))-155.55
vec = np.arange(0, 10, 0.1)
plt.plot(vec, fx(vec))
plt.grid("X")
plt.grid("Y")
plt.show()
def biseccion(a, b, cota):
    error = 1
    i = 0
    lista = [1, 10]
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
            lista.append(xr)
            xract = xr
            if(len(lista) >= 2):
                xrant = lista[-2]
                error = np.abs((xract-xrant)/xract)
            else:
                error = 1
            i += 1
    else:
        print("NO HAY SOLUCIÓN")
    return lista
raices = biseccion(1, 10, 0.01)
y = 20-raices[-1]
print(raices)
print("X:", raices[-1], "Y = ", y)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




