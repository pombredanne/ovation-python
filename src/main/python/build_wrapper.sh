#!/bin/bash

M2_REPO=$1
VERSION=$2

/usr/local/bin/virtualenv --distribute wrapper.build.venv
source wrapper.build.venv/bin/activate

pip install jcc

python -m jcc.__main__ \
--arch x86_64 \
--shared \
--version $VERSION  \
--python ovation \
--build \
--bdist \
--files separate \
--jar $M2_REPO/us/physion/ovation-core/2.0-SNAPSHOT/ovation-core-2.0-SNAPSHOT.jar \
--jar $M2_REPO/us/physion/ovation-api/2.0-SNAPSHOT/ovation-api-2.0-SNAPSHOT.jar \
--jar $M2_REPO/joda-time/joda-time/2.1/joda-time-2.1.jar \
--package java.lang \
--package java.util \
--classpath $M2_REPO/com/google/guava/guava/13.0.1/guava-13.0.1.jar \
--classpath $M2_REPO/org/slf4j/slf4j-api/1.7.2/slf4j-api-1.7.2.jar \
--classpath $M2_REPO/commons-lang/commons-lang/2.6/commons-lang-2.6.jar \
--classpath $M2_REPO/com/google/inject/guice/3.0/guice-3.0.jar  \
--classpath $M2_REPO/javax/inject/javax.inject/1/javax.inject-1.jar \
--classpath $M2_REPO/aopalliance/aopalliance/1.0/aopalliance-1.0.jar \
--rename \
us.physion.ovation.domain.dto.Project=OVProjectDto,\
us.physion.ovation.util.Types=OVTypes,\
us.physion.ovation.domain.dto.Group=OVGroupDto,\
us.physion.ovation.domain.dto.User=OVUserDto,\
us.physion.ovation.domain.dto.Experiment=OVExperimentDto,\
us.physion.ovation.values.Resource=OVResource \
--exclude us.physion.ovation.domain.impl.Project \
--exclude us.physion.ovation.domain.impl.User \
--exclude us.physion.ovation.domain.impl.Group \
--exclude us.physion.ovation.domain.impl.OwnedEntityBase \
--exclude us.physion.ovation.domain.impl.AnnotatableEntityBase \
--exclude us.physion.ovation.domain.impl.Experiment

deactivate

rm -rf wrapper.build.venv

# rename org.apache.commons.lang.enums.Enum=CLEnum 