'''
Created on 26 wrz 2016

@author: Konrad Rutkowski
'''

import lab_equipment.visa


class LabEqScope(lab_equipment.visa.LabEqVisa):
    '''
    classdocs
    '''
    
    def __init__(self, resource_name):
        '''
        Constructor
        '''
        super(LabEqScope,self).__init__(resource_name)
        
    def config_channel(self, \
                          channel_no = 1, \
                          enable = 1, \
                          label = '', \
                          coupling = 'DC', \
                          scale_vpdiv = 1, \
                          bandwidth_hz = 'Full', \
                          position_div = 0):

        self.write('SELECT:CH' + str(channel_no) + ' ' + str(enable))
        
        if enable:
            self.write('CH' + str(channel_no) + ':LABEL \'' + label + '\'')
            self.write('CH' + str(channel_no) + ':COUPLING ' + coupling)
            self.write('CH' + str(channel_no) + ':SCALE ' + str(scale_vpdiv))
            self.write('CH' + str(channel_no) + ':POSITION ' + str(position_div))
            self.write('CH' + str(channel_no) + ':BANDWIDTH ' + str(bandwidth_hz))
            
    def config_trigger_edge(self, \
                          channel_no = 1, \
                          coupling = 'DC', \
                          is_rising_slope = 1, \
                          treshold_v = 0, \
                          mode = 'NORMAL'):       
        self.write('TRIG:A:TYPE EDGE')
        self.write('TRIG:A:EDGE:COUPLING ' + coupling)
        self.write('TRIG:A:EDGE:SOURCE CH' + str(channel_no))
        self.write('TRIG:A:LEVEL ' + str(treshold_v))
        self.write('TRIG:A:MODE ' + mode)
    
        if is_rising_slope:
            self.write('TRIG:A:EDGE:SLOPE RISE')
        else:
            self.write('TRIG:A:EDGE:SLOPE FALL')
            
    def acquire(self, scale_spdiv, delay_s = 0, recordlength = 10000, acquire_mode = 'SAMPLE'):
        self.write('HOR:SCALE ' + str(scale_spdiv))
        self.write('HOR:DELAY:TIME ' + str(delay_s))
        self.write('HOR:RECORDLENGTH ' + str(recordlength))
        self.write('ACQ:MODE ' + acquire_mode)
        
        self.write('ACQ:STOPAfter SEQ')
        self.write('ACQ:STATE RUN')

    def get_data(self):
        return None