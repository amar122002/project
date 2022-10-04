import matplotlib.pyplot as plt
import numpy as np
from sclpy import ststs
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([7,14,15,18,19,21,26,23])
slpoe,intercept,r,p,std_err = stats.linegress(x,y)
def myfunc(x);
return slope * x + intercept
mynode = list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x,mynode)
plt.show()