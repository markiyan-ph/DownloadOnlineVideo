#!/usr/bin/python3
import sys
import os
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


def runScript(name, filesAmount):
    # link = raw_input('Link: ')
    link = input('Link: ')
    matchLink = re.match(r'.+/segment', link).group()
    folderName = getFolderName(name)
    dirname = os.path.dirname(os.path.abspath(__file__))
    script = os.path.join(dirname, 'loadTS')

    if matchLink:
        # print(matchLink)
        subprocess.check_call([script, name, matchLink, folderName, filesAmount])
    else:
        print('SEGMENT NOT FOUND')


if len(sys.argv) > 2:
    name = str(sys.argv[1])
    files_amount = str(sys.argv[2])
else:
    files_amount = '550'
    if len(sys.argv) > 1:
        name = str(sys.argv[1])
    else:
        # name = raw_input('Name: ')
        name = input('Name: ')


runScript(name, files_amount)
