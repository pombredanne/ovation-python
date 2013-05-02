#!/usr/bin/env python

import sys
import subprocess
import shutil
import os.path
from dependencies import dependency_list, jar_list, include_list

EXCLUDES = []

# TODO generate these from excluded domain classes, and package prefixes
RENAMES = [
    'us.physion.ovation.util.Types',
    'us.physion.ovation.values.impl.Resource',
    'us.physion.ovation.domain.impl.Project',
    'us.physion.ovation.domain.impl.User',
    'us.physion.ovation.domain.impl.Group',
    'us.physion.ovation.domain.impl.OwnedEntityBase',
    'us.physion.ovation.domain.impl.AnnotatableEntityBase',
    'us.physion.ovation.domain.impl.Experiment',
    'us.physion.ovation.domain.impl.Epoch',
    'us.physion.ovation.domain.impl.Protocol',
    'us.physion.ovation.domain.impl.EpochGroup',
    'us.physion.ovation.domain.impl.EquipmentSetup',
    'us.physion.ovation.domain.impl.Measurement',
    'us.physion.ovation.domain.impl.Source',
    'us.physion.ovation.domain.impl.EntityBase',
    'us.physion.ovation.domain.impl.AnnotatableEntityBase',
    'us.physion.ovation.domain.impl.ProcedureEntityBase',
    'us.physion.ovation.domain.impl.TimelineEntityBase',
    'us.physion.ovation.domain.impl.AnalysisRecord',
    'us.physion.ovation.domain.impl.NumericMeasurement',
    'us.physion.ovation.domain.dto.EpochGroup',
    'us.physion.ovation.domain.dto.Project',
    'us.physion.ovation.domain.dto.Group',
    'us.physion.ovation.domain.dto.User',
    'us.physion.ovation.domain.dto.Experiment',
    'us.physion.ovation.domain.dto.Epoch',
    'us.physion.ovation.domain.dto.AnalysisRecord',
    'us.physion.ovation.domain.dto.EquipmentSetup',
    'us.physion.ovation.domain.dto.Measurement',
    'us.physion.ovation.domain.dto.Protocol',
    'us.physion.ovation.domain.dto.Source',
    'us.physion.ovation.domain.dto.ProcedureEntityBase',
    'us.physion.ovation.domain.dto.AnnotatableEntityBase',
    'us.physion.ovation.domain.dto.TimelineEntityBase',
    'us.physion.ovation.domain.dto.AnalysisRecord',
    'us.physion.ovation.couch.dto.EpochGroup',
    'us.physion.ovation.couch.dto.Project',
    'us.physion.ovation.couch.dto.Group',
    'us.physion.ovation.couch.dto.User',
    'us.physion.ovation.couch.dto.Experiment',
    'us.physion.ovation.couch.dto.Epoch',
    'us.physion.ovation.couch.dto.AnalysisRecord',
    'us.physion.ovation.couch.dto.EquipmentSetup',
    'us.physion.ovation.couch.dto.Measurement',
    'us.physion.ovation.couch.dto.Protocol',
    'us.physion.ovation.couch.dto.Source',
    'us.physion.ovation.couch.dto.EntityBase',
    'us.physion.ovation.couch.dto.ProcedureEntityBase',
    'us.physion.ovation.couch.dto.AnnotatableEntityBase',
    'us.physion.ovation.couch.dto.TimelineEntityBase',
    'us.physion.ovation.couch.dto.AnalysisRecord',
    'us.physion.ovation.couch.dto.ObjectivityPlacement',
    'us.physion.ovation.couch.dto.NumericMeasurement',
]

MODULES = [ "connection.py", "numpy.py", "testing.py" ]


def main(argv=sys.argv):
    
    version = argv[1]
    pom = argv[2]
    mvn_opts = argv[3]
    
    #Copy modules to build directory
    for m in MODULES:
        print("Copying " + m + " to build directory...")
        shutil.copy(os.path.join("../../src/main/python", m), m)
    
    args = ["python", "-m", "jcc.__main__", 
            "--arch", "x86_64", 
            "--version", version,
            "--python", "ovation",
            "--build",
            "--bdist",
            "--files", "separate",
            "--package", "java.lang",
            "--package", "java.util",
            "--module", "connection.py" #"../../src/main/python/connection.py"
            "java.util.HashMap",
            "java.util.HashSet",
            "com.google.common.collect.Maps",
            "com.google.common.collect.Sets",
            "--package", "us.physion.ovation.domain.mixin",
            "us.physion.ovation.domain.mixin.Taggable",
            "us.physion.ovation.domain.mixin.PropertyAnnotatable"]
    
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
        
    renames = dict(((c, '_' + c.replace('.','_')) for c in RENAMES))
    args.append("--rename")
    rename_entries = ["{0}={1}".format(k,v) for (k,v) in renames.iteritems()]
    args.append(",".join(rename_entries))
    
    
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
