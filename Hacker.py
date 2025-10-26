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

