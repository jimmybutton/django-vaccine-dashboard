def convert(arg_in):
    """convert to float or int if possible, return string otherwise"""
    if not arg_in:
        return None
    try:
        arg_float = float(arg_in)
        arg_int = int(arg_float)
        if arg_int == arg_float:
            return arg_int
        else:
            return arg_float
    except:
        return arg_in

if __name__ == "__main__":
    assert convert('') == None
    assert convert('1') == 1
    assert convert('1.0') == 1
    assert convert('1.2') == 1.2
    assert convert('asdf') == 'asdf'