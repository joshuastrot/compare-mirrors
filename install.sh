#!/usr/bin/bash

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

if [ $EUID != 0 ]; then
    echo "This script needs to be ran as root! Exiting..."
    exit
fi

if [ "$1" == "-r" ] || [ "$1" == "--remove" ]; then
    echo "Uninstalling compare-mirrors..."
    rm -r /usr/share/compare-mirrors
    rm /usr/bin/compare-mirrors
    exit 1
fi

echo "Installing compare-mirrors..."

if [ ! -d "/usr/share/compare-mirrors" ]; then
    echo "Creating /usr/share/compare-mirrors"
    mkdir -p /usr/share/compare-mirrors
else
    echo "Could not install compare-mirrors... Are you sure it's not already installed? Exiting..."
    exit 1
fi

echo "Copying data to compare-mirrors directory."
cp -r utilities_ /usr/share/compare-mirrors
cp compare-mirrors.yaml /usr/share/compare-mirrors
cp compare-mirrors.py /usr/share/compare-mirrors

echo "Copying the compare-mirrors executable"
cp compare-mirrors /usr/bin

echo "Making executable"
chmod +x /usr/bin/compare-mirrors
chmod +x /usr/share/compare-mirrors/compare-mirrors.py



