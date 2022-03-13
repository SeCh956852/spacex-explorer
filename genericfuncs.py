"""
provide generic functions
"""

def addStringPaddingBefore(string: str, length : int, char : str = " ") -> str:
    return length * char + string
    