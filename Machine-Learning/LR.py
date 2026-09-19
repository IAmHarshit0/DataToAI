import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(f'C:\\Users\\iamha\\OneDrive\\Documents\\DS\\OneShot\\package.csv')

def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].cgpa
        y = points.iloc[i].package
        total_error += (y - (m*x + b))**2
    return total_error/float(len(points))

def gradient_descent(m_now, b_now, points, l):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].cgpa
        y = points.iloc[i].package

        m_gradient += -(2/n)*x*(y - (m_now*x + b_now))
        b_gradient += -(2/n)*(y - (m_now*x + b_now))

    m = m_now - m_gradient*l
    b = b_now - b_gradient*l
    return m, b

def linear_regression(m, b, l, epochs, data):
    for i in range(epochs):
        if i%50 == 0:
            print(f'Epoch: {i}')
        m, b = gradient_descent(m, b, data, l)

    print('scratch m: ',m)
    print('scratch b: ',b)
    return(m, b)

m, b = linear_regression(m=0, b=0, l=0.0001, epochs=500, data=data)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(data[['cgpa']], data['package'])

print('scikit m: ',lr.coef_[0])
print('scikit b: ',lr.intercept_)


import numpy as np

# Scatter actual points
plt.scatter(data.cgpa, data.package, color='black', label='Actual data')

# Create a smooth range of CGPA values for plotting
x_vals = np.linspace(data.cgpa.min(), data.cgpa.max(), 100)

# Custom linear regression line (from scratch)
y_scratch = m * x_vals + b
plt.plot(x_vals, y_scratch, color='red', label='Scratch LR')

# Scikit-learn linear regression line
y_sklearn = lr.coef_[0] * x_vals + lr.intercept_
plt.plot(x_vals, y_sklearn, color='blue', linestyle='--', label='Scikit-learn LR')

# Add labels and legend
plt.xlabel('CGPA')
plt.ylabel('Package (LPA)')
plt.title('Comparison of Scratch vs Scikit-learn Linear Regression')
plt.legend()
plt.show()