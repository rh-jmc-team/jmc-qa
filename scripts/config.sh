# repos
JMC_REPO=http://hg.openjdk.java.net/jmc/jmc/
JEMMY_REPO=http://hg.openjdk.java.net/code-tools/jemmy/v3/

# jmc
JMC_QA=$(dirname "$0")/../
JMC_ROOT=$JMC_QA/jmc
JMC_CORE=$JMC_ROOT/core
JMC_THIRD_PARTY=$JMC_ROOT/releng/third-party

# jemmy
JEMMY_ROOT=$JMC_QA/jemmy
JMC_JEMMY_LIB=$JMC_ROOT/application/uitests/org.openjdk.jmc.test.jemmy/lib/

# jemmy jar output directories
JEMMY_AWTINPUT=$JEMMY_ROOT/core/JemmyAWTInput/target
JEMMY_BROWSER=$JEMMY_ROOT/core/JemmyBrowser/target
JEMMY_CORE=$JEMMY_ROOT/core/JemmyCore/target
JEMMY_SWT=$JEMMY_ROOT/SWT/JemmySWT/target

# ui test 
MBEAN_BROWSER_TAB_TEST=$JMC_ROOT/application/uitests/org.openjdk.jmc.console.uitest/src/test/java/org/openjdk/jmc/console/uitest/MBeanBrowserTabTest.java
RCP_APPLICATION_JAVA=$JMC_ROOT/application/org.openjdk.jmc.rcp.application/src/main/java/org/openjdk/jmc/rcp/application/Application.java
