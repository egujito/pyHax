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

class MainWin(QMainWindow):
    def __init__(self):

        self.glval = False
        self.bhval = False
        self.radarval = False
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
        self.radarbtn.setChecked(self.config['RADAR'].getboolean('activate'))
        self.fovsl.setValue(self.config['FOV'].getint('value'))

    # INCREMENTE CHANGES. If you check for buttons state in a main func it will cause problems.

    def forceUpdate(self):
        is_updated = False
        while not is_updated:
            self.glval = self.glbtn.isChecked()
            self.bhval = self.bhbtn.isChecked()
            self.radarval = self.radarbtn.isChecked()
            self.foval = self.fovsl.value()

            is_updated = True

        time.sleep(1)

    # MAIN CHEAT THREAD
    def mainCheat(self):
        while True:
            try:

                if self.glval:
                    gl.enableGlow(vl.dwGlowObjectManager, vl.dwEntityList, vl.m_iTeamNum, vl.m_iGlowIndex,vl.dwLocalPlayer, vl.m_iHealth, pm, client)

                if self.bhval:
                    bh.enableBhop(vl.dwForceJump, vl.dwLocalPlayer, vl.m_fFlags, pm, client)

                if self.radarval:
                    radar.enableRadar(vl.dwEntityList, vl.m_bSpotted, pm, client)

                if self.foval != 90:
                    fov.changeFov(vl.dwEntityList, vl.m_iFOV, self.foval, pm, client)

            except:
                print("Waiting for game to start.")
                time.sleep(1)
                os.system("cls")
                print("Waiting for game to start..")
                time.sleep(1)
                os.system("cls")
                print("Waiting for game to start...")
                time.sleep(1)
                os.system("cls")


if __name__ == "__main__":

    # CREATE pymem object

    try:
        pm = pymem.Pymem("csgo.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll" ).lpBaseOfDll
    except Exception as e:
        print(e)
        quit()

    ini = QApplication(sys.argv)
    win = MainWin()
    Thread(target = win.mainCheat).start()
    sys.exit(ini.exec_())
