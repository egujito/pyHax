# GUI

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# HACKS

import scripts.hacks.glow as gl
import offsets.offsets as vl
import scripts.hacks.bhop as bh
import scripts.hacks.fov as fov

# MEMORY OBJECT
import pymem
import pymem.process

# MISC

import sys
from threading import Thread
import time


class MainWin(QMainWindow):
    def __init__(self):

        self.glval = False
        self.bhval = False
        self.foval = 90

        super().__init__()

        self.initUI()

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

        self.updt = QPushButton(self)
        self.updt.setText("Force Update")
        self.updt.show()
        self.updt.clicked.connect(self.forceUpdate)

    def forceUpdate(self):
        is_updated = False
        while not is_updated:
            self.glval = self.glbtn.isChecked()
            self.bhval = self.bhbtn.isChecked()
            self.foval = self.fovsl.value()

            is_updated = True

        time.sleep(1)

    def mainCheat(self):
        while True:
            if self.glval:
                gl.enableGlow(vl.dwGlowObjectManager, vl.dwEntityList, vl.m_iTeamNum, vl.m_iGlowIndex,vl.dwLocalPlayer, vl.m_iHealth, pm, client)
            if self.bhval:
                bh.enableBhop(vl.dwForceJump, vl.dwLocalPlayer, vl.m_fFlags, pm, client)
            fov.changeFov(vl.dwEntityList, vl.m_iFOV, self.foval, pm, client)



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
