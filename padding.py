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

def random_padding():
    return 0

def linear_padding():
    return 1

def max_value_padding():
    return 2

def min_value_padding():
    return 3



def pad_matrix(padding_name : str, matrix_to_pad : numpy.ndarray) -> numpy.ndarray:
    """
    Retun : matrix_to_pad padded with the chosen padding type
    the matrix should be numpy
    """
    dict_of_padding = define_paddings()
    return select_padding_type(padding_name, dict_of_padding)(matrix_to_pad)

def padding_main(matrix_to_pad : numpy.ndarray, padding_name : str = 'linear', interactive_mode : bool = True):
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
    for name in ('random','linear','max','min'):
        print(select_padding_type(name, dict_of_padding)())