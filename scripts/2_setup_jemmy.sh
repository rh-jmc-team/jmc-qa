#!/bin/bash
source $(dirname "$0")/config.sh

# if a jemmy folder already exists, remove it prior to cloning
if [ -d $JEMMY_ROOT ]; then
    rm -r $JEMMY_ROOT;
fi

# clone the jemmy repo
hg clone $JEMMY_REPO $JEMMY_ROOT  || { exit 1; };

# revert Jemmy to the pre-package conflict revision
cd $JEMMY_ROOT;
hg update -r 7f267a1c3d63;
cd ..;

# build jemmy
mvn clean package -DskipTests --quiet -f $JEMMY_ROOT/pom.xml || { exit 1; };

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
