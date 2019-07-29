import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x = range(0,10,3)  
y = map(lambda i:  10*i**3  , x)

#x = [1.,2.,3.]
#y = [1.,8.,27.]

a = sym.var('a')
res = 0
for j in range(len(x)):
    y_k = y[j]
    lj = 1.
    for m in range(len(x)):
        try:
            if m != j:
                lj *= (a - x[m]) / float(x[j] - x[m])
        except:
            print "Err"
            pass
    
    res+= y_k  * lj
print sym.expand(res) 
plt.figure()
plt.plot(x,y)
plt.show()


