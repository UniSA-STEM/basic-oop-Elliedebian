"""
File: main.py
Description: <Runs the central game loop, coordinating hacker actions, rig interactions, and asset management to drive the overall hacking gameplay experience.>
Author: <Elham Debian>
ID: <debey003>
Username: <Elliedebian>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Rig import Rig
from Asset import Asset

def main():
    alice = Hacker("Wonderland")
    bob = Hacker("BobStar")

    alice.acquire_rig("Phantom-X")
    bob.acquire_rig("Sphere-9")

    alice.rig.generate_asset()
    alice.inventory.append(Asset("Hardware Patch", "Upgrade tool for rigs."))
    alice.upgrade_rig()
