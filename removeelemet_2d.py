import numpy as np
arr = np.array([[1,2,3],
                [3,4,5]])
new_arr = np.delete(arr,0,axis=0)
print(new_arr)