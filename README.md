# JMC QA [![Build Status](https://travis-ci.org/aptmac/jmc-qa.svg?branch=master)](https://travis-ci.org/aptmac/jmc-qa)

Collection of scripts to download and setup Java Mission Control (JMC), setup the Jemmy ui test library, and run tests (unit & uitests).

Note: these instructions and scripts currently apply to the Fedora OS and may require adjustments to run properly otherwise.

## Requirements

1. mercurial
2. maven
3. openjfx (supplied by the `java-1.8.0-openjdk-openjfx` package)

On Fedora this can be accomplished with: `sudo dnf install mercurial maven java-1.8.0-openjdk-openjfx`

## Running the scripts

The scripts are written using Python 3, and will need to be executed accordingly. 

- e.g., `python3 1_setup_jmc.py`

The scripts are named to indicate the order they should be executed in.
