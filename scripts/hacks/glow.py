import misc.healthGetH as hp

def enableGlow(dwGlowObjectManager, dwEntityList, m_iTeamNum, m_iGlowIndex, dwLocalPlayer, m_iHealth, pm, client):
    glow_manager = pm.read_int(client + dwGlowObjectManager)
    player = pm.read_int( client + dwLocalPlayer )
    localTeam = pm.read_int( player + m_iTeamNum )

    for i in range(1,32):
        entity = pm.read_int(client + dwEntityList + i * 0x10)

        if entity:
            entity_team_id = pm.read_int(entity + m_iTeamNum)
            entity_glow = pm.read_int(entity + m_iGlowIndex)
            entity_hp = pm.read_int(entity + m_iHealth)

            if entity_team_id == localTeam:
                pass

            elif entity_team_id != localTeam:
                r, g, b = hp.getHealth(entity_hp)
                pm.write_float( glow_manager + entity_glow * 0x38 + 0x4, float( r ) )  # Red
                pm.write_float( glow_manager + entity_glow * 0x38 + 0x8, float( g ) )  # Green
                pm.write_float( glow_manager + entity_glow * 0x38 + 0xC, float( b ) )  # Blue
                pm.write_float( glow_manager + entity_glow * 0x38 + 0x10, float( 255 ) )  # Alpha

                pm.write_int( glow_manager + entity_glow * 0x38 + 0x24, 1 )  # Enable
