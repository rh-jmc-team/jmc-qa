#!/usr/bin/env python3

import os, subprocess

HOME = os.path.expanduser('~')
SCRIPTS_ROOT = HOME + '/workspace/jmc-qa/scripts/'

def setup_jmc():
  return subprocess.call(['python3', SCRIPTS_ROOT + '1_setup_jmc.py'])

def setup_jemmy():
  return subprocess.call(['python3', SCRIPTS_ROOT + '2_setup_jemmy.py'])

def run_ui_tests():
  return subprocess.call(['python3', SCRIPTS_ROOT + '3_run_ui_tests.py'])

def main():
  if setup_jmc() != 0:
    raise Exception('Something happened attempting to setup JMC.')
  if setup_jemmy() != 0:
    raise Exception('Something happened attempting to setup Jemmy.')
  if run_ui_tests() != 0:
    raise Exception('Something happened attempting to verify uitests.')

if __name__ == '__main__':
  main()