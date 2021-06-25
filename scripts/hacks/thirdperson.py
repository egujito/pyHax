import keyboard
from colorama import Fore
import time

def checkThirdPerson(m_iObserverMode, dwLocalPlayer, m_iFOV, pm, client, bind, is_observer):

    localplayer = pm.read_int(client + dwLocalPlayer)
    fov = localplayer + m_iFOV

    try:
        if keyboard.is_pressed(bind) and not is_observer:

            pm.write_int(localplayer + m_iObserverMode, 1)
            is_observer = True
            time.sleep(0.5)

        elif keyboard.is_pressed(bind) and is_observer:

            pm.write_int(localplayer + m_iObserverMode, 0)
            is_observer = False
            time.sleep(0.5)

    except Exception as e:
        print(e)
        quit()
        #print("[ " + Fore.RED + "WARNING" '\033[39m' + " ]" + " keybind is not valid. Change its value.")
