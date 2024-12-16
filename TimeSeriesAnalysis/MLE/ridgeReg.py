import numpy as np

def rReg(X, y):
    X = np.array(X)
    l = 0.5
    T = X.T
    A = np.dot(T, X)
    L = np.identity(len(X[0]))
    A = A + L
    A = np.linalg.inv(A)
    A = np.dot(A, T)
    beta = np.dot(A, y)
    return beta