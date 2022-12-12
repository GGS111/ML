import numpy as np


def linear_regression_normal_equation(X, y):
    '''
    y = X * w -->
    X.T * y = X.T * X * w --> 
    X.T * X = R - Это Матрица регрессии -->
    X.T * y = R * w --> 
    X.T * y * R^-1 = w 
    '''
    ones = np.ones((X.shape[0], 1)) #Bias
    X = np.append(ones, X, axis=1) #Собираем параметры Условно wx + b
    X_dot = np.dot(X.T, X) #Матрица регрессии
    Y_dot = np.dot(X.T, y)
    X_SVD = np.linalg.inv(X_dot) #Перенесли в другую часть уравнение и взяли обратную матрицу, чтобы поднять наверх
    W = np.dot(X_SVD, Y_dot) 
    return W


if __name__ == "__main__":
    # Run a small test example: y = 5x (approximately)
    m, n = 500, 1
    X = np.random.rand(m, n)
    y = 5 * X + np.random.randn(m, n) * 0.1
    W = linear_regression_normal_equation(X, y)
    print(W)
    # Находим что W очень близко равно 5