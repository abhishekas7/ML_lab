import numpy as np
from numpy import array
from scipy.linalg import svd

mat1=np.array([[2,3,4],[5,6,7],[8,9,0]])
mat2=np.array([[5,3,4],[5,4,7],[4,2,0]])
print("Addition")
print(np.add(mat1,mat2))
print("Subtraction")
print(np.subtract(mat1,mat2))
print("Division")
print(np.divide(mat1,mat2))
print("multiply")
print(np.multiply(mat1,mat2))

A=array([[12,12,30],[5,8,2],[1,5,3],[5,2,6]])
a,b,c=svd(A)
print("decomposition",a)
print("Inverse",b)
print("Transpose",c)




