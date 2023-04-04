import numpy as np
# image compression uses matrix calculations

a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])

a[1] = 6
print(a)


a = np.array([[1, 2, 3],[4,5,6]])
print(a)

dimensions = (3,4) # (rows, columns)
b = np.zeros(dimensions)
c = np.ones((2,2))

print(b,c)

d = np.full((4,5), 7)

e = np.random.random((2,2))

print(d,e)
