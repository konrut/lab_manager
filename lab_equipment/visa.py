'''!
@package lab_equipment.visa
@date 22 sep 2016
@author Konrad Rutkowski
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
        super(LabEqVisa,self).__init__('scope')
        self.resource_name = resource_name
        self._resource = None        
        
    def open(self, resource_name = ''):
        if resource_name != '':
            self.resource_name = resource_name          
              
        try:
            rm = pyvisa.ResourceManager()
        except OSError:
            rm = pyvisa.ResourceManager('C:\\Windows\\system32\\visa32.dll')
  
        try:
            self._resource = rm.open_resource(self.resource_name)
            return 0
        except pyvisa.errors.VisaIOError:
            print('Available resources:')
            print(rm.list_resources())
            self._resource = None
            return -1
        
    def close(self):
        if self._resource != None:
            self._resource.close()
            self._resource = None
            
    def reset(self):
        self.write("*RST")
        self.write("HEADER 1")
        
    def get_resources(self):
        try:
            rm = pyvisa.ResourceManager()
        except OSError:
            rm = pyvisa.ResourceManager('C:\\Windows\\system32\\visa32.dll')
        return rm.list_resources()        
        
    def write(self, command):
        return self._resource.write(command)
    
    def query(self, command):
        return self._resource.query(command)
        
        