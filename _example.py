'''
Created on 22 wrz 2016

@author: Konrad Rutkowski
'''

import matplotlib.pyplot
import time

import lab_equipment.subprocess
import lab_equipment.scope


#if __name__ == '__main__':

# labEq1 = lab_equipment.scope.LabEqScope('USB0::0x0699::0x0401::C021704::INSTR')
#  
# labEq1.open()
# labEq1.reset()
#  
# labEq1.config_channel(1, label = 'ch1', scale_vpdiv = 1, position_div = -2)
# labEq1.config_channel(2 ,1 , 'ch2', 'AC', 1, 20e6, 2)
# labEq1.config_trigger_edge(1, 'AC', 0, 1)
# labEq1.acquire(0.001, 0.004, 1e4)
# time.sleep(2)
# data = labEq1.get_data([1,2])
# fig = matplotlib.pyplot.figure()
# matplotlib.pyplot.plot(data[0],data[1],'g',data[0], data[2],'r')
# matplotlib.pyplot.show()
#  
# labEq1.close()

labEq2 = lab_equipment.subprocess.LabEqSubprocess(\
            'D:/Dropbox/MyApplications/eclipse/lab_manager/_inputs/tmp.exe')
 
labEq2.open()
tmp = [labEq2.query('h'), labEq2.query('h')]
print(tmp)
print(labEq2.attrib)
#time.sleep(5)

labEq2.close()

