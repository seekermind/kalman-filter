import nupy as np
import scipy as sc

X_i = [np.array([[4000], [280]])]
Y = np.array([4260, 282, 4550, 285, 4860, 286, 5110, 290]).reshape(4,2,1)
P_i = [np.array([[400, 0], [0, 25]])]

dt = 1
A = np.array([[1, dt], [0,1]])
B = np.array([[(dt**2)/2], [dt]])
U = np.array([[2]])

def predict_new_state(X_i, A, B, U):
    X =  A.dot(X_i) + B.dot(U)
    return X


def predict_new_cov(P_i):
    P = A.dot(P_i.dot(A.T))
    return P

R = np.array([[625, 0], [0, 36]])
H = np.eye(2)

def kalman_gain(P, H, R):
    K = (P.dot(H)).dot(np.linalg.inv(H.dot(P.dot(H.T)) + R))
    return K

def current_state(X_i, K, H, Y):
    X = X_i + K.dot(Y - H.dot(X_i))
    return X


def update_cov(K, H, P_i):
    P = (np.eye(2)-K.dot(H)).dot(P_i)
    return P

for i in range(4):
    X = predict_new_state(np.array(X_i[i]), A, B, U)
    P = predict_new_cov(P_i[i])
    K = kalman_gain(P, H, R)
    X_i += [current_state(X, K, H, Y[i])]
    P_i += [update_cov(K, H, P)]    


print(P_i)
print(X_i)
