def enableRadar(dwEntityList, m_bSpotted, pm, client):
    for i in range(1, 32):
        entity = pm.read_int(client + dwEntityList + i * 0x10)
        if entity:
            pm.write_uchar(entity + m_bSpotted, 1)
