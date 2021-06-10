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

        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,350,350)
        self.setWindowTitle("PyHax")
        self.show()

        self.glbtn = QCheckBox(self)
        self.glbtn.setText("Glow")
        self.glbtn.setChecked(False)
        self.glbtn.move(10, 50)
        self.glbtn.show()

        self.updt = QPushButton(self)
        self.updt.setText("Force Update")
        self.updt.show()
        self.updt.clicked.connect(self.forceUpdate)

    def forceUpdate(self):
        is_updated = False
        while not is_updated:
            self.glval = self.glbtn.isChecked()
            is_updated = True
        else:
            time.sleep(1)

    def mainCheat(self):
        while True:
            if self.glval:
                gl.enableGlow(vl.dwGlowObjectManager, vl.dwEntityList, vl.m_iTeamNum, vl.m_iGlowIndex,vl.dwLocalPlayer, vl.m_iHealth, pm, client)
            bh.enableBhop(vl.dwForceJump, vl.dwLocalPlayer, vl.m_fFlags, pm, client)

if __name__ == "__main__":
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
