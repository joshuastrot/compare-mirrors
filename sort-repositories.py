#!/usr/bin/python

################################
#
# Coded entirely by Joshua Strot
#
# joshuastrot@gmail.com
#
################################

from os import path
import subprocess

#Set some basic variables
DatabaseDirectory = path.expanduser("~") + "/.compare-mirrors"
ManjaroDirectory = DatabaseDirectory + "/manjaro/"
ArchDirectory = DatabaseDirectory + "/arch/"
Databases = ["core-i686", "core-x86_64", "extra-i686", "extra-x86_64", "community-i686", "community-x86_64", "multilib-x86_64"]

#Begin sorting files
for DB in Databases:
    #Load up the Database files
    DBFileManjaro = ManjaroDirectory + DB + ".lst"
    DBFileArch = ArchDirectory + DB + ".lst"
    
    with open(DBFileManjaro, "r") as f:
        ManjaroPackages = f.read().splitlines()
    
    with open(DBFileArch, "r") as f:
        ArchPackages = f.read().splitlines()
    
    #Begin parsing the databases.
    ManjaroPackagesNV = []
    for Package in ManjaroPackages:
        ManjaroPackagesNV.append(Package.rsplit("-", 2)[0])
    
    ArchPackagesNV = []
    for Package in ArchPackages:
        ArchPackagesNV.append(Package.rsplit("-", 2)[0])
    
    #Find new packages and packages with version changes.
    NewPackages = sorted(list(set(ArchPackages) - set(ManjaroPackages)))
    NewPackagesNV = sorted(list(set(ArchPackagesNV) - set(ManjaroPackagesNV)))
    
    print("    => [" + DB + "] New Packages in Arch")
    
    #Output all new packages in Arch repos.
    if NewPackagesNV:
        for Package in NewPackagesNV:
            for PackageFull in ArchPackages:
                if PackageFull.rsplit("-", 2)[0] == Package:
                    print("        " + PackageFull)
                    continue
    else:
        print("        None")
        
    print("\n    => [" + DB + "] Version Change")
        
    #Output all packages that have changed in versions. 
    #Uses vercmp to determine update or downgrade.
    if NewPackages:
        for Package in NewPackages:
            for PackageFull in ManjaroPackages:
                if PackageFull.rsplit("-", 2)[0] == Package.rsplit("-", 2)[0]:
                    Proc = subprocess.Popen(['/usr/bin/vercmp', PackageFull.rsplit("-", 2)[1] + "-" + PackageFull.rsplit("-", 2)[2], Package.rsplit("-", 2)[1] + "-" + Package.rsplit("-", 2)[2]], stdout=subprocess.PIPE)
                    VersionValue = Proc.stdout.read()
                    
                    if VersionValue.decode("utf-8").replace("\n", "") == "-1":
                        print("        Outdated: " + PackageFull + "  ->  Arch: " + Package)
    else:
        print("        None")
    print("")
