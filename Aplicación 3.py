#!/usr/bin/env python
# coding: utf-8

# In[22]:


from scipy.optimize import fsolve
import numpy as np
from matplotlib import pyplot as plt
def f(i):
    A = 750000
    P = 1500
    n = 20 * 12
    return (A - (P / i) * ((1 + i) ** n - 1))
int_mens = fsolve(f, 0.1)
print("La tasa de interés anual es:" + str(int_mens * 12 * 100))
vectorx = np.arange(0, 10, 0.01)
plt.plot(vect, f(vect))
plt.grid("x")
plt.grid("y")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




