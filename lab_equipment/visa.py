'''
Created on 22 wrz 2016

@author: Konrad Rutkowski
'''

import pyvisa
import lab_equipment

class LabEqVisa(lab_equipment.LabEq):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.resource_name = 'Unknawn'
        self.resource = None;
        super(LabEqVisa,self).__init__()
        
    def init(self, resource_name = ''):
        if resource_name != '':
            self.resource_name = resource_name            
        rm = pyvisa.ResourceManager()
        try:
            self.resource = rm.open_resource(resource_name)
        except pyvisa.errors.VisaIOError:
            print('visa: Resource not found!')
            raise IOError