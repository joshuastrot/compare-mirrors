#!/usr/bin/env python

import subprocess
from yaml import load
from urllib import request
from tarfile import open as tarOpen
from shutil import rmtree
from os import path
from sys import stderr

def parseConfiguration(xdgConfig):
    """
    Parse the configuration file and load settings.
    """
    
    #Load the configuration file
    try:
        with open(xdgConfig + "/compare-mirrors/compare-mirrors.yaml") as file:
            configFile = load(file)
            configPath = xdgConfig + "/compare-mirrors/compare-mirrors.yaml"
    except IOError as e:
        try:
            with open("/usr/share/compare-mirrors/compare-mirrors.yaml") as file:
                configFile = load(file)
                configPath = "/usr/share/compare-mirrors/compare-mirrors.yaml"
        except IOError as e:
            print("=> No configuration files could be found.", file=stderr)
            exit(1)
            
    
    return configFile


def checkCache(xdgCache, configuration):
    """
    Check the cache files to ensure that the needed ones are present
    """
    for repository in configuration["Repositories"]:
        if not path.isfile(xdgCache + "/compare-mirrors/manjaro/" + repository + ".db") or not path.isfile(xdgCache + "/compare-mirrors/manjaro/" + repository + ".db"):
            print("=> Cache's are corrupted. Please use the -u option instead", file=stderr)
            exit(1)
    

def prepareDatabases(yamlFormat, configuration, xdgCache):
    """
    Prepare the databases to be parsed.
    """
    
    if not yamlFormat:
        print("=> Parsing Databases")
    
    #Create the packages dictionary
    packagesDictionary = {
            "Manjaro": {},
            "Arch": {}
    }
    
    if not yamlFormat:
        print("    => Parsing Manjaro databases")
    
    #Generate Manjaro package list
    for repository in configuration["Repositories"]:
        database = tarOpen(xdgCache + "/compare-mirrors/manjaro/" + repository.split("-")[0] + "-" + repository.split("-")[1] + ".db")
        packageList = [package for package in database.getnames() if "/" not in package]
        packagesDictionary["Manjaro"][repository] = packageList

    if not yamlFormat:
        print("    => Parsing Arch databases")
    
    #Generate Arch package list
    for repository in configuration["Repositories"]:
        database = tarOpen(xdgCache + "/compare-mirrors/arch/" + repository.split("-")[0] + "-" + repository.split("-")[1] + ".db")
        packageList = [package for package in database.getnames() if "/" not in package]
        packagesDictionary["Arch"][repository] = packageList

    return packagesDictionary

def compareDatabases(yamlFormat, configuration, databases):
    """
    Compare the databases and output results
    """
    
    if not yamlFormat:
        print("=> Comparing databases")
    
    #Initialize the version change
    versionChanges = {}
    
    #Begin comparing the databases.
    for repository in configuration["Repositories"]:
        versionChanges[repository] = {}
        
        manjaroPackages = databases["Manjaro"][repository]
        archPackages = databases["Arch"][repository]
        
        #Generate list of all similarities
        uniqPackages = sorted(list(set(archPackages) - set(manjaroPackages)))
        
        #Main loops to compare the packages
        #iterates over unique packages, compares just the package names to identify the package in the manjaro
        #repository, and then compares those version numbers. 
        for package in uniqPackages:
            for packageFull in manjaroPackages:
                if packageFull.rsplit("-", 2)[0] == package.rsplit("-", 2)[0]:
                    versionValue = compareVersions(packageFull.rsplit("-", 2)[1] + "-" + packageFull.rsplit("-", 2)[2], \
                        package.rsplit("-", 2)[1] + "-" + package.rsplit("-", 2)[2])
                    if versionValue:
                        versionChanges[repository][package.rsplit("-", 2)[0]] = [packageFull.rsplit("-", 2)[1] + "-" + packageFull.rsplit("-", 2)[2], \
                        package.rsplit("-", 2)[1] + "-" + package.rsplit("-", 2)[2]]
        
    
    return versionChanges

def compareVersions(versionOne, versionTwo):
    """
    Compare two package versions using vercmp. Return True is versionTwo newer
    """
    
    #Use vercmp to verify that the packages in Manjaro are not actually newer. 
    Proc = subprocess.Popen(['/usr/bin/vercmp', versionOne, versionTwo], stdout=subprocess.PIPE)
    VersionValue = Proc.stdout.read()
    
    #Process vercmp output
    if VersionValue.decode("utf-8").replace("\n", "") == "-1":
        return True
    else:
        return False
    
def clear(yamlFormat, xdgCache):
    """
    Clear the caches
    """
    
    if not yamlFormat:
        print("=> Clearing all Cache files")
    
    if path.isdir(xdgCache + "/compare-mirrors"):
        rmtree(xdgCache + "/compare-mirrors")
    
