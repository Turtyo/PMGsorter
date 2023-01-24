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
def linear_padding(matrix_to_pad : np.ndarray) -> Padded_Matrix :
def max_value_padding(matrix_to_pad : np.ndarray) -> Padded_Matrix :
def min_value_padding(matrix_to_pad : np.ndarray) -> Padded_Matrix :
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
