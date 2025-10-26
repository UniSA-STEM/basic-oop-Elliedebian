"""
File: Rig.py
Description: <Represents a hacker's computer system that stores digital assets, takes damage in battles, can be upgraded or repaired, and serves as the ,main tool for attacks and asset management.>
Author: <Elham Debian>
ID: <debey003>
Username: <Elliedebian>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from asset import Asset

class Rig:
  def __init__(self, name):
    self.__name = name
    self.__damage = 0
    self.__broken = False
    self.__upgrade_level = 0
    self.__storage = []

  def get_name(self):
    return self.__name

  def get_damage(self):
    return self.__damage

  def is_broken(self):
      return self.__broken

  def get_upgrade_level(self):
    return self.__upgrade_level

  def get_storage(self):
    return self.__storage

  name = property(get_name)
  damage = property(get_damage)
  broken = property(is_broken)
  upgrade_level = property(get_upgrade_level)
  storage = property(get_storage)



  
