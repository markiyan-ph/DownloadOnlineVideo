#!/usr/bin/python
import sys
import re
import subprocess


def getFolderName(name):
    result = ""
    try:
        result = re.match(r'^([a-zA-Z]+)', name).group()
    except ValueError:
        result = "Default"
    except AttributeError:
        result = "Default"

    return result


def runScript(name):
    link = raw_input('Link: ')
    matchLink = re.match(r'.+/segment', link).group()
    folderName = getFolderName(name)

    if matchLink:
        # print(matchLink.group())
        subprocess.check_call(['./loadTS', name, matchLink, folderName])
    else:
        print('SEGMENT NOT FOUND')


if len(sys.argv) > 1:
    name = str(sys.argv[1])
else:
    name = raw_input('Name: ')

runScript(name)
