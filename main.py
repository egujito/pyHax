from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import scripts.hacks.glow as gl
import offsets.offsets as vl
import scripts.hacks.bhop as bh
import pymem
import pymem.process
import sys
from threading import Thread
import time

class MainWin(QMainWindow):
    def __init__(self):

        self.glval = False
        self.bhval = False

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

        self.glbtn = QCheckBox(self)
        self.glbtn.setText("Bhop")
        self.glbtn.setChecked(False)
        self.glbtn.move(5, 80)
        self.glbtn.show()

        self.updt = QPushButton(self)
        self.updt.setText("Force Update")
        self.updt.show()
        self.updt.clicked.connect(self.forceUpdate)

    def forceUpdate(self):
        updated = True
        while updated:
            self.glval = self.glbtn.isChecked()
            self.bhval = self.glbtn.isChecked()

            updated = False

        time.sleep(1)

    def mainCheat(self):
        while True:
            if self.glval:
                gl.enableGlow(vl.dwGlowObjectManager, vl.dwEntityList, vl.m_iTeamNum, vl.m_iGlowIndex,vl.dwLocalPlayer, vl.m_iHealth, pm, client)
            else:
                pass
            if self.bhval:
                bh.enableBhop(vl.dwForceJump, vl.dwLocalPlayer, vl.m_fFlags, pm, client)
            else:
                pass


try:
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll" ).lpBaseOfDll
except:
    print("init csgo first")
    quit()

ini = QApplication(sys.argv)
win = MainWin()
Thread(target = win.mainCheat).start()
sys.exit(ini.exec_())
