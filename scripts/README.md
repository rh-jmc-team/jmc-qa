# Scripts

## 1_setup_jmc.py

This script downloads and builds Java Mission Control (JMC). It gets third party dependencies and puts them into a local p2 repo that is served by Jetty in a child process. While the p2 repo is available on localhost, JMC is built as outlined in the source documentation.

Source documentation: http://hg.openjdk.java.net/jmc/jmc/file/9aa7085f938b/README.md#l177

## 2_setup_jemmy.py

This script downloads and builds Jemmy, the UI testing library used in the JMC uitests. Jemmy is built and it's generated `.jar` files are transfered into the local JMC repo.

Source documentation: http://hg.openjdk.java.net/jmc/jmc/file/9aa7085f938b/README.md#l233

## 3_run_ui_tests.py

This script runs the JMC uitests now that Jemmy is setup.

Source documentation: http://hg.openjdk.java.net/jmc/jmc/file/9aa7085f938b/README.md#l245
