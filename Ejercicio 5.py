#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
from matplotlib import pyplot as plt

def fx(t):
    return np.power(t, 4)-2*np.power(t, 3)-4*np.power(t, 2)+4
vect = np.arange(0, 2, 0.01)
plt.plot(vect, fx(vect))
plt.grid("X")
plt.grid("Y")
plt.show()
def biseccion(a, b, cota):
    error = 1
    i = 0
    listar = [1, 20]
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
        print("NO HAY SOLUCIÓN")
    return listar
raices = biseccion(0, 2, 0.001)
# raices = biseccion(-2, -1, 0.001) No hay solución
print(raices)
print("La raiz es: ", raices[-1])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




