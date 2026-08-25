# Ranged weapons profiles
from Archetypes import battlesuit_veteran
from Specialisms_and_Abilities import broadside_battlesuit


class weaponclass:
    def __init__(self, name,range,attacks,skill,strength,AP,Damage,Traits = None,points = None):
        self.name = name
        self.range = range
        self.attacks = attacks
        self.skill = skill
        self.strength = strength
        self.AP = AP
        self.Damage = Damage
        self.Traits = Traits if Traits != "" else None
        self.points = points if points != "" else None

# for weapons with multiple profiles
class Weapon:
    def __init__(self, name, profiles,points = None):
        self.name = name
        self.profiles = profiles
        self.points = points if points != "" else None



not_available = {"N/A"}

#Astartes Primary weapons
combi_weapon = weaponclass("Combi-weapon", 24, 1, "3+", 4, 0, 1, ["ANTI-INFANTRY 4+", "DEVASTATING WOUNDS", "RAPID FIRE 1"])
forge_bolter = weaponclass("Forge Bolter", 24, 3, "2+", 5, -1, 2)
master_crafted_bolt_carbine = weaponclass("Master-crafted bolt carbine", 24, 1, "2+", 4, -2, 2, ["PRECISION"])
master_crafted_bolter = weaponclass("Master-crafted bolter", 24, 2, "2+", 4, -1, 2)
master_crafted_heavy_bolt_rifle = weaponclass("Master-crafted heavy bolt rifle", 30, 2, "2+", 5, -1, 2)
smite_witchfire = weaponclass("Smite – witchfire", 24, "D6", "3+", 5, 1, "D3", ["PSYCHIC"])
smite_focused_witchfire = weaponclass("Smite – focused witchfire", 24, "D6", "3+", 6, -2, "D3", ["DEVASTATING WOUNDS", "HAZARDOUS", "PSYCHIC"])
storm_bolter = weaponclass("Storm bolter", 24, 2, "2+", 4, 0, 1, ["RAPID FIRE 2"])
twin_bolt_rifle = weaponclass("Twin bolt rifle", 24, 2, "3+", 4, 1, 1, ["TWIN-LINKED"])

astartes_primary = [combi_weapon,
                    forge_bolter,
                    master_crafted_bolt_carbine,
                    master_crafted_bolter,
                    master_crafted_heavy_bolt_rifle,
                    ]

# Astartes pistols
absolver_bolt_pistol = weaponclass("Absolver bolt pistol", 18, 1, "3+", 5, -1, 2, ["PISTOL"])
bolt_pistol = weaponclass("Bolt pistol", 12, 1, "2+", 4, 0, 1, ["PISTOL"])
boltstorm_gauntlet = weaponclass("Boltstorm gauntlet", 12, 3, "2+", 4, -1, 1, ["PISTOL"])
grav_pistol = weaponclass("Grav pistol", 12, 1, "2+", 4, -1, 1, ["ANTI-VEHICLE 2+", "PISTOL"])
hand_flamer = weaponclass("Hand flamer", 12, "D6", "N/A", 3, 0, 1, ["IGNORES COVER", "PISTOL", "TORRENT"])
heavy_bolt_pistol = weaponclass("Heavy bolt pistol", 18, 1, "2+", 4, -1, 1, ["PISTOL"])
inferno_pistol = weaponclass("Inferno pistol", 6, 1, "3+", 8, -4, "D3", ["MELTA 2", "PISTOL"])
neo_volkite_pistol = weaponclass("Neo-volkite pistol", 12, 1, "2+", 5, 0, 2, ["DEVASTATING WOUNDS", "PISTOL"])
plasma_pistol_standard = weaponclass("Plasma pistol – standard", 12, 1, "2+", 7, -2, 1, ["PISTOL"])
plasma_pistol_supercharge = weaponclass("Plasma pistol – supercharge", 12, 1, "2+", 8, -3, 2, ["HAZARDOUS", "PISTOL"])
plasma_pistol = Weapon("Plasma pistol",[plasma_pistol_standard,plasma_pistol_supercharge])

astartes_pistols  = [absolver_bolt_pistol,
                     bolt_pistol,
                     boltstorm_gauntlet,
                     grav_pistol,
                     hand_flamer,
                     heavy_bolt_pistol,
                     inferno_pistol,
                     neo_volkite_pistol,
                     plasma_pistol
                     ]
# Melee weapons
astartes_close_combat_weapon = weaponclass("Ceramite fist", "Melee", 6, "2+", 4, 0, 1)
crozius_arcanum = weaponclass("Crozius arcanum", "Melee", 5, "2+", 6, -1, 2)
force_weapon = weaponclass("Force weapon", "Melee", 4, "3+", 6, -1, "D3", ["PSYCHIC"])
master_crafted_chainsword = weaponclass("Master-crafted chainsword", "Melee", 7, "2+", 4, -1, 2, ["SUSTAINED HITS 1"])
master_crafted_power_weapon = weaponclass("Master-crafted power weapon", "Melee", 6, "2+", 5, -2, 2)
omission_power_axe = weaponclass("Omission power axe", "Melee", 4, "3+", 6, -2, 2)
power_fist = weaponclass("Power fist", "Melee", 5, "2+", 8, -2, 2)
servo_arm = weaponclass("Servo-arm", "Melee", 1, "3+", 8, -2, 3, ["EXTRA ATTACKS"])
thunder_hammer = weaponclass("Thunder hammer", "Melee", 5, "2+", 8, -2, 2, ["DEVASTATING WOUNDS"])
twin_lightning_claws = weaponclass("Twin lightning claws", "Melee", 6, "2+", 5, -2, 1)

astartes_melee = [astartes_close_combat_weapon,
                  crozius_arcanum,
                  force_weapon,
                  master_crafted_chainsword,
                  omission_power_axe,
                  power_fist,
                  servo_arm,
                  thunder_hammer,
                  twin_lightning_claws
                  ]

#Dreadnought ranged weapons
ballistus_lascannon = weaponclass("Ballistus lascannon ", 48, 2, "2+", 12, -3, "D6+1", [],10)
ballistus_missile_launcher_frag = weaponclass("Ballistus missile launcher - frag", 48, "2D6", "2+", 5, 0, 1, ["BLAST"])
ballistus_missile_launcher_krak = weaponclass("Ballistus missile launcher - krak", 48, 2, "2+", 10, -2, "D6")
ballistus_missile_launcher = Weapon('Ballistus missile launcher',[ballistus_missile_launcher_frag,ballistus_missile_launcher_krak])
brutalis_bolt_rifles = weaponclass("Brutalis bolt rifles", 24, 4, "2+", 4, -1, 1, ["TWIN-LINKED"])
heavy_flamer = weaponclass("Heavy flamer", 12, "D6", "N/A", 5, -1, 1, ["IGNORES COVER"])
heavy_onslaught_gatling_cannon = weaponclass("Heavy onslaught gatling cannon", 24, 12, "2+", 6, 0, 1, ["DEVASTATING WOUNDS"],10)
icarus_rocket_pod = weaponclass("Icarus rocket pod", 24, "D3", "2+", 8, -1, 2, ["ANTI FLY 2+"])
macro_plasma_incinerator_standard = weaponclass("Macro plasma incinerator - standard", 36, "D6+1", "2+", 8, -3, 2, ["BLAST"])
macro_plasma_incinerator_supercharge = weaponclass("Macro plasma incinerator - supercharge", 36, "D6+1", "2+", 9, -4, 3, ["BLAST", "HAZARDOUS"])
macro_plasma_incinerator = Weapon("Macro plasma incinerator",[macro_plasma_incinerator_standard,macro_plasma_incinerator_supercharge],10)
onslaught_gatling_cannon = weaponclass("Onslaught gatling cannon", 24, 8, "2+", 5, 0, 1, ["DEVASTATING WOUNDS"])
twin_fragstorm_grenade_launcher = weaponclass("Twin fragstorm grenade launcher", 18, "D6", "2+", 4, 0, 1, ["BLAST", "TWIN-LINKED"])
twin_heavy_bolter = weaponclass("Twin heavy bolter", 36, 3, "2+", 5, -1, 2, ["SUSTAINED HITS 1", "TWIN-LINKED"])
twin_icarus_ironhail_heavy_stubber = weaponclass("Twin Icarus ironhail heavy stubber", 36, 3, "2+", 4, 0, 1, ["ANTI-FLY 4+", "RAPID FIRE 2", "TWIN-LINKED"])
twin_multi_melta = weaponclass("Twin multi-melta", 18, 2, "2+", 9, -4, "D6", ["MELTA 2", "TWIN-LINKED"])
twin_storm_bolter = weaponclass("Twin storm bolter", 24, 2, "2+", 4, 0, 1, ["RAPID FIRE 2", "TWIN-LINKED"])

#Dreadnought melee weapons
armoured_feet = weaponclass("Armoured feet","Melee",4,"2+",7,0,1)
brutalis_fists = weaponclass("Brutalis fists", "Melee",6, "2+", 12, -2, 3,["TWIN-LINKED"])
brutalis_talons_strike = weaponclass("Brutalis talons - Strike", "Melee",6, "2+", 12, -2, 3,["TWIN-LINKED"])
brutalis_talons_sweep = weaponclass("Brutalis talons - Sweep", "Melee",10, "2+", 7, -2, 3,["TWIN-LINKED"])
brutalis_talons = Weapon('Brutalis talons',[brutalis_talons_sweep,brutalis_talons_strike])
redemptor_fist = weaponclass("Redemptor Fist", "Melee", 5, "2+", 12, -2, 3)

#comboed weapons for dreadie
ballistus_missile_launcher_feet = Weapon("Ballistus missile launcher and feet",[ballistus_missile_launcher_frag,ballistus_missile_launcher_krak,armoured_feet])
brutalis_bolt_rifles_fists = Weapon("Brutalis bolt rifles and Brutalis fist",[brutalis_bolt_rifles,brutalis_fists])
heavy_flamer_fist = Weapon("Heavy flamer and redemptor fist",[heavy_flamer,redemptor_fist])
onslaught_fist = Weapon("Onslaught gatling cannon and Redepmtor fist",[onslaught_gatling_cannon,redemptor_fist])
twin_bolter_icarus = Weapon("Twin heavy bolter and twin icarus ironhail heavy stubber",[twin_heavy_bolter,twin_icarus_ironhail_heavy_stubber])
twin_multi_melta_icarus = Weapon("Twin multi melta and twin icarus ironhail heavy stubber (+10pts)",[twin_multi_melta,twin_icarus_ironhail_heavy_stubber],10)

dreadie_1 = [ballistus_missile_launcher_feet,
             brutalis_bolt_rifles_fists,
             brutalis_talons,
             heavy_flamer_fist,
             onslaught_fist]

dreadie_2 = [ballistus_lascannon,
             heavy_onslaught_gatling_cannon,
             macro_plasma_incinerator]

dreadie_3 = [twin_fragstorm_grenade_launcher,
             twin_bolter_icarus,
             twin_multi_melta_icarus,
             twin_storm_bolter]

dreadie_4 = [icarus_rocket_pod]

#Black Templars ranged weapons
pyrebblaster = weaponclass("Pyrebblaster",12,"D6","N/A",5,0,1,["IGNORES COVER","TORRENT"])

#Black Templars pistols
pyre_pistol = weaponclass("Pyre Pistol", 12,"D6","N/A",4,0,1,["IGNORES COVER","TORRENT","PISTOL"])

#Black Templars melee
black_sword_strike = weaponclass("Black Sword - Strike", "Melee",6, "2+", 8, -3, 2, ["ANTI-CHARACTER 5+","PRECISION"])
black_sword_sweep = weaponclass("Black Sword - Sweep", "Melee",10, "2+", 6, -2, 1)

#Grey Knights ranged weapons
assault_cannon = weaponclass("Assault Cannon",24,6,"3+",6,0,1)
combi_weapon = weaponclass("Combi-weapon", 24, 1, "3+", 4, 0, 1, ["ANTI-INFANTRY 4+", "DEVASTATING WOUNDS", "RAPID FIRE 1"])
forge_bolter = weaponclass("Forge bolter", 24, 3, "2+", 5, -1, 2, [])
fragstrom_grenade_launcher = weaponclass("Fragstrom grenade launcher", 18, "D6", "3+", 4, 0, 1, ["BLAST"])
gatling_silencer = weaponclass("Gatling splencer", 24, 12, "3+", 6, 0, 1, ["PSYCHIC", "SUSTAINED HITS 1"])
heavy_flamer_p4 = weaponclass("Heavy flamer", 12, "D6", "N/A", 5, -1, 1, ["TORRENT", "IGNORES COVER"])
heavy_incinerator = weaponclass("Heavy incinerator", 18, "2D6", "N/A", 6, -1, 1, ["IGNORES COVER", "TORRENT"])
heavy_plasma_cannon_standard = weaponclass("Heavy plasma cannon - standard", 36, "D3", "3+", 7, -2, 2, ["BLAST"])
heavy_plasma_cannon_supercharge = weaponclass("Heavy plasma cannon - supercharge", 36, "D3", "3+", 8, -3, 2, ["BLAST", "HAZARDOUS"])
heavy_plasma_cannon = Weapon('Heavy plasma cannon',[heavy_plasma_cannon_standard, heavy_plasma_cannon_supercharge])
heavy_psycannon = weaponclass("Heavy psycannon", 24, 6, "3+", 10, -2, 3, ["IGNORES COVER", "PSYCHIC"])
incinerator = weaponclass("Incinerator", 12, "D6", "N/A", 6, -1, 1, ["IGNORES COVER", "TORRENT"])
psilencer = weaponclass("Psilencer", 24, 6, "2+", 5, 0, 1, ["PRECISION", "PSYCHIC", "SUSTAINED HITS 1"])
psycannon = weaponclass("Psycannon", 24, 3, "2+", 8, -1, 2, ["PSYCHIC"])
purifying_flame = weaponclass("Purifying Flame", 18, 3, "3+", 4, -2, 1, ["ANTI-INFANTRY 2+", "IGNORES COVER", "PSYCHIC"])
sublimator = weaponclass("Sublimator", 18, 2, "3+", 9, -4, "D6", ["MELTA 4", "PSYCHIC", "TWIN-LINKED"])
twin_lascannon = weaponclass("Twin lascannon", 48, 1, "3+", 12, -3, "D6+1", ["TWIN-LINKED"])
vortex_of_doom = weaponclass("Vortex of Doom", 18, "D6+3", "3+", 8, -2, 2, ["BLAST", "PSYCHIC"])


COT_ranged =    [combi_weapon,
                forge_bolter,
                incinerator,
                psilencer,
                psycannon,
                purifying_flame,
                storm_bolter,
                vortex_of_doom]

VDS_ranged = [assault_cannon,
              heavy_plasma_cannon,
              twin_lascannon]

DKC_ranged = [fragstrom_grenade_launcher,
              heavy_incinerator,
              heavy_psycannon,
              sublimator]
#grey knight pistols
grav_pistol = weaponclass ("Grav Pistol",12,1,"2+",4,-1,2,["ANTI-VEHICLE","PISTOL"])

GK_pistols  = [grav_pistol]

#grey knights melee
GK_close_combat_weapon = weaponclass("Ceramite Fists", "Melee", 5, "3+", 4, 0, 1)
crozius_arcanum = weaponclass("Crozius arcanum", "Melee", 5, "2+", 6, -1, 2)
dreadfists = weaponclass("Dreadfists", "Melee", 6, "2+", 6, -1, 1)
dreadnought_combat_weapon = weaponclass("Kick of the venerable", "Melee", 5, "3+", 12, -2, 3)
nemesis_daemon_greathammer = weaponclass("Nemesis daemon greathammer", "Melee", 5, "3+", 14, -3, "D6+1", ["PSYCHIC"])
nemesis_flail = weaponclass("Nemesis flail", "Melee", 10, "2+", 5, -1, 2, ["PSYCHIC"])
nemesis_force_weapon = weaponclass("Nemesis force weapon", "Melee", 5, "2+", 6, -2, 2, ["PSYCHIC"])
nemesis_greatsword_strike = weaponclass("Nemesis greatsword - strike", "Melee", 5, "2+", 10, -2, "D6", ["PSYCHIC"])
nemesis_greatsword_sweep = weaponclass("Nemesis greatsword - sweep", "Melee", 10, "2+", 5, -1, 1, ["PSYCHIC"])
nemesis_greatsword = Weapon('Nemesis greatsword',[nemesis_greatsword_strike,nemesis_greatsword_sweep])
nemesis_mace = weaponclass("Nemesis mace", "Melee", 5, "2+", 6, -3, 3, ["ANTI-CHARACTER 2+", "PRECISION", "PSYCHIC"])
servo_arm = weaponclass("Servo-arm", "Melee", 1, "3+", 8, -2, 3, ["EXTRA ATTACKS"])

COT_melee = [GK_close_combat_weapon,
             crozius_arcanum,
             nemesis_daemon_greathammer,
             omission_power_axe,
             servo_arm]

VDS_melee  = [dreadnought_combat_weapon
              ]

DKC_melee = [dreadfists,
             nemesis_flail,
             nemesis_daemon_greathammer,
             nemesis_greatsword,
             nemesis_mace
             ]

# ============ Guard weapons ============

# Standard Ranged Weapons (no asterisks)
autogun = weaponclass("Autogun", 24, 2, "3+", 3, 0, 1)
boltgun = weaponclass("Boltgun", 24, 1, "3+", 4, 0, 1, ["RAPID FIRE 1"])
combat_shotgun = weaponclass("Combat shotgun", 12, 2, "3+", 4, 0, 1, ["ASSAULT"])
lascarbine = weaponclass("Lascarbine", 18, 2, "3+", 3, 0, 1, ["ASSAULT"])
lasgun = weaponclass("Lasgun", 24, 1, "3+", 3, 0, 1, ["RAPID FIRE 1"])
zealots_vindicator_ranged = weaponclass("Zealot's vindicator", 12, "D6", "N/A", 5, 0, 1, ["IGNORES COVER", "TORRENT"])

# Sentinel Commander Ranged Weapons (*)
autocannon = weaponclass("Autocannon", 48, 2, "3+", 9, -1, 3, [])
heavy_flamer = weaponclass("Heavy flamer", 12, "D6", "N/A", 5, -1, 1, ["IGNORES COVER", "TORRENT"])
lascannon = weaponclass("Lascannon", 48, 1, "3+", 12, -3, "D6+1", [])
missile_launcher_frag = weaponclass("Missile launcher — frag", 48, "D6", "3+", 4, 0, 1, ["BLAST", "HEAVY"])
missile_launcher_krak = weaponclass("Missile launcher — krak", 48, 1, "3+", 9, -2, "D6", ["HEAVY"])
missile_launcher = Weapon("Missle Launcher",[missile_launcher_frag, missile_launcher_krak])
multi_laser = weaponclass("Multi-laser", 36, 4, "3+", 6, 0, 1, [])
plasma_cannon_standard = weaponclass("Plasma cannon — standard", 36, "D3", "3+", 7, -2, 1, ["BLAST"])
plasma_cannon_supercharge = weaponclass("Plasma cannon — supercharge", 36, "D3", "3+", 8, -3, 2, ["BLAST", "HAZARDOUS"])
plasma_cannon = Weapon("Plasma cannon",[plasma_cannon_standard,plasma_cannon_supercharge])

# Augmented Bone'ead Ranged Weapons (**)
grenadier_gauntlet_augmented = weaponclass("Grenadier gauntlet", 18, "D6", "3+", 4, 0, 1, ["BLAST"])
ripper_gun_augmented = weaponclass("Ripper gun", 18, 3, "3+", 5, -1, 2, ["RAPID FIRE 3"])

# ============ PISTOLS ============

# Standard Pistols (no asterisks)
autopistol = weaponclass("Autopistol", 12, 1, "3+", 3, 0, 1, ["PISTOL"])
bolt_pistol = weaponclass("Bolt pistol", 12, 1, "3+", 4, 0, 1, ["PISTOL"])
hand_flamer = weaponclass("Hand flamer", 12, "D6", "N/A", 3, 0, 1, ["IGNORES COVER", "PISTOL", "TORRENT"])
laspistol = weaponclass("Laspistol", 12, 1, "3+", 3, 0, 1, ["PISTOL"])

# ============ MELEE WEAPONS ============

# Standard Melee Weapons (no asterisks)
guard_chainsword = weaponclass("Chainsword", "Melee", 5, "3+", 3, 0, 1)
guard_close_combat_weapon = weaponclass("Gun butt", "Melee", 3, "3+", 3, 0, 1)
frag_lance = weaponclass("Frag lance", "Melee", "D6", "3+", 4, 0, 1, ["LANCE"])
load_lance = weaponclass("Load lance", "Melee", 2, "3+", 6, -2, 2, ["LANCE"])
hunting_lance_frag = weaponclass("Hunting lance — frag tip", "Melee", "D6", "3+", 4, 0, 1, ["LANCE"])
hunting_lance_melta = weaponclass("Hunting lance — melta tip", "Melee", 1, "3+", 9, -4, "D6", ["LANCE"])
hunting_lance = Weapon('Hunting lance', [hunting_lance_frag, hunting_lance_melta])
power_fist = weaponclass("Power fist", "Melee", 3, "3+", 6, -2, 2)
power_weapon = weaponclass("Power weapon", "Melee", 4, "3+", 4, -2, 1)
ripper_gun_melee = weaponclass("Ripper gun", "Melee", 5, "3+", 6, -1, 1)
zealots_vindicator_melee = weaponclass("Zealot's vindicator", "Melee", 4, "3+", 5, -1, 2)

# Sentinel Commander Melee Weapons (*)
sentinel_chainsaw = weaponclass("Sentinel chainsaw", "Melee", 3, "3+", 6, -1, 1)

# Augmented Bone ead Melee Weapons (**)
bullgryn_maul = weaponclass("Bullgryn maul", "Melee", 5, "3+", 7, -1, 2, [])
huge_knife = weaponclass("Huge knife", "Melee", 6, "3+", 8, -1, 2, [])

# Mounter Melee Weapons (***)
frag_lance_mounter = weaponclass("Frag lance", "Melee", "D6", "3+", 4, 0, 1, ["LANCE"])
load_lance_mounter = weaponclass("Load lance", "Melee", 2, "3+", 6, -2, 2, ["LANCE"])
hunting_lance_frag_mounter = weaponclass("Hunting lance — frag tip", "Melee", "D6", "3+", 4, 0, 1, ["LANCE"])
hunting_lance_melta_mounter = weaponclass("Hunting lance — melta tip", "Melee", 1, "3+", 9, -4, "D6", ["LANCE"])



# ============ LISTS ============

# Ranged Weapons
guard_ranged_weapons = [
    autogun,
    boltgun,
    combat_shotgun,
    lascarbine,
    lasgun,
    zealots_vindicator_ranged
]

# Ranged Weapons - Sentinel Commander only (*)
ranged_sentinel = [
    autocannon,
    heavy_flamer,
    lascannon,
    missile_launcher,
    multi_laser,
    plasma_cannon
]

# Ranged Weapons - Augmented Bone ead only
ranged_augmented = [
    grenadier_gauntlet_augmented,
    ripper_gun_augmented
]

# Pistols
guard_pistols = [
    autopistol,
    bolt_pistol,
    hand_flamer,
    laspistol,
    plasma_pistol
]

# Melee Weapons
guard_melee_weapons = [
    guard_chainsword,
    guard_close_combat_weapon,
    power_fist,
    power_weapon,
    zealots_vindicator_melee
]

# Melee Weapons - Sentinel Commander only (*)
melee_sentinel = [
    sentinel_chainsaw
]

# Melee Weapons - Augmented Bone ead only (**)
melee_augmented = [
    bullgryn_maul,
    huge_knife
]

# Melee Weapons - Mounter only (***)
melee_mounted = [
    frag_lance_mounter,
    load_lance_mounter,
    hunting_lance
]
#Tau

# ===== TAU WEAPONS =====

blast_javelin = weaponclass(name="Blast javelin", range='18"', attacks="D6", skill="4+", strength=10, AP=-2, Damage=2, Traits=["ASSAULT", "BLAST"])

burst_cannon = weaponclass(name="Burst cannon", range='18"', attacks=4, skill="3+", strength=5, AP=0, Damage=1, Traits=None)

dart_bow_and_tri_blade = weaponclass(name="Dart-bow and tri-blade", range='24"', attacks="D3+1", skill="4+", strength=4, AP=-1, Damage=2, Traits=["ANTI-INFANTRY 3+", "ASSAULT", "MELEE"])

dvorgite_skinner = weaponclass(name="Dvorgite skinner", range=12, attacks="D6", skill="N/A", strength=4, AP=-1, Damage=1, Traits=["IGNORES COVER", "TORRENT"])

fireblade_pulse_rifle = weaponclass(name="Fireblade pulse rifle", range='30"', attacks=1, skill="3+", strength=5, AP=0, Damage=2, Traits=["RAPID FIRE 1"])

fusion_blaster = weaponclass(name="Fusion blaster", range='12"', attacks=1, skill="3+", strength=9, AP=-4, Damage="D6", Traits=["MELTA 2"])

heavy_rail_rifle = weaponclass(name="Heavy rail rifle", range='60"', attacks=2, skill="3+", strength=12, AP=-4, Damage="D6+1", Traits=["DEVASTATING WOUNDS", "HEAVY"])

high_yield_missile_pods = weaponclass(name="High-yield missile pods", range='30"', attacks=3, skill="3+", strength=7, AP=-2, Damage=2, Traits=["TWIN-LINKED"])

ion_rifle = Weapon(
    name="Ion rifle",
    profiles=[
        weaponclass(name="Ion rifle - Standard", range='30"', attacks=3, skill="4+", strength=7, AP=-1, Damage=2, Traits=["HEAVY"]),
        weaponclass(name="Ion rifle - Overcharge", range='30"', attacks=3, skill="4+", strength=8, AP=-2, Damage=2, Traits=["HAZARDOUS", "HEAVY"]),
    ]
)

kroot_carbine = weaponclass(name="Kroot carbine", range='18"', attacks=1, skill="4+", strength=4, AP=-1, Damage=1, Traits=None)

kroot_long_gun = weaponclass(name="Kroot long gun", range='36"', attacks=1, skill="3+", strength=6, AP=-2, Damage=3, Traits=["HEAVY", "PRECISION"])

kroot_rifle = weaponclass(name="Kroot rifle", range='24"', attacks=1, skill="4+", strength=4, AP=-1, Damage=1, Traits=["RAPID FIRE 1"])

kroot_scattergun = weaponclass(name="Kroot scattergun", range='12"', attacks=2, skill="4+", strength=4, AP=0, Damage=1, Traits=["ASSAULT"])

londax_tribalest = weaponclass(name="Londax tribalest", range='18"', attacks=3, skill="5+", strength=7, AP=-1, Damage=1, Traits=["ANTI-VEHICLE 4+", "DEVASTATING WOUNDS", "HEAVY"])

pulse_blaster = weaponclass(name="Pulse blaster", range='10"', attacks=2, skill="3+", strength=6, AP=-1, Damage=1, Traits=["ASSAULT"])

pulse_carbine = weaponclass(name="Pulse carbine", range='20"', attacks=2, skill="3+", strength=5, AP=0, Damage=1, Traits=None)

rail_rifle = weaponclass(name="Rail rifle", range='30"', attacks=1, skill="4+", strength=10, AP=-4, Damage=3, Traits=["DEVASTATING WOUNDS", "HEAVY"])

seeker_missile = weaponclass(name="Seeker missile", range='48"', attacks=1, skill="3+", strength=14, AP=-3, Damage="D6+1", Traits=["ONE SHOT"])

semi_automatic_grenade_launchers = Weapon(
    name="Semi-automatic grenade launchers",
    profiles=[
        weaponclass(name="Semi-automatic grenade launchers - EMP", range='18"', attacks=1, skill="3+", strength=3, AP=0, Damage=1, Traits=["ANTI-VEHICLE 4+", "DEVASTATING WOUNDS"]),
        weaponclass(name="Semi-automatic grenade launchers - Fusion", range='18"', attacks=1, skill="3+", strength=6, AP=-1, Damage=3, Traits=None),
    ]
)

tanglebomb_launcher = weaponclass(name="Tanglebomb launcher", range='24"', attacks="D3", skill="4+", strength=3, AP=-3, Damage=1, Traits=["BLAST"])

twin_plasma_rifle = weaponclass(name="Twin plasma rifle", range='18"', attacks=1, skill="3+", strength=8, AP=-3, Damage=2, Traits=["TWIN-LINKED"])

twin_smart_missile_system = weaponclass(name="Twin smart missile system", range='30"', attacks=4, skill="3+", strength=5, AP=0, Damage=1, Traits=["INDIRECT FIRE", "TWIN-LINKED"])

kroot_ranged = [
    blast_javelin,
    dart_bow_and_tri_blade,
    dvorgite_skinner,
    kroot_carbine,
    kroot_rifle,
    kroot_scattergun,
    londax_tribalest,
    tanglebomb_launcher,

]

shasnel_ranged = [
    fireblade_pulse_rifle,
    ion_rifle,
    pulse_blaster,
    pulse_carbine,
    rail_rifle,
    semi_automatic_grenade_launchers,

]

battlesuit_veteran_ranged = [
    burst_cannon,
    fusion_blaster,
]

broadside_battlesuit_ranged = battlesuit_veteran_ranged.copy()
broadside_battlesuit_ranged.extend([heavy_rail_rifle,high_yield_missile_pods,seeker_missile,twin_smart_missile_system])

# ===== PISTOLS =====

kroot_pistol = weaponclass(name="Kroot pistol", range='12"', attacks=1, skill="4+", strength=4, AP=0, Damage=1, Traits=["PISTOL"])

kroot_pistol_and_hunting_javelins = weaponclass(name="Kroot pistol and hunting javelins", range='12"', attacks=2, skill="4+", strength=4, AP=0, Damage=1, Traits=["ASSAULT", "PISTOL"])

pulse_pistol = weaponclass(name="Pulse pistol", range='12"', attacks=1, skill="3+", strength=5, AP=0, Damage=1, Traits=["PISTOL"])

kroot_pistol_list = [kroot_pistol,
                     kroot_pistol_and_hunting_javelins]

shasnel_pistol = [pulse_pistol]

# ===== MELEE WEAPONS =====

bladestave_and_prey_hook = weaponclass(name="Bladestave and prey-hook", range="Melee", attacks=4, skill="2+", strength=5, AP=-2, Damage=1, Traits=["LETHAL HITS"])

tau_close_combat_weapon = weaponclass(name="Close-combat weapon", range="Melee", attacks=3, skill="4+", strength=3, AP=0, Damage=1, Traits=None)

crushing_bulk = weaponclass(name="Crushing bulk", range="Melee", attacks=3, skill="4+", strength=6, AP=0, Damage=1, Traits=None)

hunting_blades = weaponclass(name="Hunting blades", range="Melee", attacks=3, skill="4+", strength=4, AP=-1, Damage=1, Traits=["LANCE"])

kalamandras_bite = weaponclass(name="Kalamandra's bite", range="Melee", attacks=4, skill="4+", strength=5, AP=-1, Damage=1, Traits=["EXTRA ATTACKS"])

rampager_fists = weaponclass(name="Rampager fists", range="Melee", attacks=4, skill="3+", strength=6, AP=-1, Damage=2, Traits=["EXTRA ATTACKS", "SUSTAINED HITS 1"])

shapers_blade = weaponclass(name="Shaper's blade", range="Melee", attacks=4, skill="2+", strength=5, AP=-1, Damage=1, Traits=None)

twin_ritualistic_blades = weaponclass(name="Twin ritualistic blades", range="Melee", attacks=4, skill="2+", strength=5, AP=-1, Damage=1, Traits=["TWIN-LINKED"])

kroot_melee = [
    bladestave_and_prey_hook,
    tau_close_combat_weapon,
    hunting_blades,
    shapers_blade,
    twin_ritualistic_blades,
]
kalamandras_melee = kroot_melee.copy()
kalamandras_melee.extend([kalamandras_bite])

krootox_melee = kroot_melee.copy()
krootox_melee.extend({rampager_fists})

shasnel_melee  = [
    tau_close_combat_weapon,

]

broadside_battlesuit_melee = shasnel_melee.copy()
broadside_battlesuit_melee.extend([crushing_bulk])

# ====== DEATH GUARD WEAPONS =======


blight_launcher = weaponclass("Blight launcher", "24'", "D3", "2+", 6, -1, 2, ["BLAST, LETHAL HITS"])
DG_boltgun= weaponclass("Boltgun", "24'", 2, "2+", 4, 0, 1, ["LETHAL HITS"])
combi_bolter =   weaponclass("Combi-bolter", "24'", 2, "2+", 4, 0, 1, ["LETHAL HITS, RAPID FIRE 2"])
DG_combi_weapon = weaponclass("Combi-weapon", "24'", 1, "3+", 4, 0, 1, ["ANTI-INFANTRY 4+, DEVASTATING WOUNDS, RAPID FIRE 1"])
hyper_blight_grenades = weaponclass("Hyper blight grenades", "12'", 6, "2+", 7, -1, 2, ["ASSAULT, LETHAL HITS"])
DG_melta =   weaponclass("Melta gun", "12'", 1, "2+", 9, -4, 0, ["MELTA 2"])
plague_belcher = weaponclass("Plague belcher", "12'", 6, "N/A", 4, 0, 1, ["ANTI-INFANTRY 4+, IGNORES COVER, TORRENT"])
plague_spewer = weaponclass("Plague spewer", "12'", 6, "N/A", 5, -1, 1, ["ANTI-INFANTRY 2+, IGNORES COVER, TORRENT"])
plague_spitter = weaponclass("Plague spitter", "12'", 6, "N/A", 7, -2, 2, ["ANTI-INFANTRY 2+, IGNORES COVER, TORRENT"])
plague_wind_witchfire = weaponclass("Plague Wind — witchfire", "12'", 6, "N/A", 4, -1, 0, ["PSYCHIC, TORRENT"])
plague_wind_focused_witchfire = weaponclass("Plague Wind — focused witchfire", "12'", "6+3", "N/A", 6, -2, 0, ["HAZARDOUS, PSYCHIC, TORRENT"])
plague_wind = Weapon("Plague wind",[plague_wind_witchfire,plague_wind_focused_witchfire])
plasma_gun_standard =weaponclass("Plasma gun — standard", "24'", 1, "2+", 7, -1, 2, ["RAPID FIRE 1"])
plasma_gun_hazardous  =weaponclass("Plasma gun — supercharge", "24'", 1, "2+", 8, -3, 2, ["HAZARDOUS, RAPID FIRE 1"])
plasma_gun =  Weapon("Plasma gun",[plasma_gun_standard,plasma_gun_hazardous])
reaper_autocannon=weaponclass("Reaper autocannon", "36'", 4, "2+", 7, -1, 1, ["DEVASTATING WOUNDS, SUSTAINED HITS 1"])
twin_plague_spewer =weaponclass("Twin plague spewer", "12'", 6, "N/A", 5, -1, 1, ["ANTI-INFANTRY 2+, IGNORES COVER, TORRENT, TWIN-LINKED"])

dg_terminator_ranged = [
    blight_launcher,
    DG_boltgun,
    combi_bolter,
    DG_combi_weapon,
    hyper_blight_grenades,
    DG_melta,
    plague_belcher,
    plague_spewer,
    plague_spitter,
    plasma_gun,
    reaper_autocannon,
    twin_plague_spewer,
]

dg_infantry_ranged = dg_terminator_ranged.copy()
dg_infantry_ranged.remove(reaper_autocannon)
dg_infantry_ranged.remove(twin_plague_spewer)

plague_sorcerer_ranged = dg_infantry_ranged.copy()
plague_sorcerer_ranged.append(plague_wind)

# PISTOLS

injector_pistol  = weaponclass("Injector pistol", "3'", 1, "3+", 4, -1, 3, ["ANTI-INFANTRY 2+, PISTOL, PRECISION"])
plaguespurt_gauntlet =weaponclass("Plaguespurt gauntlet", "12'", 6, "N/A", 3, 0, 1, ["ANTI-INFANTRY 4+, IGNORES COVER, PISTOL, TORRENT"])

dg_infantry_pistols = [bolt_pistol,
              injector_pistol,
              plasma_pistol]

dg_terminator_pistols = [plaguespurt_gauntlet]

# MELEE WEAPONS

balesword =weaponclass("Balesword", "Melee", 4, "2+", 5, -2, 2, ["LETHAL HITS"])
bubotic_weapons =weaponclass("Bubotic weapons", "Melee", 5, "2+", 5, -2, 1, ["LETHAL HITS"])
dg_close_combat= weaponclass("Close-combat weapon", "Melee", 4, "3+", 4, 0, 1, None)
corrupted_staff = weaponclass("Corrupted staff", "Melee", 4, "3+", 6, -1, 0, ["LETHAL HITS, PSYCHIC"])
cursed_plague_bell =weaponclass("Cursed plague bell", "Melee", 5, "2+", 4, 0, 2, ["ANTI-PSYKER 2+, LETHAL HITS"])
flail_of_corruption =weaponclass("Flail of corruption", "Melee", 6, "2+", 5, -1, 2, ["LETHAL HITS"])
great_plague_blade = weaponclass("Great plague blade", "Melee", 6, "2+", 8, -2, 2, ["DEVASTATING WOUNDS, LETHAL HITS"])
heavy_plague_weapon = weaponclass("Heavy plague weapon", "Melee", 5, "2+", 8, -2, 2, ["LETHAL HITS"])
manreaper_strike =weaponclass("Manreaper — strike", "Melee", 5, "2+", 9, -2, 3, ["LETHAL HITS"])
manreaper_sweep  =weaponclass("Manreaper — sweep", "Melee", 10, "2+", 6, -1, 1, ["LETHAL HITS"])
manreaper = Weapon("Manreaper",[manreaper_sweep,manreaper_strike])
plague_knife=weaponclass("Plague knife", "Melee", 5, "2+", 4, 0, 1, ["LETHAL HITS"])
power_fist =weaponclass("Power fist", "Melee", 5, "2+", 8, -2, 2, ["LETHAL HITS"])

tri_lobe_melee = [
    balesword,
    bubotic_weapons,
    dg_close_combat,
    cursed_plague_bell,
    heavy_plague_weapon,
    plague_knife,
    power_fist
]

dg_terminator_melee = tri_lobe_melee.copy()
dg_terminator_melee.extend([manreaper,flail_of_corruption])

plague_sorcerer_melee = tri_lobe_melee.copy()
plague_sorcerer_melee.append(corrupted_staff)

plague_sorcerer_terminator_melee = plague_sorcerer_melee.copy()
plague_sorcerer_terminator_melee.extend(dg_terminator_melee)

plague_lord_melee = tri_lobe_melee.copy()
plague_lord_melee.append(great_plague_blade)

plague_lord_terminator_melee = plague_lord_melee.copy()
plague_lord_terminator_melee.append(manreaper)