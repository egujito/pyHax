def changeFov(dwEntityList, m_iFOV, FOV_VAL, pm, client):
    player = pm.read_int(client + dwEntityList)
    pm.write_int(player + m_iFOV, FOV_VAL)
