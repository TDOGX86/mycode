#!/usr/bin/env python3
import shutil
import os

# The following line will rename a file

os.chdir('/home/student/mycode/')
os.chdir('/home/student/mycode/')


xname = input('What is the new name for kerrigan.obj? ')

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

