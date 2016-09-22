'''
Created on 22 wrz 2016

@author: Konrad Rutkowski
'''

import pyvisa
import lab_equipment.lab_eq

class LabEqVisa(lab_equipment.lab_eq.LabEq):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(LabEqVisa,self).__init__()
        
    def init(self):
        pass