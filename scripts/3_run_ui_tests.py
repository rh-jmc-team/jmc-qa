#!/usr/bin/env python3

import os
import subprocess

HOME = os.path.expanduser('~')
QA_ROOT = HOME+ '/workspace/jmc-qa/'
JMC_ROOT = QA_ROOT + 'jmc/'
JMC_THIRD_PARTY = JMC_ROOT + 'releng/third-party/'
JMC_UI_TESTS_DIR = JMC_ROOT + 'application/uitests/org.openjdk.jmc.console.uitest/src/test/java/org/openjdk/jmc/console/uitest/'

MVN_JETTY_RUN = ['mvn', 'jetty:run']
MVN_VERIFY_UI_TESTS = ['mvn', 'verify', '-P', 'uitests']
MVN_VERIFY_UI_TESTS_SKIP_SPOTBUGS = ['mvn', 'verify', '-P', 'uitests', '-Dspotbugs.skip=true']

def jetty_run():
  os.chdir(JMC_THIRD_PARTY)
  proc = subprocess.Popen(MVN_JETTY_RUN, stdout=subprocess.PIPE) # async
  return proc

def run_ui_tests():
  os.chdir(JMC_ROOT)
  subprocess.call(MVN_VERIFY_UI_TESTS_SKIP_SPOTBUGS)

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
  proc = jetty_run()
  run_ui_tests()
  proc.kill()

if __name__ == '__main__':
  main()
