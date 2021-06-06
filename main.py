from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import scripts.hacks.glow as gl
import offsets.offsets as vl
import scripts.hacks.bhop as bh
import pymem
import pymem.process
import sys
from threading import Thread

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        self.setGeometry(300,300,350,350)
        self.setWindowTitle("PyHax")
        self.show()

        self.glbtn = QCheckBox(self)
        self.glbtn.setText("Glow")
        self.glbtn.setChecked(False)
        self.glbtn.move(175, 50)
        self.glbtn.show()

    def mainCheat(self):
        while True:
            
            gl.enableGlow(vl.dwGlowObjectManager, vl.dwEntityList, vl.m_iTeamNum, vl.m_iGlowIndex,vl.dwLocalPlayer, vl.m_iHealth, pm, client)
            bh.enableBhop(vl.dwForceJump, vl.dwLocalPlayer, vl.m_fFlags, pm, client)

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


# DEPRICATED
""" Thread(target = glow.enableGlow, args =(vl.dwGlowObjectManager, vl.dwEntityList, vl.m_iTeamNum, vl.m_iGlowIndex),).start()
Thread(target = bhop.enableBhop, args =(vl.dwForceJump, vl.dwLocalPlayer, vl.m_fFlags),).start() """