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

    def __init__(self, resource_name):
        '''
        Constructor
        '''
        super(LabEqVisa,self).__init__()
        self._resource_name = resource_name
        self._resource = None        
        
    def open(self, resource_name = ''):
        if resource_name != '':
            self._resource_name = resource_name            
        rm = pyvisa.ResourceManager()
        try:
            self._resource = rm.open_resource(self._resource_name)
        except pyvisa.errors.VisaIOError:
            self._resource = None
            raise IOError
        
    def close(self):
        if self._resource != None:
            self._resource.close()
            self._resource = None
            
    def reset(self):
        self.write("*RST")
        self.write("HEADER 1")
        
    def write(self, command):
        return self._resource.write(command)
    
    def query(self, command):
        return self._resource.query(command)
        
        