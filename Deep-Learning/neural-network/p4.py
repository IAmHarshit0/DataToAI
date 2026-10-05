#calculation of loss 

import math 
import numpy as np

softmax_output = np.array([[4.8, 2.6, 3.5, 1.4, 0.2],
                  [8.9, 1.2, 3.1, 0.5, 0.2],
                  [1.4, 3.5, 2.6, 4.8, 0.2]])

target_output = np.array([[0, 0, 1, 0, 0],
                          [0, 1, 0, 0, 0],
                          [0, 0, 0, 1, 0]])

# loss0 = -math.log(softmax_output[0][0]*target_output[0][0] + softmax_output[0][1]*target_output[0][1] + softmax_output[0][2]*target_output[0][2] + softmax_output[0][3]*target_output[0][3] + softmax_output[0][4]*target_output[0][4])
# print(loss0)
# print(-math.log(softmax_output[0][2]))

print(-np.log(softmax_output[[0, 1, 2], np.argmax(target_output, axis=1)]))