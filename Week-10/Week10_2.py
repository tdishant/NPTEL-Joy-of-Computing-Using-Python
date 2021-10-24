'''
numpy stands for numerical python
mainly used for matrix operations

'''
import numpy as np

#creating an array using numpy
a = np.array([1, 2, 3])

print(type(a))
print(a.shape)#(3, ) => 3 cols, 1 row
print(a[0], a[1], a[2])

a[1] = 6

b = np.array([[1,2, 3], [4, 5, 6]])
print(b)
print(b.shape)#(2, 3) => 2 rows, 3 cols

#to create a 2*2 matrix initalized with zeros

c = np.zeros((2, 2))
print(c)

d = np.ones((2,2))
print(d)

e = np.full((2, 2), 6)
print(e)

#any random value between 0-1 (all values different)
f = np.random.random((2, 2))
print(f)

#to know the datatype of array elements 
x = np.array([1.0, 2.0])
print(x.dtype)

#to specify the datatype
y = np.array([1, 2], dtype = np.int32)
print(y.dtype)

z = np.array([[1, 2], [3, 4]], dtype=np.float64)
q = np.array([[5, 6], [7, 8]], dtype=np.float64)

print(z+q)
print(np.add(z, q))

print(z-q)
print(np.subtract(z, q))

print(z*q)
print(np.multiply(z, q))

print(z/q)
print(np.divide(z, q))

print(np.sqrt(z))

#to transpose a matrix
print(z.T)

#to claculate the sum of all the elements of an array
print(np.sum(z))

#to print the sum columnwise
print(np.sum(z, axis=0))

#to print the sum rowise
print(np.sum(z, axis=1))


