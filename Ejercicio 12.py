#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.tan(np.pi*x)-6
def secante(xi, xs, cota, maxiteraciones):
    error = 1
    i = 1
    while error > cota:

        xr = xi - ((f(xi)*(xi-xs))/(f(xi)-f(xs)))
        error = np.abs((xr-xi)/xr)
        print("Iteración:", i, " xsup:", xs, "xinf:",
              xi, " Raiz:", xr, " Error:", error)
        xi = xs
        xs = xr
        i += 1
        if(error <= 0.001):
            print("La raíz es: ", xr, " f(raíz): ", f(xr))
            print("Con un error de: ", error)
            plt.plot(xi, 0, 'o', color="g")
            plt.plot(xs, f(xs), 'o', color="y")

secante(0, 0.44, 0.001, 10)
vect = np.arange(.2, .5, 0.001)
plt.plot(vect, f(vect))
plt.title("Ejercicio 12")
plt.grid("X")
plt.grid("Y")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




