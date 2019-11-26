from sw_ide import *
from keil_ide import *
from iar_ide import *
import os, re, platform, string,time,socket,datetime
import subprocess,fnmatch
import serial
import sys
import serial.tools.list_ports
from time import sleep

#from distutils.version import LooseVersion, StrictVersion
#import xml.etree.ElementTree as ElementTree
dir=os.chdir("../../Projects")
dir=os.getcwd()
for projects in ['WriteURI']:
    for obj in [SW4STM32()] :
            store=["empty","empty","empty","empty"]
            store=obj.compileByName(dir,projects)
