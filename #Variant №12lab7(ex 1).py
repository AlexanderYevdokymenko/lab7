#Variant №12
#Y(x)=5*sin(10*x)*sin(3*x)/(x**x), x=[0...8]

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 8)
y = 5 * np.sin(10*x) * np.sin(3*x)/(x**x)

fig, ax = plt.subplots()
plt.plot(x,y)
plt.show()

fig.savefig('мій графік')
print("Ваш графік збереженний біля файла .py")