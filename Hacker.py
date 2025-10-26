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

    def acquire_rig(self, rig_name="Default Rig"):
        token = self.scan_inventory("CryptoToken")
        if token:
            self.__rig = Rig(rig_name)
            print(self.__name, "acquired and activated", self.__rig.name, end=".")
        else:
            print(self.__name, "cannot acquire a rig - CryptoToken required.")

    def launch_attack(self, target_hacker):
        if not self.__rig:
            print(self.__name, "has no rig to launch an attack.")
            return
        if self.__trace_level > 5:
            print(self.__name, "is exposed and cannot attack.")
            return

        spike = self.scan_storage("Data Spike")
        if spike:
            print(self.__name, "launches a data spike at", target_hacker.name, end="!")
            target_rig = target_hacker.rig
            if target_rig:
                target_rig.take_hit()
                self.__trace_level += 1
            else:
                print(target_hacker.name, "has no rig - attack wasted.")
        else:
            print("No Data Spikes available in", self.__rig.name, "storage.")

    def encrypt_asset(self, asset_name):
        chip = self.scan_inventory("Security Chip")
        asset = self.scan_inventory(asset_name)
        if chip and asset and asset.encrypted:
            asset.set_encrypted(False)
            print(self.__name, "decrypted", asset.name, end=".")
        else:
            print("Decryption failed - missing chip or asset not encrypted")

    def upgrade_rig(self):
        if not self.__rig:
            print(self.__name, "cannot upgrade - no rig equipped.")
            return
        patch = self.scan_inventory("Hardware Patch")
        if patch:
            self.__rig.upgrade(True)
        else:
            print(self.__name, "lacks a Hardware Patch.")

    def extract_assets(self, target_hacker):
        if not self.__rig or not target_hacker.rig:
            print("Execution failed, rigs missing.")
            return
        if not target_hacker.rig.broken:
            print(f"{target_hacker.name}'s rig is still secure.")
            return

        drive = self.scan_storage("Removable Drive")
        if not drive:
            print("No removable drive found in storage.")
            return

    def store_asset(self, asset_name):
        if not self.__rig:
            print(self.__name, "has no rig to store assets in.")
            return
        asset = self.scan_inventory(asset_name)
        if asset:
            self.__rig.storage.append(asset)
            print(asset.name, "stored in", self.__rig.name, end=".")
        else:
            print(asset_name, "no found in inventory.")

    def retrieve_asset(self, asset_name):
        if not self.__rig:
            print(self.__name, "has no rig.")
            return
        asset = self.scan_storage(asset_name)
        if asset:
            self.__inventory.scan_storage(asset.name)
            if asset:
                self.__inventory.append(asset)
                print(asset.name, "retrieved from", self.__rig.name, end=".")
        else:
            print(asset_name, "not found in inventory.")

def scan_inventory(self, name):
    for item in self.__inventory:
        if item.name == name:
            self.__inventory.remove(item)
            return item
        return None

def __str__(self):
    inv = ", ".join ([a.name for a in self.__inventory]) or "Empty"
    rig_status = self.__rig.name if self.__rig else "No Rig"
    return f"Hacker {self.__name} | Rig: {rig_status} | Trace: {self.__trace_level} | Inventory: {inv}"

