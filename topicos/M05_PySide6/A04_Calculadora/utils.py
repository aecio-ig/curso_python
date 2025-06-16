import re 

NUM_OR_DOT_REGEX = re.compile(r'[0-9.]$')


def isNUmOrDot(strig: str):
    return bool(NUM_OR_DOT_REGEX.search(strig))

def isEmpty(string: str):
    return len(string) <= 0

def isValidNumber(numero: str):
    try:
        float(numero)
        return True
    except ValueError:
        return False