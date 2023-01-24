### Import
import numpy as np
### Functions
def define_paddings() -> dict :
    """
    Returns the dictionnary of the functions for different paddings
    That way, the padding selection will just need to call the function related to the given key
    
    """
    return {'random' : random_padding,
            'linear' : linear_padding,
            'max' : max_value_padding,
            'min' : min_value_padding}

def select_padding_type(padding_name : str, dict_of_padding : dict) -> function :
    return dict_of_padding.get(padding_name)

def random_padding(matrix_to_pad : np.ndarray) -> Padded_Matrix :
    
    return 0

def linear_padding(matrix_to_pad : np.ndarray) -> Padded_Matrix :
    return 1

def max_value_padding(matrix_to_pad : np.ndarray) -> Padded_Matrix :
    """
    This function will pad the matrix by replacing all the zeros by the maximum value that is possible for the problem to still be correct (hence m, the number of activities)
    """
    m = matrix_to_pad.shape[1]
    padded_matrix = np.ndarray.copy(matrix_to_pad)
    padded_matrix[padded_matrix == 0] = m
    return padded_matrix

def min_value_padding(matrix_to_pad : np.ndarray) -> Padded_Matrix :
    """
    This function will pad the matrix by replacing the zeros of each line by the minimum value that is not lower than the max value of said line (e.g. the max value of the line + 1)
    """
    n = matrix_to_pad.shape[0]
    padded_matrix = np.ndarray.copy(matrix_to_pad)
    for i in range(n) :
        padded_matrix[i][padded_matrix[i] == 0] = np.amax(padded_matrix[i],axis=0) + 1
    return padded_matrix

def pad_matrix(padding_name : str, matrix_to_pad : np.ndarray) -> Padded_Matrix :
    """
    Return : matrix_to_pad padded with the chosen padding type
    the matrix should be numpy
    """
    dict_of_padding = define_paddings()
    return select_padding_type(padding_name, dict_of_padding)(matrix_to_pad)

def padding_main(matrix_to_pad : np.ndarray, padding_name : str = 'linear', interactive_mode : bool = True) -> Padded_Matrix :
    dict_of_padding = define_paddings()
    _padding_name = padding_name
    
    if(interactive_mode):
        _padding_name = ""
        print("Here are the paddings you can choose")
        paddings = dict_of_padding.keys
        for name in paddings :
            print(name)
        while(_padding_name not in paddings):
            _padding_name = input("Please choose one of the paddings : ")
            
    return pad_matrix(_padding_name, matrix_to_pad)

if __name__ == '__main__':
    dict_of_padding = define_paddings()
    print(dict_of_padding)
    
    matrix_to_pad = np.array([[1,2,3],
                       [2,1,0],
                       [1,0,2],
                       [0,0,1]])
    
    print("Matrix to pad")
    print(matrix_to_pad)
    print("Padded with max value")
    print(max_value_padding(matrix_to_pad))
    print("Matrix to pad")
    print(matrix_to_pad)
    print("Padded with min value")
    print(min_value_padding(matrix_to_pad))