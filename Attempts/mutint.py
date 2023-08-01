#Making a new primitive datatype is actually one of the most complicated programming 
#tasks in Python. There are a lot of edge cases and low-level issues to worry about
#--especially with regard to how your type interacts with other Python types. 
#Probably the key thing to keep in mind is that you can customize almost every 
#aspect of how an object interacts with the rest of Python if you know the 
#underlying protocols. If you're going to do this, it's advisable to look at the 
#existing code for something similar to what you're trying to make.

from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        return format(self.value, fmt)
    
    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented
        
    __radd__ = __add__ #reversed operands

    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
        
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
        
    def __int__(self):
        return self.value

    __index__ = __int__     # Make indexing work

    def __float__(self):
        return float(self.value)
    
