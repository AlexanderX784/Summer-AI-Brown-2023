#for matrix multiplication:
# X = [[1,2,3],  
#        [4,5,6],  
#        [7,8,9]]  
 
# Y = [[10,11,12],  
#       [13,14,15],  
#       [16,17,18]]  
 
# result = [[0,0,0],  
#                [0,0,0],  
#               [0,0,0]]  
 
# # iterate through rows of X  
# for i in range(len(X)):  
#    for j in range(len(Y[0])):  
#        for k in range(len(Y)):  
#            result[i][j] += X[i][k] * Y[k][j]  
# for r in result:  
#    print(r)
# import numpy as np

import numpy as np
import matplotlib.pyplot as plt

#fixing random state for reproducibility
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30*np.random.rand(N))**2 #0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha = 0.5)
plt.show()