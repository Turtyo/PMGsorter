### Import

### Functions

def define_paddings():
    """
    Returns the dictionnary of the functions for different paddings
    That way, the padding selection will just need to call the function related to the given key
    
    """
    return {'random' : random_padding,
            'linear' : linear_padding,
            'max' : max_value_padding,
            'min' : min_value_padding}

def select_padding_type(name : str, dict_of_padding : dict):
    return dict_of_padding.get(name)

def random_padding():
    return 0

def linear_padding():
    return 1

def max_value_padding():
    return 2

def min_value_padding():
    return 3

if __name__ == '__main__':
    dict_of_padding = define_paddings()
    print(dict_of_padding)
    for name in ('random','linear','max','min'):
        print(select_padding_type(name, dict_of_padding)())