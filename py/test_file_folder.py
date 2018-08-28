# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 01:41:33 2018

@author: 2014_Joon_IBS
"""

import os
 
folders = []
files = []
 
for entry in os.scandir('/'):
    if entry.is_dir():
        folders.append(entry.path)
    elif entry.is_file():
        files.append(entry.path)
 
print('Folders:')
print(folders)

####

import os
count = 0
with open('../'+'result_2.csv','w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['name', 'label'])
    for (dirpath, dirname, files) in os.walk(path):
        
        for filename in files:
            
       
            #ext = os.path.splitext(filename)[-1]
            a = os.path.splitext(path_sub)
            writer.writerow([filename.strip(),count])
        count+=1
        #if ext == '.jpg' and count%10==0:
        #print("%s/%s" % (path_2, filename))
    print(a)
    os.walk(path)