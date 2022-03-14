#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2*np.sin(np.pi*x)+x
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
        if(error <= 0.01):
            print("La raíz es: ", xr, " f(raíz): ", f(xr))
            print("Con un error de: ", error)
            plt.plot(xi, 0, 'o', color="g")
            plt.plot(xs, f(xs), 'o', color="y")
secante(1.5, 2, 0.01, 10)
x = np.linspace(1, 2, 7)
plt.plot(x, f(x))
plt.title("Ejercicio 8")
plt.grid('on')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




