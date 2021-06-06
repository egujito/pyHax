import keyboard
import time

def enableBhop(dwForceJump, dwLocalPlayer, m_fFlags, pm, client):

    if keyboard.is_pressed("space"):
        force_jump = client + dwForceJump
        player = pm.read_int(client + dwLocalPlayer)
        grounded = pm.read_int(player + m_fFlags)
        if player and grounded and grounded == 257:
            pm.write_int(force_jump, 5)
            time.sleep(0.08)
            pm.write_int(force_jump, 4)

                


