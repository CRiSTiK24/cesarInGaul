from ObjectClasses.faction import Faction


def init():
    roma = Faction("Roma", (255, 0, 0), [], [])
    massalia = Faction("Massalia", (0, 0, 255), [], [])
    nervii = Faction("Nervii", (255, 197, 156), [], [])
    arverni = Faction("Arverni", (0, 255, 0), [], [])
    suebi = Faction("Suebi", (145, 116, 0), [], [])
    neutral = Faction("Neutral", (255, 255, 255), [], [])

    factionDict = {
        "RO": roma,
        "MA": massalia,
        "NE": nervii,
        "AR": arverni,
        "SU": suebi,
        "N": neutral
    }

    # arrayFactions = [roma, massalia, belgae, arverni, suebi, neutral]

    return factionDict
