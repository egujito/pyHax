def enableAntiFlash(dwLocalPlayer, m_flFlashMaxAlpha, pm, client):

    player = pm.read_int(client + dwLocalPlayer)
    flash_value = player + m_flFlashMaxAlpha

    while True:

        player = pm.read_int(client + dwLocalPlayer)

        if player:
            is_flashed = player + m_flFlashMaxAlpha
            pm.write_float(is_flashed, float(0))
