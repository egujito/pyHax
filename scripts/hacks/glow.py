def enableGlow(dwGlowObjectManager, dwEntityList, m_iTeamNum, m_iGlowIndex, pm, client):
    glow_manager = pm.read_int(client + dwGlowObjectManager)
    for i in range(1,32):
        entity = pm.read_int(client + dwEntityList + i * 0x10)

        if entity:
            entity_team_id = pm.read_int(entity + m_iTeamNum)
            entity_glow = pm.read_int(entity + m_iGlowIndex)

            if entity_team_id == 2:
                pm.write_float( glow_manager + entity_glow * 0x38 + 0x4, float(1) )  # Red
                pm.write_float( glow_manager + entity_glow * 0x38 + 0x8, float(0) )  # Green
                pm.write_float( glow_manager + entity_glow * 0x38 + 0xC, float(0) )  # Blue
                pm.write_float( glow_manager + entity_glow * 0x38 + 0x10, float(222) )  # Alpha
                pm.write_int( glow_manager + entity_glow * 0x38 + 0x24, 1 )

            elif entity_team_id == 3:
                pm.write_float( glow_manager + entity_glow * 0x38 + 0x4, float(0) )  # Red
                pm.write_float( glow_manager + entity_glow * 0x38 + 0x8, float(0) )  # Green
                pm.write_float( glow_manager + entity_glow * 0x38 + 0xC, float(1) )  # Blue
                pm.write_float( glow_manager + entity_glow * 0x38 + 0x10, float(222) )  # Alpha
                pm.write_int( glow_manager + entity_glow * 0x38 + 0x24, 1 )