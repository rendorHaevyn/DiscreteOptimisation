# set CWD
import os

def setwd():
    cwd = '/'.join(__file__.split('/')[:-1])
    os.chdir(cwd)
    print(f'Set Working Directory to: {cwd}')