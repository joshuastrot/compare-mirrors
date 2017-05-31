#!/usr/bin/bash

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
cp sort-repositories.py /usr/share/compare-mirrors
cp compare-mirrors.conf /usr/share/compare-mirrors
cp README.md /usr/share/compare-mirrors

echo "Copying the compare-mirrors executable"
cp compare-mirrors /usr/bin

echo "Making executable"
chmod +x /usr/bin/compare-mirrors
chmod +x /usr/share/compare-mirrors/sort-repositories.py



