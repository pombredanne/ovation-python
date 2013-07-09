#!/usr/bin/env python

import sys
import subprocess
import os
import os.path
import shutil

    
def dependency_list(pom_path='pom.xml'):
    output_path = "maven.classpath.txt"
    subprocess.check_call(["mvn", "-f", pom_path, "dependency:build-classpath", "-Dmdep.outputFile={0}".format(output_path)], shell=True)
    
    with open(output_path) as f:
        classpath = f.read()
    
    return classpath.split(os.pathsep)
    
def copy_dependencies(pom_path="pom.xml", dest=None):
    if dest:
        if not os.path.isdir(dest):
            os.makedirs(dest)
        
        for p in dependency_list(pom_path=pom_path):
            shutil.copy(p, dest)
