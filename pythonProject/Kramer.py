import numpy as np

a = np.array([[1, 2, -3],
             [3, 2, -4],
             [2, -1, 0]])

b = np.array([1,0,-1])

def cramer(a, b):
  mask = np.broadcast_to(np.diag([1,1,1]), [3, 3, 3]).swapaxes(0, 1)

  Ms = np.where(mask, np.repeat(b, 3).reshape(3, 3), a)

  return np.linalg.det(Ms) / np.linalg.det(a)


print(cramer(a,b))