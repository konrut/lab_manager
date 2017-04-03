'''!
@package lab_equipment
@date 22 sep 2016
@author Konrad Rutkowski
'''

class LabEq(object):
    '''!
    classdocs
    '''
    def __init__(self, labeq_type, name_id = ''):
        '''!
        Constructor
        '''
                
    def open(self):
        raise NotImplementedError
    
    def close(self):
        raise NotImplementedError
    
    def reset(self):
        raise NotImplementedError
    
    
            