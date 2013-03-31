#!/usr/bin/env python

import sys
import subprocess
from dependencies import dependency_list, jar_list, include_list

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
]

def main(argv=sys.argv):
    
    version = argv[1]
    pom = argv[2]
    
    args = ["python", "-m", "jcc.__main__", 
            "--arch", "x86_64", 
            "--version", version,
            "--python", "ovation",
            "--build",
            "--bdist",
            "--files", "separate",
            "--package", "java.lang",
            "--package", "java.util"]
    
    deps = dependency_list(pom)

    for j in jar_list(deps):
        args.append("--jar")
        args.append(j)
    
    for j in include_list(deps):
        args.append("--include")
        args.append(j)
        
    # for c in EXCLUDES:
    #     args.append("--exclude")
    #     args.append(c)
        
    renames = dict(((c, c.replace('.','_')) for c in RENAMES))
    args.append("--rename")
    rename_entries = ["{0}={1}".format(k,v) for (k,v) in renames.iteritems()]
    args.append(",".join(rename_entries))
    
    
    print("GENERATING WRAPPER...")
    
    print " ".join(args)
    
    subprocess.check_call(args, stderr=subprocess.STDOUT, stdout=subprocess.STDOUT)
    

if __name__ == '__main__':
    main()

# python -m jcc.__main__ \
# --arch x86_64 \
# --shared \
# --version $VERSION  \
# --python ovation \
# --build \
# --bdist \
# --files separate \
# --jar $M2_REPO/us/physion/ovation-core/2.0-SNAPSHOT/ovation-core-2.0-SNAPSHOT.jar \
# --jar $M2_REPO/us/physion/ovation-api/2.0-SNAPSHOT/ovation-api-2.0-SNAPSHOT.jar \
# --jar $M2_REPO/joda-time/joda-time/2.1/joda-time-2.1.jar \
# --package java.lang \
# --package java.util \
# --include $M2_REPO/us/physion/ovation-couch/2.0-SNAPSHOT/ovation-couch-2.0-SNAPSHOT.jar \
# --include $M2_REPO/com/google/guava/guava/13.0.1/guava-13.0.1.jar \
# --include $M2_REPO/org/slf4j/slf4j-api/1.7.2/slf4j-api-1.7.2.jar \
# --include $M2_REPO/commons-lang/commons-lang/2.6/commons-lang-2.6.jar \
# --include $M2_REPO/com/google/inject/guice/3.0/guice-3.0.jar  \
# --include $M2_REPO/javax/inject/javax.inject/1/javax.inject-1.jar \
# --include $M2_REPO/aopalliance/aopalliance/1.0/aopalliance-1.0.jar \
# --include $M2_REPO/com/google/inject/extensions/guice-assistedinject/3.0/guice-assistedinject-3.0.jar \
# --include $M2_REPO/org/ektorp/org.ektorp/1.3.0/org.ektorp-1.3.0.jar \
# --include $M2_REPO/org/apache/httpcomponents/httpclient/4.2.1/httpclient-4.2.1.jar \
# --include $M2_REPO/org/apache/httpcomponents/httpcore/4.2.1/httpcore-4.2.1.jar \
# --include $M2_REPO/org/apache/commons/commons-compress/1.0/commons-compress-1.0.jar \
# --include $M2_REPO/us/physion/osx-keychain-java/1.0-SNAPSHOT/osx-keychain-java-1.0-SNAPSHOT.jar \
# --include $M2_REPO/org/codehaus/jackson/jackson-mapper-asl/1.9.7/jackson-mapper-asl-1.9.7.jar \
# --include $M2_REPO/org/codehaus/jackson/jackson-core-asl/1.9.7/jackson-core-asl-1.9.7.jar \
# --rename \
# us.physion.ovation.domain.dto.Project=OVProjectDto,\
# us.physion.ovation.util.Types=OVTypes,\
# us.physion.ovation.domain.dto.Group=OVGroupDto,\
# us.physion.ovation.domain.dto.User=OVUserDto,\
# us.physion.ovation.domain.dto.Experiment=OVExperimentDto,\
# us.physion.ovation.values.Resource=OVResource \
# --exclude us.physion.ovation.domain.impl.Project \
# --exclude us.physion.ovation.domain.impl.User \
# --exclude us.physion.ovation.domain.impl.Group \
# --exclude us.physion.ovation.domain.impl.OwnedEntityBase \
# --exclude us.physion.ovation.domain.impl.AnnotatableEntityBase \
# --exclude us.physion.ovation.domain.impl.Experiment