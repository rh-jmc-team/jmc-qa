#!/bin/bash

JMC_QA=~/workspace/jmc-qa
JMC_ROOT=$JMC_QA/jmc
JMC_CORE=$JMC_ROOT/core
JMC_THIRD_PARTY=$JMC_ROOT/releng/third-party
JMC_CONSOLE_UITEST_DIR=$JMC_ROOT/application/uitests/org.openjdk.jmc.console.uitest
RCP_APPLICATION_FOLDER=$JMC_ROOT/application/org.openjdk.jmc.rcp.application
RCP_APPLICATION_JAVA=$RCP_APPLICATION_FOLDER/src/main/java/org/openjdk/jmc/rcp/application/Application.java
RCP_APPLICATION_PLUGIN_XML=$RCP_APPLICATION_FOLDER/plugin.xml
UITEST_POM=$JMC_ROOT/application/uitests/pom.xml

# run the jetty server in the background
mvn jetty:run -f $JMC_THIRD_PARTY/pom.xml &
jetty_pid=$!;

# add a cursor placement for 0, 0 in the RCP application setup
sed -i '53 i 		display.setCursorLocation(0, 0);' $RCP_APPLICATION_JAVA

# temp: ignore running the console.uitest
sed -i '47d' $UITEST_POM

# remove a conflicting Eclipse shortcut
sed -i '140d' $RCP_APPLICATION_PLUGIN_XML

# run ui tests
mvn verify -P uitests -Dspotbugs.skip=true -f $JMC_ROOT/pom.xml || { kill $jetty_pid; exit 1; };

# kill the jetty process
kill $jetty_pid;
