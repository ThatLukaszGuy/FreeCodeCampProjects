import numpy as np

def calculate(list):
    # check that list has 9 elements
    if len(list) < 9: raise ValueError("List must contain nine numbers.")
    # convert to matrix
    m = np.array([      list[0:3], 
                        list[3:6], 
                        list[6:], ])
    # one dimensional
    flat_mat = m.flatten()
    
    # just apply needed method for correct axis
    return {
                'mean': [ m.mean(axis=0).tolist(), m.mean(axis=1).tolist(), flat_mat.mean() ],
                'variance': [ m.var(axis=0).tolist(), m.var(axis=1).tolist(), flat_mat.var()],
                'standard deviation': [ m.std(axis=0).tolist(),m.std(axis=1).tolist(), flat_mat.std()],
                'max': [ m.max(axis=0).tolist(), m.max(axis=1).tolist(), flat_mat.max()],
                'min': [ m.min(axis=0).tolist(), m.min(axis=1).tolist(), flat_mat.min()],
                'sum': [ m.sum(axis=0).tolist(), m.sum(axis=1).tolist(), flat_mat.sum()]
                } 