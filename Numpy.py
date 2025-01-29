
import numpy as np
import numpy
from scipy import stats

arr = np.array([1,2,3,4,5])                             ##1d-array
print(arr)
arr1 = {
    "a":"1"
}
print(type(arr))                             # it is from numpy python library
print(type(arr1))

arr = np.array([[1,2,3],[4,5,6]])                       #2-d array
print(arr)

arr1 = np.array([[[1,2,3],
                  [4,5,6]],

                 [[7,8,9],
                  [10,11,12]]])                          #3-d array
# print(arr)

print(arr[0,2])
print(arr[0,1,1])
print(arr1.shape)

arr2 = np.ones((2,3))
print(arr2.ndim)

arr_mat = np.add([1,2,3],[4,5,6])                    #Arthematic operations
arr_mat1 = np.subtract([1,2,3],[4,5,6])
arr_mat2 = np.multiply([1,2,3],[4,5,6])
arr_mat3 = np.divide([1,2,3],[4,5,6])
arr_mat4 = np.power([1,2,3],[4,5,6])
print("add", arr_mat4)


array = np.arange(1,10)                               #reshaping the array np.reshape
print(array)
reshape_arr = array.reshape(3,3)
print(reshape_arr)

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]      #MEAN, MEDIAN, MODE
x = numpy.mean(speed)
print(x)

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]        #we use scipy here for the MODE
x = stats.mode(speed)
print(x)