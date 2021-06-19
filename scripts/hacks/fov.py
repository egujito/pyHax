def changeFov(dwLocalPlayer, dwEntityList, m_iFOV, FOV_VAL, pm, client):
    player = pm.read_int(client + dwLocalPlayer)
    fov = player + m_iFOV
    pm.write_int(fov, FOV_VAL)

    #player = pm.read_int(client + dwEntityList)
    #pm.write_int(player + m_iFOV, FOV_VAL)
