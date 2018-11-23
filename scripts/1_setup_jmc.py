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
  if not os.path.isdir(JMC_ROOT):
    subprocess.call(HG_CLONE_JMC)

def p2site():
  os.chdir(JMC_THIRD_PARTY)
  subprocess.call(MVN_P2_SITE)

def jetty_run():
  os.chdir(JMC_THIRD_PARTY)
  proc = subprocess.Popen(MVN_JETTY_RUN) # async
  return proc
  
def build_jmc_core():
  os.chdir(JMC_CORE)
  subprocess.call(MVN_CLEAN_INSTALL)

def build_jmc():
  os.chdir(JMC_ROOT)
  subprocess.call(MVN_PACKAGE)

def main():
  clone_repo()
  p2site()
  proc = jetty_run()
  build_jmc_core()
  proc.kill()

if __name__ == '__main__':
  main()
