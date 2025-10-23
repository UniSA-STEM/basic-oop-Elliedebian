"""
File: Asset.py
Description: <The Asset class represents a digital item within the grid that can be stored, transferred, encrypted, or used by hackers and rigs during gameplay.>
Author: <Elham Debian>
ID: <debey003>
Username: <Elliedebian>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
  def __init__(self, name, description, encrypted):
      self.__name = name
      self.__description = description
      self.__encrypted = False

  def get_name(self):
    return self.__name

  def get_description(self):
    return self.__description

  def is_encrypted(self):
    return self.__encrypted

  def set_encrypted(self, value):
    self.__encrypted = value

  name = property(get_name)
  description = property(get_description)
  encrypted = property(is_encrypted, set_encrypted)

  def __str__(self):
    if self.__encrypted:
      return f"{self.__name}: {self.__description} [Encrypted]"
    return f"{self.__name}: {self.__description}"

  def __eq__(self, other):
    return False
