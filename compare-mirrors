#!/usr/bin/env python

#######################
#
# Coded by Joshua Strot
#
# joshuastrot@gmail.com
#
#######################

import argparse
from utilities_ import *
from sys import exit, argv
from os import environ, path

def beginComparing(yamlFormat, updateDB):
    configuration = data_parser.parseConfiguration(xdgConfig)
    
    if updateDB:
        web_tools.updateDB(yamlFormat, configuration, xdgCache)
    
    data_parser.checkCache(xdgCache, configuration)
    databases = data_parser.prepareDatabases(yamlFormat, configuration, xdgCache)
    versionChanges = data_parser.compareDatabases(yamlFormat, configuration, databases)
    control_output.output(yamlFormat, configuration, versionChanges)

#Check for XDG configuration path
if environ.get("XDG_CONFIG_HOME"):
    xdgConfig = environ["XDG_CONFIG_HOME"]
else:
    xdgConfig = path.expanduser("~") + "/.config"    

#Check for XDG cache path
if environ.get("XDG_CACHE_HOME"):
    xdgCache = environ["XDG_CACHE_HOME"]
else:
    xdgCache = path.expanduser("~") + "/.cache"
        
#Set up the argument parser
parser = argparse.ArgumentParser(description='Compare the Manjaro and Arch repositories by downloading their databases.')
parser.add_argument('-u', "--update", action="store_true", help="Update the databases")
parser.add_argument('-c', "--compare", action="store_true", help="Dry run: Compare the databases without updating")
parser.add_argument('-y', "--yaml", action="store_true", help="Output in YAML")
parser.add_argument("--clear", action="store_true", help="Clear the databases")

#Output help if no argument is passed
if len(argv)==1:
    parser.print_help()
    exit(1)
    
#Parse args
args=parser.parse_args()

#Begin running program
if args.update:
    beginComparing(args.yaml, True)

if args.compare and not args.update:
    beginComparing(args.yaml, False)

if args.clear:
    data_parser.clear(args.yaml, xdgCache)
