'''
Created on 22 wrz 2016

@author: Konrad Rutkowski
'''
import lab_equipment.visa


#if __name__ == '__main__':
labEq1 = lab_equipment.visa.LabEqVisa()

labEq1.write('ble')

try:
    labEq1.init('USB0::0x0699::0x0401::C021704::INSTR')
except NotImplementedError:
    print('Here!')    
except:
    print('Oops! Something goes wrong!')
        

print(labEq1.name)