#!/usr/bin/env python

#
# Coded by Joshua Strot
#
# E-Mail: joshuastrot@gmail.com
# URL: https://github.com/joshuastrot/compare-mirrors
#

def output(yamlFormat, configuration, versionDifferences):
    """
    Output the version differences. 
    """
    
    #Output format done here:
    if not yamlFormat:
        print("=> Version Changes")
    
        #Output all the versions in plain format
        for repository in configuration["Repositories"]:
            print("    => [" + repository + "] Version Changes")
            for packageName, packageVersions in versionDifferences[repository].items():
                print("        => %s-%s  ->  %s-%s" % (packageName, packageVersions[0], packageName, packageVersions[1]))
    else:
        # Yaml format:
        #Repository
        #    - Package name
        #        -Manjaro Version
        #        -Arch Version
        print("""# Output generated by compare-mirrors
# 
# Author: Joshua Strot
# URL: https://github.com/joshuastrot/compare-mirrors

        """)
        
        #Output in YAML format
        for repository in configuration["Repositories"]:
            print(repository + ":")
            for packageName, packageVersions in versionDifferences[repository].items():
                print("    - " + packageName + ":")
                print("        - \"" + packageVersions[0] + "\"")
                print("        - \"" + packageVersions[1] + "\"")
