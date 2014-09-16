#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run
from fabric.api import cd
from fabric.api import sudo
from fabric.api import env
from fabric.colors import red, green

import cuisine

cuisine.select_package("apt")


def setup():
    _setup_ubuntu()
    _install_dotfiles()
    _install_scala_and_sbt()


def _setup_ubuntu():
    sudo("cp /usr/share/zoneinfo/Japan /etc/localtime")
    sudo("apt-get update")
    cuisine.package_ensure('git')
    cuisine.package_ensure('exuberant-ctags')


def _install_dotfiles():
    env.forward_agent = True
    run("git clone git@github.com:m3y/dotfiles.git")
    with cd("/home/vagrant/dotfiles"):
        run("make install")
    print(green("[dotfiles] installed."))


def _install_scala_and_sbt():
    cuisine.package_ensure('openjdk-7-jdk')
    run("wget http://www.scala-lang.org/files/archive/scala-2.11.2.deb")
    run("wget http://dl.bintray.com/sbt/debian/sbt-0.13.6.deb")
    sudo("dpkg -i scala-2.11.2.deb")
    sudo("dpkg -i sbt-0.13.5.deb")
    sudo("apt-get update")
    sudo("apt-get install scala")
    sudo("apt-get install sbt")
