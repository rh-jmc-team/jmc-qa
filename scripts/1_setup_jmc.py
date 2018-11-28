#!/usr/bin/env python3

import os
import subprocess

HOME = os.path.expanduser('~')
QA_ROOT = HOME+ '/workspace/jmc-qa/'
JMC_ROOT = QA_ROOT + 'jmc/'
JMC_CORE = JMC_ROOT + 'core/'
JMC_THIRD_PARTY = JMC_ROOT + 'releng/third-party/'
JMC_TARGET_LINUX = JMC_ROOT + 'target/products/org.openjdk.jmc/linux/gtk/x86_64/'

JMC_REPO = 'http://hg.openjdk.java.net/jmc/jmc/'
HG_CLONE_JMC = ['hg', 'clone', JMC_REPO, JMC_ROOT]

MVN_CLEAN_INSTALL = ['mvn', 'clean', 'install']
MVN_PACKAGE = ['mvn', 'package']

MVN_P2_SITE = ['mvn', 'p2:site']
MVN_JETTY_RUN = ['mvn', 'jetty:run']

def clone_repo():
  return subprocess.call(HG_CLONE_JMC)

def p2site():
  os.chdir(JMC_THIRD_PARTY)
  return subprocess.call(MVN_P2_SITE)

def jetty_run():
  os.chdir(JMC_THIRD_PARTY)
  proc = subprocess.Popen(MVN_JETTY_RUN) # async
  return proc
  
def build_jmc_core():
  os.chdir(JMC_CORE)
  return subprocess.call(MVN_CLEAN_INSTALL)

def build_jmc():
  os.chdir(JMC_ROOT)
  return subprocess.call(MVN_PACKAGE)

def main():
  if clone_repo() != 0:
    raise Exception('Unable to clone JMC!')
  if p2site() != 0:
    raise Exception('Unable to setup p2 repository!')
  proc = jetty_run()
  if build_jmc_core() != 0:
    raise Exception('Unable to build JMC Core!')
  proc.kill()
  if build_jmc() != 0:
    raise Exception('Unable to build JMC!')

if __name__ == '__main__':
  main()
