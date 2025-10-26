"""
File: Hacker.py
Description: <Controls the main game mechanics, letting players manage rigs, collect and use assets, and perform actions like upgrading, repairing, and attacking within the hacking simulation>
Author: <Elham Debian>
ID: <debey003>
Username: <Elliedebian>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig

class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory = [Asset("CryptoToken", "Base currency of the grid.")]
        self.__rig = None
        self.__trace_level = 0

    def get_name(self):
        return self.__name

    def get_trace_level(self):
        return self.__trace_level

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    name = property(get_name)
    trace_level = property(get_trace_level)
    inventory = property(get_inventory)
    rig = property(get_rig)



