#!/usr/bin/python
# encoding=utf-8


from __future__ import print_function
import sys
import argparse
import base64
from arc4 import ARC4

ALLOW_COMMAND_LIST=['encode','decode']

def parse_and_define_params():
    parser=argparse.ArgumentParser()
    parser.add_argument('command',type=str,help='command:%s'%('/'.join(ALLOW_COMMAND_LIST)))
    parser.add_argument('-c','--content',required=False,type=str,action='store',help='content')
    parser.add_argument('-p','--password',required=True,type=str,action='store',help='password')
    return parser.parse_args()

if __name__ != '__main__':
    print 'Do not support the script as library.'
    exit()
params=parse_and_define_params()
if params.command not in ALLOW_COMMAND_LIST:
   print 'cannot recognise your command(%s)'%(params.command)
   exit()
content=params.content
if not content or len(content)<=0:
   print '>'
   content=sys.stdin.readline()
print "Recomfirm your inputs:[password]=%s [content]=%s"%(params.password,content)

cipher=ARC4(params.password)
output=None
if params.command=='encode':
   output=base64.b64encode(cipher.encrypt(content))
else:
   output=cipher.decrypt(base64.b64decode(content))
print output