#!/bin/bash
source $(dirname "$0")/config.sh

# run the jetty server in the background
mvn jetty:run -f $JMC_THIRD_PARTY/pom.xml &
jetty_pid=$!;

# Addresses https://github.com/aptmac/jmc-qa/issues/16
# The RCP application will not display if not given mouse focus.
# Add a cursor placement for 0, 0 in the RCP application setup.
sed -i '53 i 		display.setCursorLocation(0, 0);' $RCP_APPLICATION_JAVA

# Addresses https://github.com/aptmac/jmc-qa/issues/22
# MBeanBrowserTabTest.testValueFontSize() asserts that a font can be resized to the system default height.
# However, the test uses a hardcoded value of 11 to test against, and the default for Travis & Jenkins is 10.
sed -i 's/DEFAULT_FONT_HEIGHT = 11/DEFAULT_FONT_HEIGHT = JFaceResources.getDefaultFont().getFontData()[0].getHeight()/' $MBEAN_BROWSER_TAB_TEST

# run ui tests
mvn verify -P uitests -Dspotbugs.skip=true -f $JMC_ROOT/pom.xml || { kill $jetty_pid; exit 1; };

# kill the jetty process
kill $jetty_pid;
