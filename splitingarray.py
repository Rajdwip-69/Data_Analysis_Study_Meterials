import numpy as np

arr = np.array([1, 2, 3, 4, 5,6])

# Correct usage: Provide the indices where the split should happen
print(np.split(arr, [2]))  # Splits at index 2
