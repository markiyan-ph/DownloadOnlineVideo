#!/usr/bin/python
import sys
import re
import subprocess


def runScript(name):
    link = raw_input('Link: ')
    matchLink = re.match(r'.+/segment', link)

    if matchLink:
        # print(matchLink.group())
        subprocess.check_call(['./downloadTS', name, matchLink.group()])
    else:
        print('SEGMENT NOT FOUND')


if len(sys.argv) > 1:
    name = str(sys.argv[1])
else:
    name = raw_input('Name: ')

runScript(name)
