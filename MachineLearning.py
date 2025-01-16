import numpy
from scipy import stats
import matplotlib.pyplot as plt


# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]      #MEAN, MEDIAN, MODE
# x = numpy.mean(speed)
# print(x)
#
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# x = numpy.median(speed)
# print(x)
#
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]        #we use scipy stats here for the MODE
# x = stats.mode(speed)
# print(x)

#                     #percentile
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
#
# x = numpy.percentile(ages,42)
# print(x, "%")

                        # DATA DISTRIBUTION
# x = numpy.random.uniform(0.0, 5.0, 250)
# print(x)
# plt.hist(x,5)
# plt.show()
                        #NORMAL DATA DISTRIBUTION
# y = numpy.random.normal(5.0, 1.0, 250)
# print(y)
# plt.hist(y,5)
# plt.show()



                        #LINEAR REGRESSION
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x,y)

def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc,x))

plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()