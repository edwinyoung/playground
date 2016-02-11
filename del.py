#!/usr/bin/env python
import os


with open('README.md') as oldfile, open('newfile.txt', 'w') as newfile:
    for line in oldfile:
        if "===" in line:
             print line
        elif "<<<<" in line:
             print line
        elif ">>>>" in line:
             print line
        else:
        	 newfile.write(line)

os.remove('README.md')
os.rename('newfile.txt','README.md')