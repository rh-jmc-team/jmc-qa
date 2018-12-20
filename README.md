# JMC QA [![Build Status](https://travis-ci.org/aptmac/jmc-qa.svg?branch=master)](https://travis-ci.org/aptmac/jmc-qa)

Collection of scripts to download and setup Java Mission Control (JMC), setup the Jemmy ui test library, and run tests (unit & uitests).

Note: these instructions and scripts currently apply to the Fedora OS and may require adjustments to run properly otherwise.

## Requirements

1. mercurial
2. maven
3. openjfx (supplied by the `java-1.8.0-openjdk-openjfx` package)

On Fedora this can be accomplished with: `sudo dnf install mercurial maven java-1.8.0-openjdk-openjfx`

### (Optional) Virtual Displays

The ui tests requires control of the screen's cursor, and will interact with many components of the test application. As a result, the user must not move their mouse during the ui tests otherwise the motion may cause the tests to fail. This can be particularly annoying because it can take anywhere from 5 to 10 minutes for the tests to complete.

As a work around I run the QA scripts using a virtual display (this is how I have Travis & Jenkins configured).

- `Xvnc` (https://linux.die.net/man/1/xvnc)
- `vncserver` (https://linux.die.net/man/1/vncserver)
- `vncviewer` (https://linux.die.net/man/1/vncviewer)

`Xvnc` is based on the standard X server, but used a virtual display. This allows applications to display themselves as they would on your monitor, but you can think of them as running in the background. This is particularly useful for the uitests because it allows the user to retain their cursor and not have to sacrifice their screen to the tests. Setting up and running the virtual display can be taken care of by the `vncserver` command, in which you will need to specify the display number and optional parameters.

- e.g., `vncserver :42` will start a virtual display on display number 42

Next, update the environment variable `$DISPLAY` to use this new display number by default. This will allow the scripts to be run in the virtual display. The default display number on Linux is usually `:0`, so once you're done with the virtual display you may want to revert the display number.

- e.g., `export DISPLAY=:42`

Lastly, it may be useful to see what the application is doing in the virtual display. This can be helpful for seeing why ui tests or failing, or forcing an application to open in a consistent location (I added the vnc display number to my JMC RCP config for example). The virtual display can be opened using the `vncviewer` command.

- e.g., `vncviewer :42`

## Running the scripts

This repo includes three bash scripts, each responsible for a different step of the QA framework. A master script has also been included, that will run the three scripts sequentially.

- e.g., `bash scripts/run.sh`
