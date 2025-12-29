import numpy as np

x = np.array([1,2,3,4,5,6])
y = np.array([6,12,18,24,30,36])

def gradient_descent(x, y):
    m_curr = 0
    b_curr = 0
    iterations = 100 #100....10000
    learning_rate = 0.001 # 0.01....0.08

    for i in range(iterations):
        y_predict = m_curr * x + b_curr

        # cost function (MSE)
        cost = (1/n) * np.sum((y - y_predict)**2)

        # gradient
        md = -(2/n) * np.sum(x * (y - y_predict))
        bd = -(2/n) * np.sum(y - y_predict)

        # update parameters
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        if i % 100 == 0:
            print(f"Iteration {i}: m={m_curr:.4f}, b={b_curr:.4f}, cost={cost:.4f})")

    return m_curr, b_curr


m, b = gradient_descent(x, y)
print("\nFinal Result:")
print("m =", m)
print("b =", b)
