#!/bin/bash

# Clone the JMC repo, build jmc-core and jmc
bash ./scripts/1_setup_jmc.sh

# Clone the Jemmy repo, build it, and move the resulting jars into jmc
bash ./scripts/2_setup_jemmy.sh

# Run the ui tests
bash ./scripts/3_run_ui_tests.sh
