class Abilities:
    def __init__(self, name, description, abilpoint):
        self.name = name
        self.description = description
        self.abilpoint = abilpoint if abilpoint != None else 0

class Specialisms:
    def __init__(self, name, description, spepoint, remove_keywords, m, t, sv, inv_sv, w, add_keywords, remove_ability, add_ability, leader):
        self.name = name
        self.description = description
        self.spepoint = spepoint if spepoint != None else 0
        self.remove_keywords = remove_keywords if remove_keywords != None else 0
        self.m = m
        self.t = t
        self.sv = sv
        self.inv_sv = inv_sv
        self.w = w
        self.add_keywords = add_keywords if add_keywords != None else 0
        self.remove_ability = remove_ability if remove_ability != None else 0
        self.add_ability = add_ability if add_ability != None else 0
        self.leader = leader


no_specialism = Specialisms(
    name="No Specialism",
    description="This model has no specialism selected.",
    spepoint=None,
    remove_keywords=[],
    m=None,
    t=None,
    sv=None,
    inv_sv=None,
    w=None,
    add_keywords=[],
    remove_ability=[],
    add_ability=[],
    leader=None,

)

no_ability = Abilities(
    name="No Ability",
    description="This model has no ability selected.",
    abilpoint=0
)
# ============================================
# ADEPTUS ASTARTES
# ============================================

adamantine_will = Abilities(
    name="Adamantine Will",
    description="While this model is leading a unit, models in that unit have the Feel No Pain 4+ ability against Psychic Attacks.",
    abilpoint=0
)

astartes_banner = Abilities(
    name="Astartes Banner",
    description="Add 1 to the Objective Control characteristic of models in this unit.",
    abilpoint=0
)

blessing_of_the_omnissiah_AA = Abilities(
    name="Blessing of the Omnissiah",
    description="In your Command phase, you can select one friendly ADEPTUS ASTARTES VEHICLE model within 3\" of this model. That model regains up to D3 lost wounds and, until the start of your next Command phase, each time that VEHICLE model makes an attack, add 1 to the Hit roll. Each model can only be selected for this ability once per turn. (INFANTRY or MOUNTED only)",
    abilpoint=0
)

litany_of_hate = Abilities(
    name="Litany of Hate (+10pts)",
    description="Each time a model in this unit makes a melee attack, add 1 to the Wound roll.",
    abilpoint=10
)

narthecium = Abilities(
    name="Narthecium",
    description="While this model is leading a unit, in your Command phase, you can return 1 destroyed model (excluding CHARACTER models) to that unit.",
    abilpoint=0
)

rites_of_battle = Abilities(
    name="Rites of Battle",
    description="Once per battle round, one unit from your army with this ability can be targeted with a Stratagem for 0CP, even if another unit from your army has already been targeted with that Stratagem this phase.",
    abilpoint=0
)

tactical_precision = Abilities(
    name="Tactical Precision",
    description="Weapons equipped by models in this unit have the [LETHAL HITS] ability.",
    abilpoint=0
)

adeptus_astartes_abilities = [
    no_ability,
    adamantine_will,
    astartes_banner,
    blessing_of_the_omnissiah_AA,
    litany_of_hate,
    narthecium,
    rites_of_battle,
    tactical_precision
]

dreadie_abilities = adeptus_astartes_abilities.copy()
dreadie_abilities.remove(narthecium)
dreadie_abilities.remove(blessing_of_the_omnissiah_AA)


heavy_jumppack_and_gravis_armour = Specialisms(
    name="Heavy Jump Pack and MKX Gravis Armour",
    description="Change this model's Move characteristic to 10\", its Toughness characteristic to 6 and its Wounds characteristic to 5. Remove the Tacticus keyword, add the Jump Pack, Fly and Gravis keywords, it gains the Deep Strike ability and replace the list of units this model can be attached to: Inceptor Squad",
    spepoint=0,
    remove_keywords=["Tacticus"],
    m=10,
    t=6,
    sv=None,
    inv_sv=None,
    w=5,
    add_keywords=["Jump Pack", "Fly", "Gravis"],
    remove_ability=[],
    add_ability=["Deep Strike"],
    leader=["Inceptor Squad"]
)

jump_pack = Specialisms(
    name="Jump Pack",
    description="Change this model's Move characteristic to 12\", add the Fly and Jump Pack keywords, it gains the Deep Strike ability and replace the list of units this model can be attached to: Assault Intercessors with Jump Packs, Vanguard Veteran Squad with Jump Packs",
    spepoint=0,
    remove_keywords=[],
    m=12,
    t=None,
    sv=None,
    inv_sv=None,
    w=None,
    add_keywords=["Fly", "Jump Pack"],
    remove_ability=[],
    add_ability=["Deep Strike"],
    leader=["Assault Intercessors with Jump Packs", "Vanguard Veteran Squad with Jump Packs"]

)

mkx_gravis_armour = Specialisms(
    name="MKX Gravis Armour",
    description="Change this model's Move characteristic to 5\", its Toughness characteristic to 6 and its Wounds characteristic to 5. Remove the Tacticus keyword, add the Gravis keyword and replace the list of units this model can be attached to: Gravis (excluding Fly)",
    spepoint=0,
    remove_keywords=["Tacticus"],
    m=5,
    t=6,
    sv=None,
    inv_sv=None,
    w=5,
    add_keywords=["Gravis"],
    remove_ability=[],
    add_ability=[],
    leader=["Gravis"]
)

mkx_phobos_armour = Specialisms(
    name="MKX Phobos Armour",
    description="This model gains the Infiltrators and Stealth abilities, remove the Tacticus keyword, add the Phobos keyword, and replace the list of units this model can be attached to: Eliminator Squad, Incursor Squad, Infiltrator Squad, Reiver Squad, Scout Squad",
    spepoint=0,
    remove_keywords=["Tacticus"],
    m=None,
    t=None,
    sv=None,
    inv_sv=None,
    w=None,
    add_keywords=["Phobos"],
    remove_ability=[],
    add_ability=["Infiltrators", "Stealth"],
    leader=["Eliminator Squad", "Incursor Squad", "Infiltrator Squad", "Reiver Squad", "Scout Squad"]
)

raider_pattern_bike = Specialisms(
    name="Raider-pattern Bike (+15)",
    description="Change this model's Move characteristic to 12\", its Toughness characteristic to 5, and its Wounds characteristic to 5. Remove the Infantry and Tacticus keywords, add the Mounted keyword, it is equipped with 1 twin bolt rifle in addition to the weapons you choose in the next step, and replace the list of units this model can be attached to: Outrider Squad",
    spepoint=15,
    remove_keywords=["Infantry", "Tacticus"],
    m=12,
    t=5,
    sv=None,
    inv_sv=None,
    w=5,
    add_keywords=["Mounted"],
    remove_ability=[],
    add_ability=[],
    leader=["Outrider Squad"]
)

terminator_armour = Specialisms(
    name="Terminator Armour (+15pts)",
    description="Change this model's Move characteristic to 5\", its Toughness characteristic to 5, its Save characteristic to 2+, and its Wounds characteristic to 5. Remove the Tacticus keyword, add the Terminator keyword, it has a 4+ invulnerable save, it gains the Deep Strike ability, and replace the list of units this model can be attached to: Terminator Assault Squad, Terminator Squad",
    spepoint=15,
    remove_keywords=["Tacticus"],
    m=5,
    t=5,
    sv=2,
    inv_sv=4,
    w=5,
    add_keywords=["Terminator"],
    remove_ability=[],
    add_ability=["Deep Strike"],
    leader=["Terminator Assault Squad", "Terminator Squad"]
)

conversion_field = Specialisms(
    name="Conversion Field (+10)",
    description="This model has a 4+ invulnerable save",
    spepoint=10,
    remove_keywords=[],
    m=None,
    t=None,
    sv=None,
    inv_sv=4,
    w=None,
    add_keywords=[],
    remove_ability=[],
    add_ability=[],
    leader=[]
)

astartes_specialisms = [
    heavy_jumppack_and_gravis_armour,
    jump_pack,
    mkx_gravis_armour,
    mkx_phobos_armour,
    raider_pattern_bike,
    terminator_armour,
    conversion_field
]

dreadie_specialisms = [
    conversion_field
]

# ============================================
# T'AU EMPIRE
# ============================================

cunning_ambush = Abilities(
    name="Cunning Ambush",
    description="After both players have deployed their armies, you can redeploy this model's unit and one other friendly T'AU EMPIRE unit. When doing so, any of those units can be placed into Strategic Reserves, regardless of how many units are already in Strategic Reserves.",
    abilpoint=0
)

fire_and_fade = Abilities(
    name="Fire and Fade",
    description="In your Shooting phase, after this unit has shot, if it is not within Engagement Range of one or more enemy units, it can make a Normal move of up to 6\". If it does, until the end of the turn, this unit is not eligible to declare a charge. [KINBAND CHAMPION only]",
    abilpoint=0
)

fire_discipline = Abilities(
    name="Fire Discipline",
    description="Each time this unit makes a ranged attack, re-roll a Hit roll of 1.",
    abilpoint=0
)

ritual_butchery = Abilities(
    name="Ritual Butchery",
    description="While this model is leading a unit, melee weapons equipped by models in that unit have the [SUSTAINED HITS 1] ability.",
    abilpoint=0
)

warrior_bond = Abilities(
    name="Warrior Bond",
    description="Once per battle, at the start of any phase, you can select one friendly T'AU EMPIRE unit that is Battle-shocked and within 12\" of this model. That unit is no longer Battle-shocked.",
    abilpoint=0
)

kinband_abilities = [
    no_ability,
    cunning_ambush,
    fire_and_fade,
    fire_discipline,
    ritual_butchery,
    warrior_bond
]

shasnelvet_abilities = kinband_abilities.copy()
shasnelvet_abilities.remove(fire_and_fade)
shasnelvet_abilities.remove(ritual_butchery)

broadside_battlesuit = Specialisms(
    name="Broadside Battlesuit",
    description="Change this model's Move characteristic to 5\", its Toughness characteristic to 6, its Save characteristic to 2+, and its Wounds characteristic to 10. Remove the Infantry keyword, add the Vehicle and Walker keywords, and remove the Infiltrators and Stealth abilities. It can be equipped with up to three ranged weapons, and replace the list of units this model can be attached to: Broadside Battlesuits.",
    spepoint=0,
    remove_keywords=["Infantry"],
    m=5,
    t=6,
    sv=2,
    inv_sv=0,
    w=10,
    add_keywords=["Vehicle", "Walker"],
    remove_ability=["Infiltrators", "Stealth"],
    add_ability=["up to three ranged weapons"],
    leader=["Broadside Battlesuits"]
)

battlesuit_specialisms = [
    broadside_battlesuit
]


kalamandra = Specialisms(
    name="Kalamandra(+25)",
    description="Change this model's Move characteristic to 12\", its Toughness characteristic to 5, its Save characteristic to 5+, its Wounds characteristic to 6, and it is equipped with 1 kalamandra's bite in addition to the weapons you choose in Step 4. Remove the Infantry keyword, add the Mounted keyword and it gains the Lone Operative ability.",
    spepoint=225,
    remove_keywords=["Infantry"],
    m=12,
    t=5,
    sv=5,
    inv_sv=None,
    w=6,
    add_keywords=["Mounted"],
    remove_ability=[],
    add_ability=["Lone Operative"],
    leader=[]
)

krootox = Specialisms(
    name="Krootox(+10)",
    description="Change this model's Toughness characteristic to 6, its Save characteristic to 5+ and its Wounds characteristic to 7, and it is equipped with 1 Rampager fists in addition to the weapons you choose in Step 4. Remove the Infantry keyword, add the Mounted keyword, and replace the list of units this model can be attached to: Krootox Rampagers, Krootox Riders.",
    spepoint=10,
    remove_keywords=["Infantry"],
    m=0,
    t=6,
    sv=5,
    inv_sv=None,
    w=7,
    add_keywords=["Mounted"],
    remove_ability=[],
    add_ability=[],
    leader=["Krootox Rampagers", "Krootox Riders"]
)

kinband_specialisms = [
    kalamandra,
    krootox,
]


veteran_scout = Specialisms(
    name="Veteran Scout",
    description="Change this model's Move characteristic to 7\", it gains the Scouts 7\" ability, and replace the list of units this model can be attached to: Pathfinder Team.",
    spepoint=0,
    remove_keywords=[],
    m=7,
    t=None,
    sv=None,
    inv_sv=None,
    w=None,
    add_keywords=[],
    remove_ability=[],
    add_ability=["Scouts 7\""],
    leader=["Pathfinder Team"]
)

shasnel_specialisms = [
    veteran_scout
]
# ============================================
# DEATH GUARD
# ============================================

foul_infusion = Abilities(
    name="Foul Infusion (+10pts)",
    description="While this model is leading a unit, weapons equipped by models in that unit have the [LETHAL HITS] ability. In addition, each time a model in that unit makes an attack, a Critical Hit is scored on an unmodified Hit roll of 5+, instead of only a 6.",
    abilpoint=10
)

malicious_calculations = Abilities(
    name="Malicious Calculations",
    description="While this model is leading a unit, each time a model in that unit makes an attack, you can ignore any or all modifiers to that attack's Ballistic Skill or Weapon Skill characteristics and/or any or all modifiers to the Hit roll.",
    abilpoint=0
)

putrefying_stink = Abilities(
    name="Putrefying Stink",
    description="Enemy models cannot start or end an Advance move within 9\" of this model.",
    abilpoint=0
)

shroud_of_disease = Abilities(
    name="Shroud of Disease",
    description="While this model is leading a unit, that unit cannot be targeted by ranged attacks unless the attacking model is within 18\".",
    abilpoint=0
)

sickening_vitality = Abilities(
    name="Sickening Vitality",
    description="While this model is leading a unit, add 1\" to the Move characteristic of models in that unit and you can re-roll Advance and Charge rolls made for that unit.",
    abilpoint=10
)

tainted_narthecium = Abilities(
    name="Tainted Narthecium (+10pts)",
    description="While this model is leading a unit, in your Command phase, you can return 1 destroyed Bodyguard model to that unit.",
    abilpoint=10
)

tocsin_of_misery = Abilities(
    name="Tocsin of Misery",
    description="In the Battle-shock step of your opponent's Command phase, if an enemy unit that is below its Starting Strength is within 9\" of this model, that enemy unit must take a Battle-shock test, subtracting 1 from that test if it is a PSYKER unit.",
    abilpoint=0
)

unclean_icon = Abilities(
    name="Unclean Icon",
    description="While this model is leading a unit, add 1 to the Objective Control characteristic of models in that unit.",
    abilpoint=0
)

vector_of_disease = Abilities(
    name="Vector of Disease",
    description="While this model is leading a unit, melee weapons equipped by models in that unit have the [SUSTAINED HITS 1] and [LANCE] abilities.",
    abilpoint=0
)

death_guard_abilities = [
    no_ability,
    foul_infusion,
    malicious_calculations,
    putrefying_stink,
    shroud_of_disease,
    sickening_vitality,
    tainted_narthecium,
    tocsin_of_misery,
    unclean_icon,
    vector_of_disease
]


corrupted_with_infection = Specialisms(
    name="Corrupted With Infection",
    description="This model gains the Deadly Demise D3 ability",
    spepoint=0,
    remove_keywords=[],
    m=None,
    t=None,
    sv=None,
    inv_sv=None,
    w=None,
    add_keywords=[],
    remove_ability=[],
    add_ability=["Deadly Demise D3"],
    leader=None
)

terminator_armour_chaos = Specialisms(
    name="Terminator Armour",
    description="Change this model's Toughness characteristic to 7, its Save characteristic to 2+, its Wounds characteristic to 5, and it has a 4+ invulnerable save. Add the Terminator keyword, it gains the Deep Strike ability, and replace the list of units this model can be attached to: Blightlord Terminators, Deathshroud Terminators",
    spepoint=0,
    remove_keywords=[],
    m=None,
    t=7,
    sv=2,
    inv_sv=4,
    w=5,
    add_keywords=["Terminator"],
    remove_ability=[],
    add_ability=["4+ invulnerable save", "Deep Strike"],
    leader=["Blightlord Terminators", "Deathshroud Terminators"]
)

death_guard_specialisms = [
    terminator_armour_chaos,
    corrupted_with_infection
]
# ============================================
# GUARD
# ============================================

Dauntless_veteran = Abilities(
    name="Dauntless Veteran",
    description="You can re-roll Battle-shock tests for this unit.",
    abilpoint=0
)

rare_coordinator = Abilities(
    name="Fire Coordinator",
    description="Ranged weapons equipped by models in this unit have the [SUSTAINED HITS 1] ability.",
    abilpoint=0
)

partial_zealot = Abilities(
    name="Martial Zealot",
    description="Melee weapons equipped by models in this unit have the [SUSTAINED HITS 1] ability.",
    abilpoint=0
)

Guard_abilities = [
    no_ability,
    Dauntless_veteran,
    rare_coordinator,
    partial_zealot
]
brute_shield = Specialisms(
    name="Brute Shield",
    description="This model has a 4+ invulnerable save.",
    spepoint=0,
    remove_keywords=[],
    m=None,
    t=None,
    sv=None,
    inv_sv=4,
    w=None,
    add_keywords=[],
    remove_ability=[],
    add_ability=[],
    leader=[]
)

slabshield = Specialisms(
    name="Slabshield",
    description="Change this model's Wound characteristic to 7.",
    spepoint=0,
    remove_keywords=[],
    m=None,
    t=None,
    sv=None,
    inv_sv=None,
    w=7,
    add_keywords=[],
    remove_ability=[],
    add_ability=[],
    leader=[]
)

augmented_specialism = [
    brute_shield,
    slabshield
]
noble_steed = Specialisms(
    name="Noble Steed",
    description="(Front-line Commander only): Change this model's Move characteristic to 12\", change its Toughness characteristic to 4 and change its Save characteristic to 4+. Remove the Infantry keyword, add the Mounted keyword, and add to the list of units this model can be attached to: Attilan Rough Riders, Death Riders.",
    spepoint=0,
    remove_keywords=["INFANTRY"],
    m=12,
    t=4,
    sv=4,
    inv_sv=None,
    w=None,
    add_keywords=["MOUNTED"],
    remove_ability=[],
    add_ability=[],
    leader=["Attilan Rough Riders", "Death Riders"]
)

FLC_specialisms = [
    noble_steed
]
extra_armour = Specialisms(
    name="Extra Armour",
    description="Change this model's Move characteristic to 8\", change its Toughness characteristic to 8, change its Save characteristic to 2+, and it loses the Scouts 9\" ability.",
    spepoint=0,
    remove_keywords=[],
    m=8,
    t=8,
    sv=2,
    inv_sv=None,
    w=None,
    add_keywords=[],
    remove_ability=["Scouts 9\""],
    add_ability=[],
    leader=[]
)

sentinel_specialisms = [
    extra_armour
]
# ============================================
# GREY KNIGHTS
# ============================================

blessing_of_the_omnissiah_GK = Abilities(
    name="Blending of the Omnissiah",
    description="In your Command phase, you can select one friendly GREY KNIGHTS VEHICLE model within 3\" of this model. That model regains up to D3 lost wounds and, until the start of your next Command phase, each time that model makes an attack, add 1 to the Hit roll. Each model can only be selected for this ability once per turn. (INFANTRY only)",
    abilpoint=0
)

clarion_of_haste = Abilities(
    name="Clarion of Haste",
    description="While this model is leading a unit, that unit is eligible to declare a charge in a turn in which it Advanced. (Psychic)",
    abilpoint=0
)

eye_of_judgement = Abilities(
    name="Eye of Judgement (+10pts)[Psychic]",
    description="Each time this model makes an attack, you can re-roll the wound roll.",
    abilpoint=10
)

haloed_in_soulfire = Abilities(
    name="Haloed in Soulfire [Psychic]",
    description="While this model is leading a unit, that unit can only be selected as the target of a ranged attack if the attacking model is within 18\".",
    abilpoint=0
)

hammerhead = Abilities(
    name="Hammerhead [Psychic]",
    description="While this model is leading a unit, melee weapons equipped by models in that unit have the [LETHAL HITS] ability.",
    abilpoint=0
)

litanies_of_sanctity = Abilities(
    name="Litanies of Sanctity",
    description="Once per battle, at the start of any phase, you can select one friendly GREY KNIGHTS unit that is Battle-shocked and within 12\" of this model. That unit is no longer Battle-shocked.",
    abilpoint=0
)

sanctic_hood = Abilities(
    name="Sanctic Hood",
    description="Models in this unit have the Feel No Pain 4+ ability against Psychic Attacks.",
    abilpoint=0
)

warrior_strategist = Abilities(
    name="Warrior Strategist",
    description="Once per battle round, one model from your army with this ability can use it when its unit is targeted with a Stratagem. If it does, reduce the CP cost of that use of that Stratagem by 1CP.",
    abilpoint=0
)

zealous_path = Abilities(
    name="Zealous Path",
    description="While this model is leading a unit, you can re-roll Charge rolls made for that unit.",
    abilpoint=0
)

grey_knights_abilities_infantry = [
    no_ability,
    blessing_of_the_omnissiah_GK,
    clarion_of_haste,
    eye_of_judgement,
    haloed_in_soulfire,
    hammerhead,
    litanies_of_sanctity,
    sanctic_hood,
    warrior_strategist,
    zealous_path
]

grey_knights_abilities_vehicles = grey_knights_abilities_infantry.copy()
grey_knights_abilities_vehicles.remove(blessing_of_the_omnissiah_GK)

order_of_purifiers = Specialisms(
    name="Order of Purifiers",
    description="Add the Purifier keyword, and add to the list of units this model can be attached to: Purifiers.",
    spepoint=0,
    remove_keywords=[],
    m=None,
    t=None,
    sv=None,
    inv_sv=None,
    w=None,
    add_keywords=["Purifier"],
    remove_ability=[],
    add_ability=[],
    leader=["Purifiers"]
)

personal_teleporter = Specialisms(
    name="Personal Teleporter",
    description="Change this model's Move characteristic to 12\", and add the Fly keyword. Replace the list of units this model can be attached to: Interceptor Squad.",
    spepoint=0,
    remove_keywords=[],
    m=12,
    t=None,
    sv=None,
    inv_sv=None,
    w=None,
    add_keywords=["Fly"],
    remove_ability=[],
    add_ability=[],
    leader=["Interceptor Squad"]
)

prognosticars_foresight = Specialisms(
    name="Prognosticars' Foresight",
    description="This model has the Scouts 6\" ability.",
    spepoint=0,
    remove_keywords=[],
    m=None,
    t=None,
    sv=None,
    inv_sv=None,
    w=None,
    add_keywords=[],
    remove_ability=[],
    add_ability=["Scouts 6\""],
    leader=[]
)

terminator_armour_gk = Specialisms(
    name="Terminator Armour",
    description="Change this model's Move characteristic to 5\", its Toughness and Wounds characteristics to 5, and add the Terminator keyword. Replace the list of units this model can be attached to: Brotherhood Terminator Squad, Paladin Squad.",
    spepoint=0,
    remove_keywords=[],
    m=5,
    t=5,
    sv=None,
    inv_sv=None,
    w=5,
    add_keywords=["Terminator"],
    remove_ability=[],
    add_ability=[],
    leader=["Brotherhood Terminator Squad", "Paladin Squad"]
)

GK_infantry_specialisms = [
    order_of_purifiers,
    personal_teleporter,
    prognosticars_foresight,
    terminator_armour_gk
]

GK_vehicles_specialisms = [
    prognosticars_foresight
]

# ============================================
# BLACK TEMPLARS
# ============================================

armour_of_faith = Abilities(
    name="Armour of Faith",
    description="Once per phase, when an attack is allocated to this model and the saving throw is failed, you can change the Damage characteristic of that attack to 0. (INFANTRY and MOUNTED only) *No more than one per army. You cannot include this model in an army that includes an EMPEROR'S CHAMPION model.*",
    abilpoint=0
)

condemnatory_annihilation = Abilities(
    name="Condemnatory Annihilation",
    description="Each time this model's unit has fought, if one or more enemy units were destroyed as a result of those attacks, each enemy unit within 6\" of this model must take a Battle-shock test.",
    abilpoint=0
)

inspirational_exemplar = Abilities(
    name="Inspirational Exemplar",
    description="While this model is leading a unit, each time a model in that unit makes a melee attack, an unmodified Hit roll of 5+ scores a Critical Hit.",
    abilpoint=0
)

remorseless_persecution = Abilities(
    name="Remorseless Persecution (+10pts)",
    description="While this model is leading a unit, that unit is eligible to declare a charge in a turn in which it Advanced.",
    abilpoint=10
)

vehement_aggression = Abilities(
    name="Vehement Aggression",
    description="While this model is leading a unit, each time that unit is selected to fight, take a Leadership test for that unit: if passed, until the end of the phase, each time a model in that unit makes an attack, you can re-roll the Hit roll; if failed, until the end of the phase, each time a model in that unit makes an attack, re-roll a Hit roll of 1.",
    abilpoint=20
)

vengeful_exhortation = Abilities(
    name="Vengeful Exhortation",
    description="While this model is leading a unit, each time a model in that unit is destroyed by a melee attack, if it has not fought this phase, roll one D6: on a 4+, do not remove it from play. The destroyed model can fight after the attacking unit has finished making its attacks, and is then removed from play.",
    abilpoint=0
)


black_templars_abilities = [
    no_ability,
    armour_of_faith,
    condemnatory_annihilation,
    inspirational_exemplar,
    remorseless_persecution,
    vehement_aggression,
    vengeful_exhortation
]

black_templars_abilities.extend(adeptus_astartes_abilities)

black_templars_dreadie_abilities = black_templars_abilities.copy()
black_templars_dreadie_abilities.remove(armour_of_faith)
black_templars_dreadie_abilities.remove(vehement_aggression)


# ============================================
# KHORNE DAEMONS
# ============================================
daemonic_wings = Specialisms(
    name="Daemonic Wings",
    description="Add 4\" to this model's Move characteristic and it has the FLY keyword.",
    spepoint=0,
    remove_keywords=[],
    m=4,
    t=0,
    sv=0,
    inv_sv=0,
    w=0,
    add_keywords=["FLY"],
    remove_ability=[],
    add_ability=[],
    leader=[]
)

collar_of_khorne = Specialisms(
    name="Collar of Khorne",
    description="This model has the Feel No Pain 3+ ability against Psychic Attacks.",
    spepoint=0,
    remove_keywords=[],
    m=0,
    t=0,
    sv=0,
    inv_sv=0,
    w=0,
    add_keywords=[],
    remove_ability=[],
    add_ability=["Feel No Pain 3+ against Psychic Attacks"],
    leader=[]
)

juggernaut_of_khorne = Specialisms(
    name="Juggernaut of Khorne (+20 pts)",
    description="Improve this model's Move characteristic by 2\", its Toughness characteristic by 3, change its Save characteristic to 3+, it is equipped with 1 Juggernaut's bladed horn in addition to the weapons you choose in Step 4, change its INFANTRY keyword to MOUNTED, and replace the list of units this model can be attached to: BLOODCRUSHERS.",
    spepoint=20,
    remove_keywords=["INFANTRY"],
    m=2,
    t=3,
    sv=3,
    inv_sv=0,
    w=0,
    add_keywords=["MOUNTED"],
    remove_ability=[],
    add_ability=["Juggernaut's bladed horn"],
    leader=["BLOODCRUSHERS"]
)

khorne_infantry_specialisms = [
    collar_of_khorne,
    juggernaut_of_khorne,
]

khorne_mounted_specialisms = khorne_infantry_specialisms.copy()
khorne_mounted_specialisms.remove(juggernaut_of_khorne)

khorne_monster_specialisms = khorne_mounted_specialisms.copy()
khorne_monster_specialisms.append(daemonic_wings)

bloodmarked = Abilities(
    name="Bloodmarked (+20 pts)",
    description="At the start of the Fight phase, select one enemy unit within 18\" of and visible to this model. Until the end of the phase, each time a friendly KHORNE unit makes an attack that targets that unit, improve the Strength, Armour Penetration and Damage characteristics of that attack by 1.",
    abilpoint=20
)

rage_fuelled_strength = Abilities(
    name="Rage-fuelled Strength (+10 pts)",
    description="Each time a model in this unit makes an attack, add 1 to the Wound roll.",
    abilpoint=10
)

restless_prey_seeker = Abilities(
    name="Restless Prey-seeker",
    description="You can re-roll Advance and Charge rolls made for this unit.",
    abilpoint=0
)
khorne_infantry_abilities = [
    bloodmarked,
    rage_fuelled_strength,
    restless_prey_seeker
]

khorne_other_abilities = khorne_infantry_abilities.copy()
khorne_other_abilities.remove(rage_fuelled_strength)

#=========================================
#Nurgle Daemons
#=========================================

giggling_balemite = Specialisms(
    name="Giggling Balemite",
    description="Replace this model's INFANTRY keyword with the SWARM keyword, and replace the list of units this model can be attached to: NURGLINGS.",
    spepoint=0,
    remove_keywords=["INFANTRY"],
    m=0,
    t=0,
    sv=0,
    inv_sv=0,
    w=0,
    add_keywords=["SWARM"],
    remove_ability=[],
    add_ability=[],
    leader=["NURGLINGS"]
)

rot_fly = Specialisms(
    name="Rot Fly (+10 pts)",
    description="Improve this model's Move characteristic by 4\", its Toughness characteristic by 3, replace its INFANTRY keyword with the MOUNTED and FLY keywords, and replace the list of units this model can be attached to: PLAGUE DRONES.",
    spepoint=10,
    remove_keywords=["INFANTRY"],
    m=4,
    t=3,
    sv=0,
    inv_sv=0,
    w=0,
    add_keywords=["MOUNTED", "FLY"],
    remove_ability=[],
    add_ability=[],
    leader=["PLAGUE DRONES"]
)

nurgle_infantry_specialisms = [
    giggling_balemite,
    rot_fly
]

nurgle_mounted_specialisms = [

]

nurgle_monster_specialisms = [
    daemonic_wings
]

jolly_gutpipes = Abilities(
    name="Jolly Gutpipes",
    description= "This model is leading a unit, add 1\" to the Move characteristic of models in that unit and you can re-roll Advance rolls made for it.",
    abilpoint=0
)

keep_counting = Abilities(
    name="Keep Counting!",
    description="Melee weapons equipped by models in this unit have the [SUSTAINED HITS 1] ability.",
    abilpoint=0
)

meet_your_quota = Abilities(
    name="Meet Your Quota!",
    description="While this model's unit is not Battle-shocked, add 1 to the Objective Control characteristic of models in that unit.",
    abilpoint=0
)

nurgle_abilities = [
    jolly_gutpipes,
    keep_counting,
    meet_your_quota
]

#===========================
#Slaanesh Daemons
#===========================

perfumed_fog = Specialisms(
    name="Perfumed Fog",
    description="This unit has the SMOKE keyword.",
    spepoint=0,
    remove_keywords=[],
    m=0,
    t=0,
    sv=0,
    inv_sv=0,
    w=0,
    add_keywords=["SMOKE"],
    remove_ability=[],
    add_ability=[],
    leader=[]
)

steed_of_slaanesh = Specialisms(
    name="Steed of Slaanesh (+10 pts)",
    description="Improve this model's Move characteristic by 5\", its Toughness characteristic by 1 and its Wounds characteristic by 2, add the Scouts 9\" ability, change its INFANTRY keyword to MOUNTED, and replace the list of units this model can be attached to: SEEKERS.",
    spepoint=10,
    remove_keywords=["INFANTRY"],
    m=5,
    t=1,
    sv=0,
    inv_sv=0,
    w=2,
    add_keywords=["MOUNTED"],
    remove_ability=[],
    add_ability=["Scouts 9\""],
    leader=["SEEKERS"]
)

slaanesh_infantry_specialisms = [
    perfumed_fog,
    steed_of_slaanesh
]

slaanesh_mounted_specialisms = slaanesh_infantry_specialisms.copy()
slaanesh_mounted_specialisms.remove(steed_of_slaanesh)
slaanesh_monster_specialisms = slaanesh_mounted_specialisms.copy()
slaanesh_monster_specialisms.append(daemonic_wings)

discordant_disruption = Abilities(
    name="Discordant Disruption [Aura]",
    description="While an enemy PSYKER unit is within 12\" of this model, Psychic weapons equipped by models in that unit have the [HAZARDOUS] ability.",
    abilpoint=0
)

sadistic_savagery = Abilities(
    name="Sadistic Savagery",
    description="Melee weapons equipped by models in this unit have the [SUSTAINED HITS 1] ability.",
    abilpoint=0
)

swallow_energy = Abilities(
    name="Swallow Energy",
    description="Models in this unit have the Feel No Pain 4+ ability against mortal wounds and Psychic Attacks.",
    abilpoint=0
)

slaanesh_abilities = [
    discordant_disruption,
    sadistic_savagery,
    swallow_energy
]

#================================
#Tzeentch Daemons
#================================

disc_of_tzeentch = Specialisms(
    name="Disc of Tzeentch",
    description="Improve this model's Move characteristic by 6\", change its INFANTRY keyword to MOUNTED, add the FLY keyword, and replace the list of units this model can be attached to: SCREAMERS.",
    spepoint=0,
    remove_keywords=["INFANTRY"],
    m=6,
    t=0,
    sv=0,
    inv_sv=0,
    w=0,
    add_keywords=["MOUNTED", "FLY"],
    remove_ability=[],
    add_ability=[],
    leader=["SCREAMERS"]
)

eldritch_flames = Specialisms(
    name="Eldritch Flames",
    description="In your Shooting phase, after this model has shot, select one enemy unit that was hit by one or more of those attacks. Until the end of the phase, that unit cannot have the Benefit of Cover.",
    spepoint=0,
    remove_keywords=[],
    m=0,
    t=0,
    sv=0,
    inv_sv=0,
    w=0,
    add_keywords=[],
    remove_ability=[],
    add_ability=["Deny Cover"],
    leader=[]
)

tzeentch_infantry_specialisms = [
    disc_of_tzeentch,
    eldritch_flames
]

tzeentch_mounted_specialisms = tzeentch_infantry_specialisms.copy()
tzeentch_mounted_specialisms.remove(disc_of_tzeentch)
tzeentch_monster_specialisms = tzeentch_mounted_specialisms.copy()
tzeentch_monster_specialisms.append(daemonic_wings)

blazing_warpfire = Abilities(
    name="Blazing Warpfire",
    description="Ranged weapons equipped by models in this unit have the [ASSAULT] ability.",
    abilpoint=0
)

malefic_deceit = Abilities(
    name="Malefic Deceit",
    description="Each time an attack is made against this unit, subtract 1 from the Hit roll.",
    abilpoint=0
)

rider_of_the_immaterial_winds = Abilities(
    name="Rider of the Immaterial Winds",
    description="Once per battle, at the end of your opponent's turn, if this model's unit is not within Engagement Range of one or more enemy units, you can remove that unit from the battlefield and place it into Strategic Reserves.",
    abilpoint=0
)

tzeentch_abilities = [
    blazing_warpfire,
    malefic_deceit,
    rider_of_the_immaterial_winds
]
