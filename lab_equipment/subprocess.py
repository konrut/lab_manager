'''
Created on 28 wrz 2016

@author: Konrad Rutkowski
'''

import subprocess
import time

import lab_equipment


class LabEqSubprocess(lab_equipment.LabEq):
    '''
    classdocs
    '''

    def __init__(self, path = '', working_dir = ''):
        '''
        Constructor
        '''
        super(LabEqSubprocess,self).__init__()
        self.process = None
        self.log_file = None
        
        self.path = path
        if working_dir != '' and working_dir[len(working_dir)-1] != '/':
            working_dir = working_dir + '/'
        self.cwd = working_dir        
        
        self.stdin_leading_seq = '>> '        
        self.timeout_s = 1
        
    def open(self):
        
        if self.process != None:
            raise IOError
        
        if self.name != '':
            self.log_file = open(self.cwd + self.name + '.log','w+')
        else:
            self.log_file = open(self.cwd + 'stdout.log','w+')
        
        if self.cwd != '':
            cwd = self.cwd
        else:
            cwd = None
        self.process = subprocess.Popen(self.path, shell=False, stdin=subprocess.PIPE, stdout = self.log_file, universal_newlines = True, cwd = cwd)
        
        time_start = time.time()        
        while (time.time() - time_start) < self.timeout_s and not (0 < self.log_file.tell()):
            pass
        
        if self.process.poll() != None:
            raise IOError
        
    def close(self):
        if self.process == None:
            raise IOError
        
        self.process.terminate();
        
        try:
            self.process.wait(5)
        except:
            self.process.kill()
                
        if(self.process.poll() != None):
            self.process = None
            self.log_file.close()
            self.log_file = None
        else:
            raise IOError
    
    def write(self, input_cmd):
        
        if self.process == None:
            raise IOError
        
        self.log_file.write('\n' + self.stdin_leading_seq + input_cmd + '\n')
        self.log_file.flush()
        
        self.process.stdin.write(input_cmd + '\n')
        self.process.stdin.flush()        

    def query(self, query, timeout_s = -1):        
        if self.process == None:
            raise IOError
        
        if timeout_s < 0:
            timeout_s = self.timeout_s
        
        self.log_file.write('\n' + self.stdin_leading_seq + query + '\n')
        self.log_file.flush()
        out_start = self.log_file.tell()
        
        self.process.stdin.write(query + '\n')
        self.process.stdin.flush()
        
        time_start = time.time()
        
        while (time.time() - time_start) < timeout_s and not (out_start < self.log_file.tell()):
            pass
        
        self.log_file.seek(out_start)
        return self.log_file.read()
        