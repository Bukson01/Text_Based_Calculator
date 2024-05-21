# private variable to store the result
_result = None  

def _is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False