#!/usr/bin/env python

#
# Coded by Joshua Strot
#
# E-Mail: joshuastrot@gmail.com
# URL: https://github.com/joshuastrot/compare-mirrors
#

from os import makedirs, path
from urllib import request

def updateDB(outFormat, configuration, xdgCache):
    """
        Update the databases and parse them into usable format.
    """
    
    #Make necessary directories, provided not already present
    if not path.isdir(xdgCache + "/compare-mirrors/manjaro") or not path.isdir(xdgCache + "/compare-mirrors/arch"):
        makedirs(xdgCache + "/compare-mirrors/manjaro", exist_ok=True)
        makedirs(xdgCache + "/compare-mirrors/arch", exist_ok=True)
    
    if not outFormat:
        print("=> Downloading the databases from the Manjaro Mirror")
    
    #Download the Manjaro repositories
    for repository in configuration["Repositories"]:
        if not outFormat:
            print("    => Downloading " + repository)

        request.urlretrieve(configuration["ManjaroMirror"] + configuration["Branch"] + "/" + repository.split("-")[0] + "/" + \
            repository.split("-")[1] + "/" + repository.split("-")[0] + ".db", xdgCache + "/compare-mirrors/manjaro/" + \
            repository.split("-")[0] + "-" + repository.split("-")[1] + ".db")
    
    if not outFormat:
        print("=> Downloading the databases from the Arch Mirror")
    
    #Download the Arch repositories
    for repository in configuration["Repositories"]:
        if not outFormat:
            print("    => Downloading " + repository)
        
        request.urlretrieve(configuration["ArchMirror"] + repository.split("-")[0] + "/os/" + repository.split("-")[1] + \
            "/" + repository.split("-")[0] + ".db", xdgCache + "/compare-mirrors/arch/" + repository.split("-")[0] + "-" + \
            repository.split("-")[1] + ".db")
   
