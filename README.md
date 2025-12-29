

# Machine-learning-LinearRegression-train-by-gradient_descent

This project demonstrates the implementation of Linear Regression using Gradient Descent from scratch in Python. The model predicts continuous numerical values by learning the optimal slope (m) and intercept (b) to minimize the Mean Squared Error (MSE) between predicted and actual values.

## Features
- Implemented gradient descent algorithm to optimize slope and intercept.
- Calculates Mean Squared Error to monitor learning progress.
- Visualizes regression line and data points using Matplotlib.
- Can be applied to real-world datasets like house prices, sales, etc.

## How to Run
1. Clone the repository.
2. Run `linear_regression_gradient_descent.py` in Python.
3. Observe output and plotted regression line.

## Learning Outcomes
- Understanding Linear Regression mechanics and optimization.
- Hands-on experience with iterative parameter updates.
- Practical Python skills with NumPy and Matplotlib.

## Example Code
```python
# Example usage
m, b = gradient_descent(x, y)
print("Slope:", m, "Intercept:", b)
