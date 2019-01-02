#!/bin/bash

JMC_QA=~/workspace/jmc-qa
JEMMY_ROOT=$JMC_QA/jemmy
JEMMY_REPO=http://hg.openjdk.java.net/code-tools/jemmy/v3/
JMC_ROOT=$JMC_QA/jmc
JMC_JEMMY_LIB=$JMC_ROOT/application/uitests/org.openjdk.jmc.test.jemmy/lib/
MCJEMMYTESTBASE=$JMC_ROOT/application/uitests/org.openjdk.jmc.test.jemmy/src/test/java/org/openjdk/jmc/test/jemmy/MCJemmyTestBase.java

# jar output directories
JEMMY_AWTINPUT=$JEMMY_ROOT/core/JemmyAWTInput/target
JEMMY_BROWSER=$JEMMY_ROOT/core/JemmyBrowser/target
JEMMY_CORE=$JEMMY_ROOT/core/JemmyCore/target
JEMMY_SWT=$JEMMY_ROOT/SWT/JemmySWT/target

# if a jemmy folder already exists, remove it prior to cloning
if [ -d $JEMMY_ROOT ]; then
    rm -r $JEMMY_ROOT;
fi

# clone the jemmy repo
hg clone $JEMMY_REPO $JEMMY_ROOT  || { exit 1; };

# build jemmy
mvn clean package -DskipTests --quiet -f $JEMMY_ROOT || { exit 1; };

# create the jemmy lib folder
mkdir $JMC_JEMMY_LIB;

# transfer the exported jars to jmc
for jar in `ls $JEMMY_AWTINPUT | grep .jar`; do
  mv $JEMMY_AWTINPUT/$jar $JMC_JEMMY_LIB;
done

for jar in `ls $JEMMY_BROWSER | grep .jar`; do
  mv $JEMMY_BROWSER/$jar $JMC_JEMMY_LIB;
done

for jar in `ls $JEMMY_CORE | grep .jar`; do
  mv $JEMMY_CORE/$jar $JMC_JEMMY_LIB;
done

for jar in `ls $JEMMY_SWT | grep .jar`; do
  mv $JEMMY_SWT/$jar $JMC_JEMMY_LIB;
done

# increase the timeout for focusing JMC window
sed -i '86 s/sleep(10000)/sleep(50000)/' $MCJEMMYTESTBASE
