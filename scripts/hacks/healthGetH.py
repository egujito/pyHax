def getHealth(entity_hp):
    if entity_hp > 50 and not entity_hp == 100:
        return 255, 165, 0
    elif entity_hp < 50:
        return 255, 0, 0
    else:
        return 0, 255, 0
