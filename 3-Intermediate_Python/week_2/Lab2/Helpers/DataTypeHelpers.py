__all__ = ['isInt', 'isFloat', 'isDate']

from datetime import datetime

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def isDate(value):
    try:
        datetime.strptime(value, '%Y-%m-%d')
        return True
    except ValueError:
        return False