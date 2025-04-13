import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(list).reshape((3,3))
    #Calculations
    mean_calc = [np.mean(a, axis =0).tolist(), np.mean(a, axis=1).tolist(), np.mean(a.flatten()).tolist()]
    var_calc = [np.var(a, axis= 0).tolist(), np.var(a, axis=1).tolist(), np.var(a.flatten()).tolist()]
    std_calc = [np.std(a, axis=0).tolist(), np.std(a, axis=1).tolist(), np.std(a.flatten()).tolist()]
    max_calc =[np.ndarray.max(a, axis=0).tolist(), np.ndarray.max(a, axis=1).tolist(), np.ndarray.max(a.flatten()).tolist()]
    min_calc = [np.min(a, axis=0).tolist(), np.min(a, axis=1).tolist(), np.min(a.flatten()).tolist()]
    sum_calc = [np.sum(a, axis=0).tolist(), np.sum(a, axis=1).tolist(), np.sum(a.flatten()).tolist()]   

    calculations = {'mean': [mean_calc[0], mean_calc[1], mean_calc[2]],
            'variance': [var_calc[0], var_calc[1], var_calc[2]],
            'standard deviation': [std_calc[0], std_calc[1], std_calc[2]],
            'max': [max_calc[0], max_calc[1], max_calc[2]],
            'min': [min_calc[0], min_calc[1], min_calc[2]],
            'sum': [sum_calc[0], sum_calc[1], sum_calc[2]]}
    

    return calculations