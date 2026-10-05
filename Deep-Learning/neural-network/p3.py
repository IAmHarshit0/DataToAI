# implementing softmax activation function

import math 
import numpy as np

output = [[4.8, 2.6, 3.5, 1.4, 0.2],
          [8.9, 1.2, 3.1, 0.5, 0.2],
          [1.4, 3.5, 2.6, 4.8, 0.2]]

exp_values = np.exp(output - np.max(output, axis=0, keepdims=True))  

norm_values = exp_values / np.sum(exp_values, axis=0, keepdims=True)

print(norm_values)
print(np.sum(norm_values))
