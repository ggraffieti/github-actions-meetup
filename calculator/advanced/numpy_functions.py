import numpy as np


def list_to_numpy(list_py):
    return np.array(list_py)


def average(array):
    if isinstance(array, np.ndarray):
        return array.mean()
    else:
        tmp_array = list_to_numpy(array)
        return tmp_array.mean()

def array_sum(array):
    if isinstance(array, np.ndarray):
        return array.sum()
    else:
        tmp_array = list_to_numpy(array)
        return tmp_array.sum()
