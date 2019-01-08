# -*- coding = utf-8 -*-

from collections import defaultdict


class Flag(object):
    ''' a bool-like class which has a initial value and switch() method. '''
    def __init__(self, value=False):
        self._value = value
        
    def switch(self):
        self._value = not self._value
        return self._value
        
    def true(self):
        self._value = True
        return self._value
        
    def false(self):
        self._value = False
        return self._value
        
    def __bool__(self):
        return self._value
        
    def __repr__(self):
        return str(self._value)


class Flags(object):
    def __init__(self):
        self._flags = defaultdict()
        
    def add(self, flag_name, flag_value=False):
        if flag_name in self._flags.keys():
            raise TypeError('\'{0}\' is already in global flags.'.format(flag_name))
        self._flags[flag_name] = Flag(flag_value)
        
    def remove(self, flag_name):
        if flag_name not in self._flags.keys():
            raise TypeError('\'{0}\' is not in global flags.'.format(flag_name))
        self._flags.pop(flag_name)
        
    def __getattr__(self, flag_name):
        if flag_name not in self._flags.keys():
            self.add(flag_name)
        return self._flags[flag_name]
