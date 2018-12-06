#!/bin/bash

JMC_QA=~/workspace/jmc-qa
JMC_ROOT=$JMC_QA/jmc
JMC_CORE=$JMC_ROOT/core
JMC_THIRD_PARTY=$JMC_ROOT/releng/third-party
JMC_REPO=http://hg.openjdk.java.net/jmc/jmc/

# if a jmc folder already exists, remove it prior to cloning
if [ -d $JMC_ROOT ]; then
    rm -r $JMC_ROOT;
fi

# clone the jmc repo
hg clone $JMC_REPO $JMC_ROOT || { exit 1; };

# setup the p2 repository
mvn p2:site -f $JMC_THIRD_PARTY/pom.xml || { exit 1; };

# run the jetty server in the background
mvn jetty:run -f $JMC_THIRD_PARTY/pom.xml &
jetty_pid=$!;

# build jmc-core
mvn clean install -f $JMC_CORE/pom.xml || { exit 1; };

# build jmc
mvn package -f $JMC_ROOT/pom.xml || { exit 1; };

# kill the jetty process
kill $jetty_pid;
