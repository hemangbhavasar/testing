# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:34:30 2019

@author: Kalyani-Hemang
"""

import os
import shutil

def remove_files(dir):
    path = (os.getcwd() + '\\' + dir + '\\')

    shutil.rmtree(path)
    os.mkdir(path)