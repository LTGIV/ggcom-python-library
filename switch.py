#!/usr/bin/env python
#
# GGCOM - Python - Library - Switch v201503240224
# Brian Beck c/o Louis T. Getterman IV (@LTGIV)
# www.GotGetLLC.com | www.opensour.cc/ggcom/python/lib/switch
#
# Example usage:
# sys.path.append( '%s/ggcom' % os.path.expanduser('~') )
# from ggcom_python_library import switch
#
# Special Thanks to Brian Beck:
# http://code.activestate.com/recipes/410692/

# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
# http://code.activestate.com/recipes/410692/
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False
