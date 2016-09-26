'''
Created on 22 wrz 2016

@author: Konrad Rutkowski
'''

import time
import lab_equipment.scope


#if __name__ == '__main__':

labEq1 = lab_equipment.scope.LabEqScope('USB0::0x0699::0x0401::C021704::INSTR')

labEq1.open()
labEq1.reset()

labEq1.config_channel(1, label = 'ch1', scale_vpdiv = 5, position_div = -2)
labEq1.config_channel(2 ,1 , 'ch2', 'AC', 5, 20e6, 2)
labEq1.config_trigger_edge(1, 'AC', 0, 1)
labEq1.acquire(0.001, 0.004, 1e6)

labEq1.close()
#slabEq1.reset()

#labEq1.write('ble')
'''
try:
    labEq1.init('USB0::0x0699::0x0401::C021704::INSTR')
except NotImplementedError:
    print('Here!')    
except:
    print('Oops! Something goes wrong!')
 '''       

print(labEq1.name)