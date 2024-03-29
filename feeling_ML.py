# *
# *基础感知：线性拟合数据
# *20180815

import numpy as np 
# 原始数据
x = [1, 2, 3, 4, 5, 6]
y = [2.6, 3.4, 4.7, 5.5, 6.47, 7.8]

# 用一次多项式拟合，相当于线性拟合
z1 = np.polyfit(x, y, 1)
p1 =np.poly1d(z1)
print(z1)   # [1.          1.49333333]
print(p1)   # [ 1 x + 1.493]

# 作图显示
import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(1, 7)
y = z1[0] * x + z1[1]
plt.figure()
plt.scatter(x, y)
plt.plot(x, y)
plt.show()
