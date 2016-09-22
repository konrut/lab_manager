'''
Created on 22 wrz 2016

@author: Konrad Rutkowski
'''

class LabEq(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.name = ""
        
    def init(self):
        raise NotImplementedError
    
    def reset(self):
        raise NotImplementedError
    
    def turn_on(self):
        raise NotImplementedError
    
    def turn_off(self):
        raise NotImplementedError
    
    def get_state(self):
        raise NotImplementedError