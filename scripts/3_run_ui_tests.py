#!/usr/bin/env python3

import os
import subprocess

HOME = os.path.expanduser('~')
QA_ROOT = HOME+ '/workspace/jmc-qa/'
JMC_ROOT = QA_ROOT + 'jmc/'
JMC_UI_TESTS_DIR = JMC_ROOT + 'application/uitests/org.openjdk.jmc.console.uitest/src/test/java/org/openjdk/jmc/console/uitest/'

RUN_UI_TESTS = ['mvn', 'verify', '-P', 'uitests']
RUN_UI_TESTS_SKIP_SPOTBUGS = ['mvn', 'verify', '-P', 'uitests', '-Dspotbugs.skip=true']

def run_ui_tests():
  os.chdir(JMC_ROOT)
  subprocess.call(RUN_UI_TESTS_SKIP_SPOTBUGS)

def remove_failing_tests():
  os.chdir(JMC_ROOT)
  failing_tests = []
  # MBeanBrowserTabTest = JMC_UI_TESTS_DIR + 'MBeanBrowserTabTest.java' # Current fails at org.openjdk.jmc.console.uitest.MBeanBrowserTabTest
  # failing_tests.append(MBeanBrowserTabTest)
  for test in failing_tests:
    if os.path.isfile(test):
      os.remove(test)

def main():
  remove_failing_tests()
  run_ui_tests()

if __name__ == '__main__':
  main()
