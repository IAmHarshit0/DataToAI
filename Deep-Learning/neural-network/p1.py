import numpy as np

# from the previous layers
inputs = [[1.0, 2.0, 3.0, 2.5],
          [2.0, 5.0, 1.0, 2.5],
          [3.0, 1.0, 2.5, 1.5]]

weights1 = [0.1, 0.2, 0.3, 0.4]
weights2 = [0.4, 0.5, 0.6, 0.7]
weights3 = [0.7, 0.8, 0.9, 1.0]
weights = [weights1, weights2, weights3]
weights02 = [[0.1, 0.14, 0.19],
             [0.2, 0.25, 0.3],
             [0.3, 0.35, 0.4]]
bias1 = 2.0
bias2 = 3.0
bias3 = 4.0

bias = [bias1, bias2, bias3]
bias02 = [-1.0, -2.0, -3.0]

# current layer
# layer_outputs = []  # output of current layer
# for neuron_weights, neuron_bias in zip(weights, bias):
#     neuron_output = 0  # output of given neuron
#     for n_input, weight in zip(inputs, neuron_weights):
#         neuron_output += n_input * weight
#     neuron_output += neuron_bias
#     layer_outputs.append(neuron_output)

# print(layer_outputs)

# Using numpy to calculate the outputs of the layer
layer1_outputs = np.dot(inputs, np.array(weights).T) + bias
layer2_outputs = np.dot(layer1_outputs, np.array(weights02).T) + bias02
print(layer2_outputs)