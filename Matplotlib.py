import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([0,6])
# ypoints = np.array([0,250])
#
# plt.plot(xpoints, ypoints, 'o')
# plt.show()


xaxis = np.array([1,2,6,8])      #graph
yaxis = np.array([3,8,1,10])
plt.plot(xaxis,yaxis)
plt.show()


x = np.array(["A", "B", "C", "D"])      #bar graph
y = np.array([3, 8, 1, 10])

plt.bar(x,y, color = "orange")
plt.show()

y = np.array([35, 25, 25, 15])           #pie chart

plt.pie(y)
plt.show()