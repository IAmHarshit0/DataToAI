# converting to class-based implementation of neural network

import numpy as np

np.random.seed(0)

X = [[-1.0, 2.0, 3.0, -2.5],
     [2.0, -5.0, 1.0, -2.5],
     [-3.0, 1.0, -2.5, 1.5]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

# implementing activation function ReLU (Rectified Linear Activation Function)
class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

# implementing the softmax activation function
class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=0, keepdims=True))
        norm_values = exp_values / np.sum(exp_values, axis=0, keepdims=True)
        self.output = norm_values

class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

class Loss_CrossEntropy(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7) 
        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods

layer1 = Layer_Dense(4, 3)
layer2 = Layer_Dense(3, 2)
activation_layer = Activation_ReLU()
activation_softmax = Activation_Softmax()
loss = Loss_CrossEntropy()

layer1.forward(X)
activation_layer.forward(layer1.output)
layer2.forward(activation_layer.output)
activation_softmax.forward(layer2.output)
loss = loss.calculate(activation_softmax.output, np.array([[0, 1], [1, 0], [0, 1]]))

print(loss)