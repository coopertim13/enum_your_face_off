#!/usr/bin/python3
import os
import argparse
import sys

header = """
   __                                                ___                  ___  __  __ 
  /__\ __  _   _ _ __ ___   /\_/\___  _   _ _ __    / __\_ _  ___ ___    /___\/ _|/ _|
 /_\| '_ \| | | | '_ ` _ \  \_ _/ _ \| | | | '__|  / _\/ _` |/ __/ _ \  //  // |_| |_ 
//__| | | | |_| | | | | | |  / \ (_) | |_| | |    / / | (_| | (_|  __/ / \_//|  _|  _|
\__/|_| |_|\__,_|_| |_| |_|  \_/\___/ \__,_|_|    \/   \__,_|\___\___| \___/ |_| |_|  
                                                                                      
FIND OPEN PORTS, GIVE THEM TO ME, AND I WILL FEED YOU INFO 'TILL YOUR FACE FALLS OFF!!
"""
print(header)

parser = argparse.ArgumentParser()
parser.add_argument("-i", metavar='<<ip>>', help="IP to scan")
parser.add_argument("-w", metavar='<<port1,port2>>', help="Ports running web services")
parser.add_argument("-f", metavar='<<port1,port2>>', help="Ports running ftp services")
args = parser.parse_args()

if len(sys.argv) <= 1 or not args.i:
	parser.print_help()
	sys.exit()

def web():
	print("web")

def ftp():
	print("ftp")

if(args.w):
	web()

if(args.f):
	ftp()

