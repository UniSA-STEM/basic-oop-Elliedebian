"""
File: Rig.py
Description: <Represents a hacker's computer system that stores digital assets, takes damage in battles, can be upgraded or repaired, and serves as the ,main tool for attacks and asset management.>
Author: <Elham Debian>
ID: <debey003>
Username: <Elliedebian>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset

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

  def repair(self, token_found:bool):
      if token_found:
          if self.__damage > 0:
              self.__damage = 0
              self.__broken = False
              print(self.__name, "has been repaired and is now functional.")
          else:
              print(self.__name, "is pristine - no repair needed.")

      else:
          print("Repair failed - missing CryptoToken.")

  def upgrade(self, patch_found:bool):
      if patch_found:
          self.__upgrade_level += 1
          print(self.__name, "upgraded to Level", self.__upgrade_level, end=".")
      else:
          print("Upgrade failed - missing Hardware Patch.")

  def take_hit(self):
      if not self.__broken:
          print(self.__name, "took a hit! Damage level:", self.__damage, end=".")
          limit = 2 - self.__upgrade_level
          if self.__damage > max(1, limit):
              self.__broken = True
              print(self.__name, "has broken down!")

      else:
          print(self.__name, "is already broken.")

  def condition(self):
      state = "Broken" if self.__broken else "Pristine"
      return f"{state} (level {self.__upgrade_level})"

  def generate_asset(self):
      new_asset = Asset("Security Chip", "Used for encryption or decryption.")
      self.__storage.append(new_asset)
      print(self.__name, "generated a new asset:", new_asset)
      return new_asset

  def __str__(self):
      assets = ", ".join[a.name for a in self.__storage]) or "Empty"
      return f"{self.__name} - {self.condition()} - Stored: {assets}"



  
