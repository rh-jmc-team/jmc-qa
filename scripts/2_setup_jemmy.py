#!/usr/bin/env python3

import glob
import os
import shutil
import subprocess

HOME = os.path.expanduser('~')
QA_ROOT = HOME + '/workspace/jmc-qa/'
JEMMY_ROOT = QA_ROOT + 'jemmy/'
JMC_ROOT = QA_ROOT + 'jmc/'
JMC_JEMMY_LIB = JMC_ROOT + '/application/uitests/org.openjdk.jmc.test.jemmy/lib/'

JEMMY_REPO = 'http://hg.openjdk.java.net/code-tools/jemmy/v3/'
HG_CLONE_JEMMY = ['hg', 'clone', JEMMY_REPO, JEMMY_ROOT]

MVN_CLEAN_PACKAGE = ['mvn', 'clean', 'package'] # fails at the moment
MVN_CLEAN_PACKAGE_SKIP_TESTS = ['mvn', 'clean', 'package', '-DskipTests']

def clone_jemmy():
  if os.path.isdir(JEMMY_ROOT) is False:
    subprocess.call(HG_CLONE_JEMMY)

def build_jemmy():
  os.chdir(JEMMY_ROOT)
  subprocess.call(MVN_CLEAN_PACKAGE_SKIP_TESTS)

def transfer_jars():
  if not os.path.exists(JMC_JEMMY_LIB):
    os.makedirs(JMC_JEMMY_LIB)
  packages = ['core/JemmyAWTInput/', 'core/JemmyBrowser/', 'core/JemmyCore/', 'SWT/JemmySWT/']
  for package in packages:
    os.chdir(JEMMY_ROOT + package + 'target')
    for jar in glob.glob("*.jar"):
      shutil.copy(jar, JMC_JEMMY_LIB)
    
def main():
  clone_jemmy()
  build_jemmy()
  transfer_jars()

if __name__ == '__main__':
  main()
