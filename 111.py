from numpy import linalg as la
from numpy import mat
A = mat([[1,0,1,0,0,0],[0,1,0,0,0,0],[1,1,0,0,0,0],[1,0,0,1,1,0],[0,0,0,1,0,1]])
#SVD降维
U,S,T = la.svd(A)
#取出矩阵的前三列构成词项矩阵
u = U[:,0:3]
print(u)
#去除矩阵的前三行构成文档矩阵
t = T[0:3,:]
print(t)