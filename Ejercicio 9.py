#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.power(x, 2)-6
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
secante(1, 5, 0.001, 10)
x = np.linspace(1, 10, 7)
plt.plot(x, f(x))
plt.title("Ejercicio 9")
plt.grid('on')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




