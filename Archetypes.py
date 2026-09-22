import Specialisms_and_Abilities
from Specialisms_and_Abilities import heavy_jumppack_and_gravis_armour

class Archetype:
    def __init__(self, name, m,t,sv,ivl,w,ld, oc,archpoints,core,faction_rules,keywords,ability,composition,leader,model_count=1,primary_limit =1,pistol_limit=2,melee_limit=2):
        self.name = name
        self.m = m
        self.t = t
        self.sv = sv
        self.ivl = ivl if ivl is not None else 0
        self.w = w
        self.ld = ld
        self.oc = oc
        self.archpoints = archpoints
        self.core = core
        self.faction_rules = faction_rules
        self.keywords = keywords
        self.ability = ability
        self.composition = composition
        self.leader = leader if leader is not None else 0
        self.model_count = model_count
        self.primary_limit = primary_limit
        self.pistol_limit = pistol_limit
        self.melee_limit = melee_limit

class chaos_patron:
    def __init__(self, patron, patron_points, keywords,faction_keyword, pact_name, m, t, w, sv, ivl, archetype_overrides=None):
        self.patron = patron
        self.patron_points = patron_points
        self.keywords = keywords
        self.faction_keyword= faction_keyword
        self.pact_name = pact_name
        self.m = m
        self.t = t
        self.w = w
        self.sv = sv
        self.ivl = ivl
        self.archetype_overrides = archetype_overrides if archetype_overrides is not None else {}


patron_khorne = chaos_patron(
    patron="Khorne",
    patron_points=15,
    keywords=["KHORNE"],
    faction_keyword= "BLOOD LEGIONS",
    pact_name="PACT OF BLOOD",
    m=2, t=1, w=1, sv=None, ivl=None,
    archetype_overrides={
        "Daemonic Charioteer": {"sv": {"mode": "override", "value": 3}}
    }
)

patron_tzeentch = chaos_patron(
    patron="Tzeentch",
    patron_points=0,
    keywords=["TZEENTCH", "PSYKER"],
    faction_keyword= "SCINTILLATING LEGIONS",
    pact_name="PACT OF SORCERY",
    m=None, t=None, w=None, sv=None, ivl=4,
    archetype_overrides={
        "Daemonic Charioteer": {
            "m": {"mode": "modifier", "value": 6},
            "extra_keywords": ["FLY"]
        }
    }
)

patron_nurgle = chaos_patron(
    patron="Nurgle",
    patron_points=10,
    keywords=["NURGLE"],
    faction_keyword= "PLAGUE LEGIONS",
    pact_name="PACT OF DECAY",
    m=None, t=2, w=2, sv=None, ivl=None,
    archetype_overrides={}
)

patron_slaanesh = chaos_patron(
    patron="Slaanesh",
    patron_points=0,
    keywords=["SLAANESH", "LEGIONS OF EXCESS", "PSYKER"],
    faction_keyword= "LEGIONS OF EXCESS",
    pact_name="PACT OF EXCESS",
    m=3, t=None, w=None, sv=None, ivl=None,
    archetype_overrides={}
)
champion_of_the_chapter = Archetype(
    name="Champion of the Chapter",
    m=6, t=4, sv=3, ivl=None, w=4, ld=6, oc=1,
    archpoints=70,
    core=["Crucible", "Leader"],
    faction_rules=["Oath of Moment"],
    keywords=["Infantry", "Character", "Grenades", "Imperium", "Tacticus", "Champion of the Chapter"],

    ability={
        "Exemplar Warrior": "Once per turn, when this model's unit is selected to shoot or fight, "
                             "it can use this ability. If it does, until the end of the phase, each "
                             "time this model makes an attack, you can re-roll the Wound roll."
    },
    composition=["1 Champion of the Chapter"],
    leader="This model can be attached to the following units: Tacticus (excluding Character and Fly), Tactical Squad"
)

librarius_adept = Archetype(
    name="Librarius Adept",
    m=6, t=4, sv=3, ivl=None, w=3, ld=6, oc=1,
    archpoints= 70,
    core=["Crucible", "Leader"],
    faction_rules=["Oath of Moment"],
    keywords=["Infantry", "Character", "Grenades", "Psyker", "Imperium", "Tacticus", "Librarius Adept"],
    ability={
        "Veil of Time (Psychic)": "Weapons equipped by models in this unit have the [SUSTAINED HITS 1] ability."
    },
    composition=["1 Librarius Adept"],
    leader="This model can be attached to the following units: Tacticus (excluding Character and Fly), Tactical Squad"
)

venerable_battle_brother = Archetype(
    name="Venerable Battle-Brother",
    m=8, t=10, sv=2, ivl=None, w=12, ld=6, oc=4,
    archpoints= 160,
    core=["Crucible", "Deadly Demise D3"],
    faction_rules=["Oath of Moment"],
    keywords=["Vehicle", "Walker", "Character", "Imperium", "Dreadnought", "Venerable Battle-Brother"],

    ability={
        "Wisdom of the Ancients (Aura)": "While a friendly Adeptus Astartes Infantry unit is within 6\" "
                                          "of this model, each model in that unit makes an attack, re-roll "
                                          "a Hit roll of 1."
    },
    composition=["1 Venerable Battle-Brother"],
    leader=None
)

astartes_archetypes = [champion_of_the_chapter,
                           librarius_adept,
                           venerable_battle_brother]

champion_of_titan = Archetype(
    name="Champion of Titan",
    m=6, t=4, sv=2, ivl=4, w=4, ld=6, oc=1,
    archpoints= 90,
    core=["Crucible", "Deep Strike", "Leader"],
    faction_rules=["Gate of Infinity"],
    keywords=["Infantry", "Character", "Psyker", "Grenades", "Imperium", "Champion of Titan"],

    ability={
        "Might of Titan": "Once per battle, at the start of a phase, this model can use this ability. "
                           "If it does, until the end of the phase, add 3 to the Attacks and Strength "
                           "characteristics of melee weapons equipped by this model."
    },
    composition=["1 Champion of Titan"],
    leader="This model can be attached to the following units: Purgation Squad, Strike Squad"
)

venerable_daemon_slayer = Archetype(
    name="Venerable Daemon Slayer",
    m=8, t=9, sv=2, ivl=None, w=8, ld=6, oc=3,
    archpoints= 175,
    core=["Crucible", "Deadly Demise 1", "Deep Strike"],
    faction_rules=["Gate of Infinity"],
    keywords=["Vehicle", "Walker", "Character", "Psyker", "Smoke", "Imperium", "Venerable Daemon Slayer"],

    ability={
        "Guidance of the Ancients": "In your Shooting phase, after this unit has shot, select one unit "
                                     "hit by one or more of those attacks. Until the end of the phase, "
                                     "each time a Grey Knights model from your army makes an attack that "
                                     "targets that unit, add 1 to the Hit roll."
    },
    composition=[
        "1 Venerable Daemon Slayer",
        "This Crucible Champion can be equipped with up to two ranged weapons instead of up to one."
    ],
    leader=None
)

dreadknight_champion = Archetype(
    name="Dreadknight Champion",
    m=8, t=8, sv=2, ivl=4, w=13, ld=6, oc=4,
    archpoints= 210,
    core=["Crucible", "Deadly Demise D3", "Deep Strike"],
    faction_rules=["Gate of Infinity"],
    keywords=["Vehicle", "Walker", "Character", "Psyker", "Imperium", "Dreadknight Champion"],

    ability={
        "Surge of Wrath": "Each time this model makes a melee attack that targets a Monster or Vehicle "
                           "unit, you can re-roll the Hit roll, you can re-roll the Wound roll and you "
                           "can re-roll the Damage roll.",
        "Damaged: 1-4 Wounds Remaining": "While Damaged, subtract 1 from Hit rolls when it makes attacks."
    },
    composition=[
        "1 Dreadknight Champion",
        "This Crucible Champion can be equipped with up to three ranged weapons instead of up to one."
    ],
    leader=None
)

grey_knights_archtype = [champion_of_titan,
                         venerable_daemon_slayer,
                         dreadknight_champion]

plague_sorcerer = Archetype(
    name="Plague Sorcerer",
    m=5, t=6, sv=3, ivl=None, w=4, ld=6, oc=1,
    archpoints= 70,
    core=["Crucible", "Leader"],
    faction_rules=["Nurgle's Gift (Aura)"],
    keywords=["Infantry", "Character", "Psyker", "Chaos", "Nurgle", "Plague Sorcerer"],

    ability={
        "Gift of Contagion (Psychic)": "Each time a model in this unit makes an attack that targets a "
                                        "unit that is Afflicted, that attack has the [SUSTAINED HITS 1] "
                                        "ability."
    },
    composition=["1 Plague Sorcerer"],
    leader="This model can be attached to the following unit: Plague Marines, Poxwalkers"
)

plague_lord = Archetype(
    name="Plague Lord",
    m=5, t=6, sv=3, ivl=4, w=5, ld=6, oc=1,
    archpoints=80,
    core=["Crucible", "Leader"],
    faction_rules=["Nurgle's Gift (Aura)"],
    keywords=["Infantry", "Character", "Grenades", "Chaos", "Nurgle", "Plague Lord"],
    ability={
        "Gift of Poxes": "Add 3\" to the range of this model's Contagion Range."
    },
    composition=["1 Plague Lord"],
    leader="This model can be attached to the following unit: Plague Marines, Poxwalkers"
)

tri_lobe_vectors = Archetype(
    name="Tri-Lobe Vectors",
    m=5, t=6, sv=3, ivl=None, w=4, ld=6, oc=1,
    archpoints=120,
    core=["Crucible","Leader"],
    faction_rules=["Nurgle's Gift (Aura)"],
    keywords= ["Infantry", "Character", "Grenades", "Chaos", "Nurgle", "Tri-lobe Vectors"],
    ability={
        "Specialism Selection": "In Step 2, choose up to one specialism for this unit. In Step 3, choose "
                                 "one unique ability for each model in this unit. In Step 4, complete this "
                                 "step for each model in this unit separately."
    },
    composition=["3 Tri-lobe Vectors"],
    leader="This unit can be attached to the following unit: Plague Marines, Poxwalkers",
    model_count = 3,


)

death_guard_archetypes = [plague_sorcerer,
                          plague_lord,
                          tri_lobe_vectors]

shas_nel = Archetype(
    name="Shas'nel",
    m=6, t=3, sv=4, ivl=None, w=3, ld=7, oc=1,
    archpoints= 50,
    core=["Crucible", "Leader"],
    faction_rules=["For the Greater Good"],
    keywords=["Infantry", "Character", "Grenades", "Shas'nel"],
    ability={
        "Volley Fire": "While this model is leading a unit, add 1 to the Attacks characteristic of "
                        "ranged weapons equipped by models in that unit."
    },
    composition=["1 Shas'nel"],
    leader="This model can be attached to the following units: Breacher Team, Strike Team"
)

battlesuit_veteran = Archetype(
    name="Battlesuit Veteran",
    m=8, t=4, sv=3, ivl=4, w=4, ld=7, oc=1,
    archpoints= 60,
    core=["Crucible", "Infiltrators", "Leader", "Stealth"],
    faction_rules=["For the Greater Good"],
    keywords=["Infantry", "Character", "Fly", "Battlesuit", "Battlesuit Veteran"],

    ability={
        "Strategic Redeployment": "The bearer's unit is eligible to shoot in a turn in which it Fell Back."
    },
    composition=["1 Battlesuit Veteran"],
    leader="This model can be attached to the following unit: Stealth Battlesuits"
)

kinband_champion = Archetype(
    name="Kinband Champion",
    m=7, t=3, sv=6, ivl=None, w=3, ld=7, oc=1,
    archpoints= 55,
    core=["Crucible", "Infiltrators", "Leader", "Scouts 7\"", "Stealth"],
    faction_rules=["For the Greater Good"],
    keywords= ["Infantry", "Character", "Kroot", "Kinband Champion"],

    ability={
        "War Leader": "Once per battle round, one unit from your army with this ability can be targeted "
                       "with a Stratagem for 0CP, even if another unit from your army has already been "
                       "targeted with that Stratagem this phase."
    },
    composition=["1 Kinband Champion"],
    leader="This model can be attached to the following units: Kroot Carnivores, Kroot Farstalkers"
)

tau_archetypes = [shas_nel,
                  battlesuit_veteran,
                  kinband_champion]
#Astra Militarum
# FRONT-LINE COMMANDER
front_line_commander = Archetype(
    name="Front-Line Commander",
    m=6,
    t=3,
    sv=5,
    ivl=5,
    w=4,
    ld=7,
    oc=1,
    archpoints=55,
    core=["Crucible", "Leader"],
    faction_rules=["Voice of Command"],
    keywords=["INFANTRY", "CHARACTER", "GRENADES", "IMPERIUM", "OFFICER", "FRONT-LINE COMMANDER"],
    ability="Get Back in the Fight: While this model is leading a unit, that unit is eligible to shoot in a turn in which it fell back. This OFFICER can issue up to 2 Orders to REGIMENT units.",
    composition="1 Front-line Commander",
    leader="ASTRA MILITARUM BATTLELINE, KASKRIN, KRIEG COMBAT ENGINEERS, TEMPESTUS SCIONS"
)

# AUGMENTED BONE 'EAD
augmented_bone_ead = Archetype(
    name="Augmented Bone'ead",
    m=6,
    t=3,
    sv=4,
    ivl=5,
    w=3,
    ld=6,
    oc=1,
    archpoints=60,
    core=["Crucible", "Feel No Pain 6+", "Leader"],
    faction_rules=["Voice of Command"],
    keywords=["INFANTRY", "GRENADES", "CHARACTER", "IMPERIUM", "REGIMENT", "OGRYN", "AUGMENTED BONE'EAD"],
    ability="You 'Eard 'Em: Each time an Order is issued to this model's unit, this model can issue that Order to one other friendly PLATOON or OGRYN unit in the same way as an OFFICER.",
    composition="1 Augmented Bone 'Ead",
    leader="BULLGRYN SQUAD, OGRYN SQUAD"
)

# SENTINEL COMMANDER
sentinel_commander = Archetype(
    name="Sentinel Commander",
    m=10,
    t=7,
    sv=3,
    ivl=0,
    w=7,
    ld=7,
    oc=2,
    archpoints=75,
    core=["Crucible", "Deadly Demise 1", "Leader", "Scouts 9\""],
    faction_rules=["Voice of Command"],
    keywords=["VEHICLE", "WALKER", "CHARACTER", "SMOKE", "IMPERIUM", "OFFICER", "SENTINEL COMMANDER"],
    ability="Mobile Firebase: Ranged weapons equipped by models in this unit have the [ASSAULT] ability. This OFFICER can issue up to 1 Order to SQUADRON units.",
    composition="1 Sentinel Commander",
    leader="ARMOURED SENTINELS, SCOUT SENTINELS"
)

guard_archetypes = [front_line_commander,
                    augmented_bone_ead,
                    sentinel_commander]

# CHAOS DAEMONS

daemonic_herald = Archetype(
    name="Daemonic Herald",
    m=6,
    t=3,
    sv=7,
    ivl=0,
    w=3,
    ld=7,
    oc=1,
    archpoints=60,
    core=["Crucible", "Deep Strike", "Leader"],
    faction_rules=["Shadow of Chaos"],
    keywords=["INFANTRY", "CHARACTER", "CHAOS", "DAEMON", "SUMMONED", "DAEMONIC HERALD"],
    ability="Daemonic Locus: While this model is leading a unit, in your Command phase, you can return 1 destroyed Bodyguard model, or 03 destroyed models with the BATTLELINE keyword, to that unit.",
    composition="1 Daemonic Herald",
    leader="INFANTRY, DAEMON units (excluding POSSESSED units) which share one of the following keywords with this model: KHORNE, NURGLE, SLAANESH, TZEENTCH"
)

daemonic_charioteer = Archetype(
    name="Daemonic Charioteer",
    m=6,
    t=7,
    sv=6,
    ivl=0,
    w=8,
    ld=7,
    oc=3,
    archpoints=120,
    core=["Crucible", "Deep Strike", "Leader"],
    faction_rules=["Shadow of Chaos"],
    keywords=["MOUNTED", "CHARACTER", "CHAOS", "DAEMON", "DAEMONIC CHARIOTEER"],
    ability="Malefic Impact: Melee weapons equipped by models in this unit have [LANCE].",
    composition="1 Daemonic Charioteer",
    leader="MOUNTED, DAEMON units which share one of the following keywords with this model: KHORNE, NURGLE, SLAANESH, TZEENTCH"
)

immortal_champion = Archetype(
    name="Immortal Champion",
    m=8,
    t=10,
    sv=2,
    ivl=0,
    w=10,
    ld=6,
    oc=3,
    archpoints=180,
    core=["Crucible", "Deadly Demise D3", "Deep Strike"],
    faction_rules=["Shadow of Chaos"],
    keywords=["MONSTER", "CHARACTER", "CHAOS", "DAEMON", "IMMORTAL CHAMPION"],
    ability="Infernal Attendants: While this model is within 3\" of one or more friendly DAEMON INFANTRY units, this model has the Lone Operative ability. Font of Unreality: Each time an attack is allocated to a friendly DAEMON unit within 3\" of this model, subtract 1 from the Hit roll.",
    composition="1 Immortal Champion",
    leader=0
)

chaos_daemons_arch = [
    daemonic_charioteer,
    daemonic_herald,
    immortal_champion,
]