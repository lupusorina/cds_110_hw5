import numpy as np
from scipy.linalg import solve_continuous_are
from scipy.linalg import inv

A = np.array([[0, 1],
              [0, 0]])
B = np.array([[0],
              [1]])

q1 = 10
q2 = 1
qu = 1
Q = np.array([[q1, 0],
              [0, q2]])
R = np.array([[qu]])

P = solve_continuous_are(A, B, Q, R)
K = inv(R) @ B.T @ P

K_analytic_1 = np.sqrt(q1 / qu)
K_analytic_2 = np.sqrt(q2 / qu + 2 * K_analytic_1)
print("LQR gain matrix K:", K)
print("LQR gain matrix K_analytic_1:", K_analytic_1)
print("LQR gain matrix K_analytic_2:", K_analytic_2)
