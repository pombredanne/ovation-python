#!/usr/bin/env python

import sys
import subprocess
import shutil
import os.path
from dependencies import dependency_list, jar_list, include_list

EXCLUDES = []


def main(argv=sys.argv):
    
    version = argv[1]
    pom = argv[2]
    mvn_opts = argv[3]
    
    args = ["python", "-m", "jcc.__main__", 
            "--arch", "x86_64", 
            "--version", version, 
            "--use_full_names",
            "--python", "ovation_api",
            "--build",
            "--bdist",
            "--package", "java.lang",
            "--package", "java.util", 
            "--package", "java.io",
            "--package", "java.net",
            "--package", "com.google.common.util.concurrent",
            "--package", "java.util.concurrent",
            "java.io.File",
            "java.net.URI",
            "java.net.URL",
            "com.google.common.util.concurrent.ListenableFuture",
            "com.google.common.util.concurrent.Futures",
            "com.google.inject.Module",
            "com.google.inject.Guice",
            "com.google.inject.Injector",
            "com.google.common.collect.Maps",
            "com.google.common.collect.Sets",
            ]

    deps = dependency_list(pom, mvn_opts=mvn_opts)

    for j in jar_list(deps):
        args.append("--jar")
        args.append(j)
    
    for j in include_list(deps):
        args.append("--include")
        args.append(j)
        
    for c in EXCLUDES:
        args.append("--exclude")
        args.append(c)
    
    
    print("GENERATING WRAPPER...")
    
    print(' ')
    print(' '.join(args))
    print(' ')
    print(' ')
    
    try:
        subprocess.check_call(args)
    except subprocess.CalledProcessError, ex:
        indent = "\t"
        if ex.output is not None:
            print(indent + "jcc output:")
            for l in ex.output.splitlines(True):
                print(indent*2 + l)
        
        raise
        
    

if __name__ == '__main__':
    main()
