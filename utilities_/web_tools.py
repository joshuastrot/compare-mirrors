#!/usr/bin/env python

#   This file is part of Compare-Mirrors - <http://github.com/joshuastrot/compare-mirrors>
#
#   Copyright Compare-Mirrors, Joshua Strot <joshuastrot@gmail.com>
#
#   Compare-Mirrors is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Compare-Mirrors is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Compare-Mirrors. If not, see <http://www.gnu.org/licenses/>.

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
   
