### Import
import numpy as np
from typing import Callable
from typing import Dict
import random
import numpy.typing as npt

### Type

Padded_matrix = npt.NDArray[npt.NDArray[int]]
Not_padded_matrix = npt.NDArray[npt.NDArray[int]]
Function = Callable

### Functions

def define_paddings() -> Dict[str,Function] :
    """
    Returns the dictionnary of the functions for different paddings
    That way, the padding selection will just need to call the function related to the given key
    
    """
    return {'random' : random_padding,
            'max' : max_value_padding,
            'min' : min_value_padding}

def random_padding(matrix_to_pad : Not_padded_matrix) -> Padded_matrix :
    n,m = matrix_to_pad.shape
    padded_matrix = np.ndarray.copy(matrix_to_pad)
    for i in range(n):
        max_on_line = np.max(padded_matrix[i])
        ranks_to_add = [var for var in range(max_on_line+1,m+1)]
        random.shuffle(ranks_to_add)
        padded_matrix[i][padded_matrix[i] == 0] = ranks_to_add
    return padded_matrix

def max_value_padding(matrix_to_pad : Not_padded_matrix) -> Padded_matrix :
    """
    This function will pad the matrix by replacing all the zeros by the maximum value that is possible for the problem to still be correct (hence m, the number of activities)
    """
    m = matrix_to_pad.shape[1]
    padded_matrix = np.ndarray.copy(matrix_to_pad)
    padded_matrix[padded_matrix == 0] = m
    return padded_matrix

def min_value_padding(matrix_to_pad : Not_padded_matrix) -> Padded_matrix :
    """
    This function will pad the matrix by replacing the zeros of each line by the minimum value that is not lower than the max value of said line (e.g. the max value of the line + 1)
    """
    n = matrix_to_pad.shape[0]
    padded_matrix = np.ndarray.copy(matrix_to_pad)
    for i in range(n) :
        padded_matrix[i][padded_matrix[i] == 0] = np.amax(padded_matrix[i],axis=0) + 1
    return padded_matrix

def pad_matrix(matrix_to_pad : Not_padded_matrix, padding_name : str = 'random', ) -> Padded_matrix :
    """
    Return : matrix_to_pad padded with the chosen padding type
    the matrix should be numpy
    """
    return define_paddings().get(padding_name)(matrix_to_pad)

if __name__ == '__main__':
    dict_of_padding = define_paddings()
    print(dict_of_padding)
    
    matrix_to_pad = np.array([[1,2,3],
                       [2,1,0],
                       [1,0,2],
                       [0,0,1],
                       [0,0,0]])
    
    print("Matrix to pad")
    print(matrix_to_pad)
    print("Padded with max value")
    print(max_value_padding(matrix_to_pad))
    print("Padded with min value")
    print(min_value_padding(matrix_to_pad))
    print("Padded with random value")
    print(random_padding(matrix_to_pad))