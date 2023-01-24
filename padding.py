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
def padding_main(matrix_to_pad : np.ndarray, padding_name : str = 'linear', interactive_mode : bool = True) -> Padded_Matrix :
