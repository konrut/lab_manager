'''
Created on 22 wrz 2016

@author: Konrad Rutkowski
'''
import lab_equipment.lab_eq_visa

#if __name__ == '__main__':
labEq1 = lab_equipment.lab_eq_visa.LabEqVisa()
labEq1.init();
labEq1.turn_on();
    