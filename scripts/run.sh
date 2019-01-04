#!/bin/bash

# Clone the JMC repo, build jmc-core and jmc
bash $(dirname "$0")/1_setup_jmc.sh

# Clone the Jemmy repo, build it, and move the resulting jars into jmc
bash $(dirname "$0")/2_setup_jemmy.sh

# Run the ui tests
bash $(dirname "$0")/3_run_ui_tests.sh
