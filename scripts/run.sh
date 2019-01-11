#!/bin/bash

# Clone the JMC repo, build jmc-core and jmc
bash $(dirname "$0")/1_setup_jmc.sh || { echo "Failed to build JMC."; exit 1; };

# Clone the Jemmy repo, build it, and move the resulting jars into jmc
bash $(dirname "$0")/2_setup_jemmy.sh || { echo "Failed to setup Jemmy."; exit 1; };

# Run the ui tests
bash $(dirname "$0")/3_run_ui_tests.sh || { echo "Failed to run UI tests."; exit 1; };
