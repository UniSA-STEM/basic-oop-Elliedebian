"""
File: Asset.py
Description: <.>
Author: <Elham Debian>
ID: <debey003>
Username: <Elliedebian>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
  def __init__(self, name, description, encrypted):
      self.__name = name
      self.__description = description
      self.__encrypted = encrypted

  def get_name(self):
    return self.__name

  def get_description(self):
    return self.__description

  def is_encrypted(self):
    return self.__encrypted

  
