#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from subprocess import Popen, PIPE
file = "0_ea-2a_1108.pdf" #provide the pdf filename
command_to_execute = 'python pdfid.py ' + 'benign_files\Benign\Ben01\\'+file
print(command_to_execute)
stdout = Popen(command_to_execute, shell=True, stdout=PIPE).stdout
data=stdout.readlines()
print(data)

