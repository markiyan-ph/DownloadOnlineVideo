#!/usr/bin/python
import sys
import re
import subprocess


def runScript(name, link):
    if matchLink:
        # print(matchLink.group())
        subprocess.check_call(['./downloadTS', name, link])
    else:
        print('SEGMENT NOT FOUND')


name = str(sys.argv[1])
link = raw_input('Link: ')
matchLink = re.match(r'.+/segment', link)

if name:
    runScript(name, matchLink.group())
else:
    name = raw_input('Name: ')
    runScript(name, matchLink.group())
