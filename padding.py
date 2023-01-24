### Import
import numpy as np
### Functions
def define_paddings() -> dict :
def select_padding_type(padding_name : str, dict_of_padding : dict) -> function :
def random_padding(matrix_to_pad : np.ndarray) -> Padded_Matrix :
def linear_padding(matrix_to_pad : np.ndarray) -> Padded_Matrix :
def max_value_padding(matrix_to_pad : np.ndarray) -> Padded_Matrix :
def min_value_padding(matrix_to_pad : np.ndarray) -> Padded_Matrix :
def pad_matrix(padding_name : str, matrix_to_pad : np.ndarray) -> Padded_Matrix :
def padding_main(matrix_to_pad : np.ndarray, padding_name : str = 'linear', interactive_mode : bool = True) -> Padded_Matrix :
