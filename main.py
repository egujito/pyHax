# GUI

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# HACKS

import scripts.hacks.glow as gl
import offsets.offsets as vl
import scripts.hacks.bhop as bh
import scripts.hacks.fov as fov
import scripts.hacks.radar as radar
import scripts.hacks.antiflash as fl
import scripts.hacks.skinchanger as sk

# MEMORY OBJECT

import pymem
import pymem.process

# CONFIG

import configparser

# MISC

import sys
from threading import Thread
import time
import os
import colorama
from colorama import Fore, Back, Style

class MainWin(QMainWindow):
    def __init__(self):

        self.glval = False
        self.bhval = False
        self.radarval = False
        self.antif = False
        self.skins = False

        self.foval = 90

        super().__init__()

        self.initUI()

    # GUI def
    def initUI(self):

        self.setGeometry(300,300,350,350)
        self.setWindowTitle("PyHax")
        self.show()

        self.glbtn = QCheckBox(self)
        self.glbtn.setText("Glow")
        self.glbtn.setChecked(False)
        self.glbtn.move(5, 50)
        self.glbtn.show()

        self.bhbtn = QCheckBox(self)
        self.bhbtn.setText("Bhop")
        self.bhbtn.setChecked(False)
        self.bhbtn.move(5, 80)
        self.bhbtn.show()

        self.fovsl = QSlider(Qt.Horizontal, self)
        self.fovsl.setRange(90, 200)
        self.fovsl.move(5, 120)
        self.fovsl.show()

        self.fovlabel = QLabel(self)
        self.fovlabel.setText("FOV CHANGER")
        self.fovlabel.move(20, 140)
        self.fovlabel.show()

        self.radarbtn = QCheckBox(self)
        self.radarbtn.setText("Radar Hack")
        self.radarbtn.setChecked(False)
        self.radarbtn.move(60, 50)
        self.radarbtn.show()

        self.antifbtn = QCheckBox(self)
        self.antifbtn.setText("Force Anti Flash")
        self.antifbtn.setChecked(False)
        self.antifbtn.move(150, 50)
        self.antifbtn.show()

        self.skinb = QCheckBox(self)
        self.skinb.setText("Enable SKin Changer")
        self.skinb.setChecked(False)
        self.skinb.move(150, 80)
        self.skinb.show()

        self.updt = QPushButton(self)
        self.updt.setText("Force Update")
        self.updt.show()
        self.updt.clicked.connect(self.forceUpdate)

        self.load = QPushButton(self)
        self.load.setText("Load CFG")
        self.load.move(100, 0)
        self.load.show()
        self.load.clicked.connect(self.load_cfg)

        self.save = QPushButton(self)
        self.save.setText("Save Config")
        self.save.move(200, 0)
        self.save.show()

    def load_cfg(self):
        self.raw_cfg = QFileDialog.getOpenFileName(self,'Single File','C:\'','*.ini')
        self.config = configparser.ConfigParser()
        self.config.read(self.raw_cfg)

        self.glbtn.setChecked(self.config['GLOW'].getboolean('activate'))
        self.bhbtn.setChecked(self.config['MOVEMENT'].getboolean('mode'))
        self.radarbtn.setChecked(self.config['MISC'].getboolean('radar'))
        self.antifbtn.setChecked(self.config['MISC'].getboolean('no_flash'))
        self.skinb.setChecked(self.config['SKINS'].getboolean('enable'))

        self.fovsl.setValue(self.config['MISC'].getint('fov'))


    # INCREMENT CHANGES. If you check for buttons state in a main func it will cause problems.

    def forceUpdate(self):
        is_updated = False
        while not is_updated:
            print("[ " + Fore.YELLOW + " INFO " '\033[39m' + " ]" + " updating all checkboxes, sliders, buttons values.")
            self.glval = self.glbtn.isChecked()
            self.bhval = self.bhbtn.isChecked()
            self.radarval = self.radarbtn.isChecked()
            self.antif = self.antifbtn.isChecked()
            self.skins = self.skinb.isChecked()
            print("[ " + Fore.YELLOW + " INFO " '\033[39m' + " ]" + " Looking for engine state to force update it")
            engine_state = pm.read_int( engine + vl.dwClientState )
            print("[ " + Fore.YELLOW + " WARNING " '\033[39m' + " ]" + " Updating the engine now")
            pm.write_int( engine_state + 0x174, -1 )
            print("[ " + Fore.GREEN + " OK " '\033[39m' + " ]" + " Fully updated engine now.")
            print("[ " + Fore.BLUE + " CHANGES " '\033[39m' + " ]")
            print(" Glow value -------> ", self.glval)
            print(" Bhop value -------> " , self.bhval)
            print(" Radar value -------> " , self.radarval)
            print(" Anti flash value -------> " , self.antif)
            print(" FOV value -------> ", self.foval)
            print(" Skin changer -------> ", self.skins)
            self.foval = self.fovsl.value()
            is_updated = True

        time.sleep(1)

    # MAIN CHEAT THREAD
    def mainCheat(self):
        while True:

            if self.glval:
                gl.enableGlow(vl.dwGlowObjectManager, vl.dwEntityList, vl.m_iTeamNum, vl.m_iGlowIndex,vl.dwLocalPlayer, vl.m_iHealth, pm, client)

            if self.bhval:
                bh.enableBhop(vl.dwForceJump, vl.dwLocalPlayer, vl.m_fFlags, pm, client)

            if self.radarval:
                radar.enableRadar(vl.dwEntityList, vl.m_bSpotted, pm, client)

            if self.antif:
                fl.enableAntiFlash(vl.dwLocalPlayer, vl.m_flFlashMaxAlpha, pm, client)

            if self.skins:
                sk.change_skin(vl.dwLocalPlayer, vl.dwClientState, vl.m_hMyWeapons, vl.dwEntityList, vl.m_iItemDefinitionIndex, vl.m_OriginalOwnerXuidLow, vl.m_iItemIDHigh, vl.m_nFallbackPaintKit, vl.m_iAccountID, vl.m_nFallbackStatTrak, vl.m_nFallbackSeed, vl.m_flFallbackWear, pm, client, engine)

            fov.changeFov(vl.dwLocalPlayer, vl.dwEntityList, vl.m_iFOV, self.foval, pm, client)


if __name__ == "__main__":

    # CREATE pymem object

    os.system('TITLE debugging pyhax')
    os.system("cls")


    try:
        print("[ " + Fore.YELLOW + "INFO" '\033[39m' + " ]" + " Finding Process 'csgo.exe'")
        pm = pymem.Pymem("csgo.exe")
        print("[ " + Fore.GREEN + "OK" '\033[39m' + " ]" + " Process found")
        print("[ " + Fore.YELLOW + "INFO" '\033[39m' + " ]" + " reading client.dll")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll" ).lpBaseOfDll
        print("[ " + Fore.GREEN + "OK" '\033[39m' + " ]" + " dll read successfuly")
        print("[ " + Fore.YELLOW + "INFO" '\033[39m' + " ]" + " reading engine.dll")
        engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
        print("[ " + Fore.GREEN + "OK" '\033[39m' + " ]" + " engine.dll read successfuly")
        print("[ " + Fore.CYAN + "INIT" '\033[39m' + " ]" + " Mounting GUI")
        time.sleep(1)

    except Exception as e:
        print("[ " + Fore.RED + "ERROR" '\033[39m' + " ] ", e)
        quit()

    ini = QApplication(sys.argv)
    win = MainWin()
    print("[ " + Fore.GREEN + "OK" '\033[39m' + " ]" + " GUI mounted")
    print("[ " + Fore.YELLOW + "WARNING" '\033[39m' + " ]" + " starting mainCheat() thread")
    time.sleep(1)
    Thread(target = win.mainCheat).start()
    print("[ " + Fore.GREEN + "OK" '\033[39m' + " ]" + " Thread started")
    sys.exit(ini.exec_())
