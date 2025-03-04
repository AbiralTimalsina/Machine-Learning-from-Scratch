import math
import numpy as np

def euclidean_distance(x1,x2):
    # Euclidean Distance between two points
    return np.sqrt(np.sum((x1-x2)**2))