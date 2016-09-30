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
        self.attrib = {'name': ''}
        
    def open(self):
        raise NotImplementedError
    
    def close(self):
        raise NotImplementedError
    
    def reset(self):
        raise NotImplementedError
    
#     def get_state(self):
#         raise NotImplementedError