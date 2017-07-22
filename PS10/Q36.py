# Does
class Bread(object):
    """
    docstring for Bread.
    """
    attr = "Bread"
    def __init__(self, arg):
        super(Bread, self).__init__()
        cls.arg = arg

def logToastEvent(arg=None):
    print("Does this change the Bread class from 'Bread' to 'Toast'?")
    print("Original Bread.attr:", Bread.attr)
    Bread.attr = "Toast"
    print("Bread.attr:", Bread.attr)

logToastEvent()
