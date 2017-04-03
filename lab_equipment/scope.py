'''
@package lab_equipment.scope
@date 26 sep 2016
@author Konrad Rutkowski
'''

import lab_equipment.visa
import numpy
import time

class LabEqScope(lab_equipment.visa.LabEqVisa):
    '''
    classdocs
    '''
    
    def __init__(self, resource_name = ''):
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
    
    def acq_state(self):
        state_str = self.query('ACQuire:STATE?')
        state_str = state_str.split(' ')[1]
        return int(state_str)        
    
    def wait_for_acquire(self, timeout_sec = 0):
        t1 = time.clock()
        time_elapsed = 0
        
        while self.acq_state():
            time_elapsed = time.clock() - t1
            if time_elapsed > timeout_sec:
                return -1
        return 0

    def get_data(self, channel_list):
        
        if not isinstance(channel_list, list):
            channel_list = [channel_list]

        partLength = 1000
        
        res = self.query('HORIZONTAL:RECORDLENGTH?')
        recordLength = int(res.split(' ')[1])

        self.write(':DATa:SOUrce CH1')
        self.write(':WFMOutpre:ENCdg ASCii')
        self.write(':WFMOutpre:BYT_Nr 2')
        
        res = self.query(':WFMOutpre?')
        wfm_info = res.split(';')    
        xzero = float([x for x in wfm_info if x.find('XZE',0,3) > -1][0].split(' ')[1])
        xinc = float([x for x in wfm_info if x.find('XIN',0,3) > -1][0].split(' ')[1])

        if not xinc:            
            return []

        data_out = numpy.linspace(xzero,(recordLength-1)*xinc + xzero, recordLength)        
        
        if recordLength < partLength:
            partLength = recordLength       
    
        for channel_no in channel_list:
            self.write(':DATa:SOUrce CH' + str(channel_no))
            
            res = self.query(':WFMOutpre?')
            wfm_info = res.split(';')    
            ymult = float([x for x in wfm_info if x.find('YMU',0,3) > -1][0].split(' ')[1])
            yoff = float([x for x in wfm_info if x.find('YOF',0,3) > -1][0].split(' ')[1])
            
            data_tmp = []
            partDone = 0
            while partDone < recordLength:
                self.write(':DATa:START ' + str(partDone + 1))
                self.write(':DATa:STOP ' + str(partDone + partLength))            
                res = self.query(":CURVE?")
                res = res.split(' ')[1]
                data_tmp = numpy.hstack((data_tmp,[float(i) for i in res.split(',')]))                                      
                partDone = partDone + partLength
            
            data_tmp = (data_tmp - yoff).dot(ymult)    
            data_out = numpy.vstack((data_out, data_tmp))
        return data_out
    
    