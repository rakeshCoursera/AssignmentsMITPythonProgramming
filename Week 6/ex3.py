class Queue(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        #if not e in self.vals:
        self.vals.append(e)

    def remove(self):
        """Remove the formost element from the queue
            otherwiae throught a value error"""
        try:
            element = self.vals[0]
            self.vals.remove(self.vals[0])
            return element
        except:
            raise ValueError()
    
    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

   

