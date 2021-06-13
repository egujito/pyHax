import configparser
import keyboard

def change_skin(dwLocalPlayer, dwClientState, m_hMyWeapons,dwEntityList, m_iItemDefinitionIndex,m_OriginalOwnerXuidLow, m_iItemIDHigh,m_nFallbackPaintKit, m_iAccountID,m_nFallbackStatTrak, m_nFallbackSeed,m_flFallbackWear, pm, client, engine):

    skins = configparser.ConfigParser()
    skins.read("config/skins.ini")

    akpaint = skins['SKINS'].getint("AK-47")
    awppaint = skins['SKINS'].getint("AWP")
    usppaint = skins['SKINS'].getint("USP-S")
    deaglepaint = skins['SKINS'].getint("Desert Eagle")
    glockpaint = skins['SKINS'].getint("Glock")
    fivepaint = skins['SKINS'].getint("Five-Seven")
    ppaint = skins['SKINS'].getint("P250")
    tecpaint = skins['SKINS'].getint("Tec-9")
    mapaint = skins['SKINS'].getint("M4A4")
    mspaint = skins['SKINS'].getint("M4A1-S")
    galilpaint = skins['SKINS'].getint("Galil")
    famaspaint = skins['SKINS'].getint("Famas")
    augpaint = skins['SKINS'].getint("AUG")
    sgpaint = skins['SKINS'].getint("SG-553")
    scoutpaint = skins['SKINS'].getint("Scout")
    macpaint = skins['SKINS'].getint("Mac-10")
    mpsevpaint = skins['SKINS'].getint("MP7")
    mpninpaint = skins['SKINS'].getint("MP9")
    pppaint = skins['SKINS'].getint("big_pp_weapon")
    pneunpaint = skins['SKINS'].getint("P90")
    umppaint = skins['SKINS'].getint("UMP")
    magpaint = skins['SKINS'].getint("MAG-7")
    novpaint = skins['SKINS'].getint("Nova")
    sawpaint = skins['SKINS'].getint("Sawed Off")
    xmpaint = skins['SKINS'].getint("XM1014")
    revolverpaint = skins['SKINS'].getint("Revolver")
    czpaint = skins['SKINS'].getint("CZ75-Auto")
    dualiespaint = skins['SKINS'].getint("Dualies")
    p2000paint = skins['SKINS'].getint("P2000")
    mp5paint = skins['SKINS'].getint("MP5-SD")
    negevpaint = skins['SKINS'].getint("Negev")
    m249paint = skins['SKINS'].getint("M249")
    g3sg1paint = skins['SKINS'].getint("G3SG1")
    scarpaint = skins['SKINS'].getint("Scar-20")
    engine_state = pm.read_int( engine + dwClientState )
    local_player = pm.read_int( client + dwLocalPlayer )

    for i in range( 0, 8 ):
        my_weapons = pm.read_int( local_player + m_hMyWeapons + (i - 1) * 0x4 ) & 0xFFF
        weapon_address = pm.read_int( client + dwEntityList + (my_weapons - 1) * 0x10 )
        if weapon_address:
            weapon_id = pm.read_short( weapon_address + m_iItemDefinitionIndex )


            weapon_owner = pm.read_int( weapon_address + m_OriginalOwnerXuidLow )
            seed = 420
            if weapon_id == 7:
                fallbackpaint = akpaint
                seed = 661
            elif weapon_id == 9:
                fallbackpaint = awppaint
                seed = 420
            elif weapon_id == 61:
                fallbackpaint = usppaint
                seed = 420
            elif weapon_id == 1:
                fallbackpaint = deaglepaint
                seed = 420
            elif weapon_id == 4:
                fallbackpaint = glockpaint
                seed = 420
            elif weapon_id == 3:
                fallbackpaint = fivepaint
                seed = 420
            elif weapon_id == 36:
                fallbackpaint = ppaint
                seed = 420
            elif weapon_id == 30:
                fallbackpaint = tecpaint
                seed = 420
            elif weapon_id == 16:
                fallbackpaint = mapaint
            elif weapon_id == 60:
                fallbackpaint = mspaint
            elif weapon_id == 13:
                fallbackpaint = galilpaint
            elif weapon_id == 10:
                fallbackpaint = famaspaint
            elif weapon_id == 8:
                fallbackpaint = augpaint
            elif weapon_id == 39:
                fallbackpaint = sgpaint
            elif weapon_id == 40:
                fallbackpaint = scoutpaint
            elif weapon_id == 17:
                fallbackpaint = macpaint
            elif weapon_id == 33:
                fallbackpaint = mpsevpaint
            elif weapon_id == 34:
                fallbackpaint = mpninpaint
            elif weapon_id == 26:
                fallbackpaint = pppaint
            elif weapon_id == 19:
                fallbackpaint = pneunpaint
            elif weapon_id == 24:
                fallbackpaint = umppaint
            elif weapon_id == 27:
                fallbackpaint = magpaint
            elif weapon_id == 35:
                fallbackpaint = novpaint
            elif weapon_id == 29:
                fallbackpaint = sawpaint
            elif weapon_id == 25:
                fallbackpaint = xmpaint
            elif weapon_id == 64:
                fallbackpaint = revolverpaint
            elif weapon_id == 63:
                fallbackpaint = czpaint
            elif weapon_id == 2:
                fallbackpaint = dualiespaint
            elif weapon_id == 32:
                fallbackpaint = p2000paint
            elif weapon_id == 23:
                fallbackpaint = mp5paint
            elif weapon_id == 28:
                fallbackpaint = negevpaint
            elif weapon_id == 14:
                fallbackpaint = m249paint
            elif weapon_id == 11:
                fallbackpaint = g3sg1paint
            elif weapon_id == 38:
                fallbackpaint = scarpaint
            else: # MEANS PLAYER IS DEAD
                continue

            pm.write_int( weapon_address + m_iItemIDHigh, -1 )
            pm.write_int( weapon_address + m_nFallbackPaintKit, fallbackpaint )
            pm.write_int( weapon_address + m_iAccountID, weapon_owner )
            pm.write_int( weapon_address + m_nFallbackStatTrak, 42069 )
            pm.write_int( weapon_address + m_nFallbackSeed, seed )
            pm.write_float( weapon_address + m_flFallbackWear, float( 0.000001 ) )

        if keyboard.is_pressed( "f6" ):
            pm.write_int( engine_state + 0x174, -1 )
