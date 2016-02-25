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
    newfile.write("\nAdditional text inserted by Ed Young [@edwinyoung](https://www.github.com/edwinyoung)")

os.remove('README.md')
os.rename('newfile.txt','README.md')
