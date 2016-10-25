#!/usr/bin/env python

import os

topdir = '.'

exten = '.txt'
logname = 'findfiletype.log'

results = str()

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            results += '%s\n' % os.path.join(dirpath, name)

with open(logname, 'w') as logfile:
    logfile.write(results)
