import numpy as np
import pandas as pd

def calculate(lst):
    try:
        if len(lst) != 9:
            raise ValueError
    except ValueError:
        print("List must contain nine numbers.")
        return {}

    arr = np.array(lst)
    mat = np.reshape(arr, (3,3))
    mean_axis1 = np.mean(mat, axis=0)
    mean_axis2 = np.mean(mat, axis=1)
    mean_flat = np.mean(mat)
    mean = [mean_axis1.tolist(), mean_axis2.tolist(), mean_flat.tolist()]

    var_axis1 = np.var(mat, axis=0)
    var_axis2 = np.var(mat, axis=1)
    var_flat = np.var(mat)
    var = [var_axis1.tolist(), var_axis2.tolist(), var_flat.tolist()]

    std_axis1 = np.std(mat, axis=0)
    std_axis2 = np.std(mat, axis=1)
    std_flat = np.std(mat)
    std = [std_axis1.tolist(), std_axis2.tolist(), std_flat.tolist()]

    max_axis1 = np.max(mat, axis=0)
    max_axis2 = np.max(mat, axis=1)
    max_flat = np.max(mat)
    max = [max_axis1.tolist(), max_axis2.tolist(), max_flat.tolist()]

    min_axis1 = np.min(mat, axis=0)
    min_axis2 = np.min(mat, axis=1)
    min_flat = np.min(mat)
    min = [min_axis1.tolist(), min_axis2.tolist(), min_flat.tolist()]

    sum = []
    sum_axis1 = np.sum(mat, axis=0)
    sum_axis2 = np.sum(mat, axis=1)
    sum_flat = np.sum(mat)
    sum = [sum_axis1.tolist(), sum_axis2.tolist(), sum_flat.tolist()]

    d = {}
    d['mean'] = mean
    d['variance'] = var
    d['standard deviation'] = std
    d['max'] = max
    d['min'] = min
    d['sum'] = sum

    return d

result = calculate([0,1,2,3,4,5,6,7,8])
if result:
    print(result)
