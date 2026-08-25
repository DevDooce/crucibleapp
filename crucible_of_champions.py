# imports
import tkinter as tk
from tkinter import ttk
#import CrucibleList
import Specialisms_and_Abilities
import Weapons
import Archetypes
from Specialisms_and_Abilities import no_specialism

factions = ('Adeptus Astartes',
            #'Dark Angels',
            #'Blood Angels',
            #'Space Wolves',
            'Black Templars',
            #'Adeptus Custodes',
            #'Adepta Sororitas',
            #'Adeptus Mechanicus',
            #'Imperial Agents',
            'Astra Militarum',
            'Grey Knights',
            #'Chaos Space Marines',
            #'World Eaters',
            #'Thousand Sons',
            'Death Guard',
            #'Emperor`s Children',
            #'Chaos Daemons',
            #'Aeldari',
            #'Drukhari',
            #'Leagues of Votann',
            #'Necrons',
            #'Orks',
            'Tau Empire',
            #'Tyranids',
            #'Genestealer Cults'
)


FACTION_TO_ARCH = {
    "Adeptus Astartes": Archetypes.astartes_archetypes,
    #"Dark Angels": CrucibleList.DarkAngels_Arch,
    #"Blood Angels": CrucibleList.BloodAngels_Arch,
    #"Space Wolves": CrucibleList.SpaceWolves_Arch,
    "Black Templars": Archetypes.astartes_archetypes,
    #"Adeptus Custodes": CrucibleList.Custodes_Arch,
    #"Adepta Sororitas": CrucibleList.Sororitas_Arch,
    #"Adeptus Mechanicus": CrucibleList.Mechanicus_Arch,
    #"Imperial Agents": CrucibleList.ImperialAgents_Arch,
    "Astra Militarum": Archetypes.guard_archetypes,
    "Grey Knights": Archetypes.grey_knights_archtype,
    #"Chaos Space Marines": CrucibleList.ChaosSpaceMarines_Arch,
    #"World Eaters": CrucibleList.WorldEaters_Arch,
    #"Thousand Sons": CrucibleList.ThousandSons_Arch,
    "Death Guard": Archetypes.death_guard_archetypes,
    #"Emperors Children": CrucibleList.EmperorsChildren_Arch,
    #"Chaos Daemons": CrucibleList.ChaosDaemons_Arch,
    #"Aeldari": CrucibleList.Aeldari_Arch,
    #"Drukhari": CrucibleList.Drukhari_Arch,
    #"Leagues of Votann": CrucibleList.LeaguesofVotann_Arch,
    #"Necrons": CrucibleList.Necrons_Arch,
    #"Orks": CrucibleList.Orks_Arch,
    "Tau Empire": Archetypes.tau_archetypes,
    #"Tyranids": CrucibleList.Tyranid_Arch,
    #"Genestealer Cults": CrucibleList.GeneStealer_Arch,
}
SPECIALISM_MAP = {
    ("Champion of the Chapter", None): Specialisms_and_Abilities.astartes_specialisms,
    ("Librarius Adept", None): Specialisms_and_Abilities.astartes_specialisms,
    ("Venerable Battle-Brother", None): Specialisms_and_Abilities.dreadie_specialisms,



    ("Front-Line Commander", "Astra Militarum"): Specialisms_and_Abilities.FLC_specialisms,
    ("Augmented Bone'ead", "Astra Militarum"): Specialisms_and_Abilities.augmented_specialism,
    ("Sentinel Commander", "Astra Militarum"): Specialisms_and_Abilities.sentinel_specialisms,

    ("Champion of Titan", "Grey Knights"): Specialisms_and_Abilities.GK_infantry_specialisms,
    ("Venerable Daemon Slayer","Grey Knights" ): Specialisms_and_Abilities.GK_vehicles_specialisms,
    ("Dreadknight Champion", "Grey Knights"): Specialisms_and_Abilities.GK_vehicles_specialisms,

    ("Plague Sorcerer", "Death Guard"): Specialisms_and_Abilities.death_guard_specialisms,
    ("Plague Lord", "Death Guard" ): Specialisms_and_Abilities.death_guard_specialisms,
    ("Tri-Lobe Vectors", "Death Guard"): Specialisms_and_Abilities.death_guard_specialisms,

    ("Shas'nel", "Tau Empire"): Specialisms_and_Abilities.shasnel_specialisms,
    ("Battlesuit Veteran", "Tau Empire"): Specialisms_and_Abilities.battlesuit_specialisms,
    ("Kinband Champion", "Tau Empire"): Specialisms_and_Abilities.kinband_specialisms,

}
Arch_to_pistol = {
    ("Champion of the Chapter",None): Weapons.astartes_pistols,
    ("Librarius Adept",None) : Weapons.astartes_pistols,
    ("Venerable Battle-Brother",None) : Weapons.dreadie_2,

    ("Front-Line Commander",None) : Weapons.guard_pistols,
    ("Champion of Titan", None): Weapons.GK_pistols,

    ("Shas'nel", None): Weapons.shasnel_pistol,
    ("Kinband Champion", None): Weapons.kroot_pistol_list,

    ("Plague Sorcerer",None): Weapons.dg_infantry_pistols,
    ("Plague Sorcerer","Terminator Armour"): Weapons.dg_terminator_pistols,
    ("Plague Lord",None):Weapons.dg_infantry_pistols,
    ("Plague Lord","Terminator Armour"):Weapons.dg_terminator_pistols,
    ("Tri-Lobe Vectors",None):Weapons.dg_infantry_pistols,
    ("Tri-Lobe Vectors","Terminator Armour"):Weapons.dg_terminator_pistols,

}
Arch_to_melee = {

    ("Champion of the Chapter",None): Weapons.astartes_melee,
    ("Librarius Adept",None) : Weapons.astartes_melee,
    ("Venerable Battle-Brother",None) : Weapons.dreadie_3,

    ("Front-Line Commander", None): Weapons.guard_melee_weapons,
    ("Front-Line Commander", "Noble Steed"): Weapons.melee_mounted,
    ("Sentinel Commander", None): Weapons.melee_sentinel,
    ("Augmented Bone'ead", None): Weapons.melee_augmented,

    ("Champion of Titan",None): Weapons.COT_melee,
    ("Venerable Daemon Slayer", None): Weapons.VDS_melee,
    ("Dreadknight Champion",None): Weapons.DKC_melee,

    ("Shas'nel", None): Weapons.shasnel_melee,
    ("Battlesuit Veteran", None): Weapons.shasnel_melee,
    ("Battlesuit Veteran","Broadside Battlesuit"): Weapons.broadside_battlesuit_melee,
    ("Kinband Champion", None): Weapons.kroot_melee,
    ("Kinband Champion", "Kalanmandras"): Weapons.kalamandras_melee,
    ("Kinband Champion", "Krootox"): Weapons.kroot_melee,

    ("Plague Sorcerer",None): Weapons.plague_sorcerer_melee,
    ("Plague Sorcerer","Terminator Armour"): Weapons.dg_terminator_melee,
    ("Plague Lord",None):Weapons.plague_lord_melee,
    ("Plague Lord","Terminator Armour"):Weapons.plague_lord_terminator_melee,
    ("Tri-Lobe Vectors",None):Weapons.tri_lobe_melee,
    ("Tri-Lobe Vectors","Terminator Armour"):Weapons.dg_terminator_melee,
}
Arch_to_primary = {
    ("Champion of the Chapter", None): Weapons.astartes_primary,
    ("Librarius Adept", None) : Weapons.astartes_primary,
    ("Venerable Battle-Brother", None) : Weapons.dreadie_1,

    ("Front-Line Commander", None): Weapons.guard_ranged_weapons,
    ("Front-Line Commander", "Noble Steed"): Weapons.guard_ranged_weapons,
    ("Sentinel Commander", None): Weapons.ranged_sentinel,
    ("Augmented Bone'ead", None): Weapons.ranged_augmented,

    ("Champion of Titan", None): Weapons.COT_ranged,
    ("Venerable Daemon Slayer", None): Weapons.VDS_ranged,
    ("Dreadknight Champion", None): Weapons.DKC_ranged,

    ("Shas'nel", None): Weapons.shasnel_ranged,
    ("Battlesuit Veteran", None): Weapons.battlesuit_veteran_ranged,
    ("Battlesuit Veteran", "Broadside Battlesuit"): Weapons.broadside_battlesuit_ranged,
    ("Kinband Champion", None): Weapons.kroot_ranged,

    ("Plague Sorcerer",None): Weapons.plague_sorcerer_ranged,
    ("Plague Sorcerer","Terminator Armour"): Weapons.dg_terminator_ranged,
    ("Plague Lord",None):Weapons.dg_infantry_ranged,
    ("Plague Lord","Terminator Armour"):Weapons.dg_terminator_ranged,
    ("Tri-Lobe Vectors",None):Weapons.dg_infantry_ranged,
    ("Tri-Lobe Vectors","Terminator Armour"):Weapons.dg_terminator_ranged,
}
Abilities_Map = {
    ("Champion of the Chapter", None): Specialisms_and_Abilities.adeptus_astartes_abilities,
    ("Librarius Adept", None): Specialisms_and_Abilities.adeptus_astartes_abilities,
    ("Venerable Battle-Brother", None): Specialisms_and_Abilities.dreadie_abilities,

    ("Front-Line Commander", "Astra Militarum"): Specialisms_and_Abilities.Guard_abilities,
    ("Augmented Bone'ead", "Astra Militarum"): Specialisms_and_Abilities.Guard_abilities,
    ("Sentinel Commander", "Astra Militarum"): Specialisms_and_Abilities.Guard_abilities,

    ("Champion of Titan", "Grey Knights"): Specialisms_and_Abilities.grey_knights_abilities_infantry,
    ("Venerable Daemon Slayer","Grey Knights" ): Specialisms_and_Abilities.grey_knights_abilities_vehicles,
    ("Dreadknight Champion", "Grey Knights"): Specialisms_and_Abilities.grey_knights_abilities_vehicles,

    ("Plague Sorcerer", "Death Guard"): Specialisms_and_Abilities.death_guard_abilities,
    ("Plague Lord", "Death Guard"): Specialisms_and_Abilities.death_guard_abilities,
    ("Tri-Lobe Vectors", "Death Guard"): Specialisms_and_Abilities.death_guard_abilities,

    ("Shas'nel", "Tau Empire"): Specialisms_and_Abilities.shasnelvet_abilities,
    ("Battlesuit Veteran", "Tau Empire"): Specialisms_and_Abilities.shasnelvet_abilities,
    ("Kinband Champion", "Tau Empire"): Specialisms_and_Abilities.kinband_abilities,

    ("Champion of the Chapter", "Black Templars"): Specialisms_and_Abilities.black_templars_dreadie_abilities,
    ("Librarius Adept", "Black Templars"): Specialisms_and_Abilities.black_templars_dreadie_abilities,
    ("Venerable Battle-Brother", "Black Templars"): Specialisms_and_Abilities.black_templars_dreadie_abilities,
}

# Definitions

def parent_frames(framename,row,col,framerowspan):
    frame = tk.Frame(input_canvas)
    frame.config(highlightbackground="black", highlightthickness=2)
    frame.grid(row=row, column=col, rowspan=framerowspan, sticky="nsew", padx=5, pady=5)
    label = tk.Label(frame, text=framename)
    label.grid(row=0, column=0, sticky="w")
    return frame

def split_dreadie_by_type(weapon_list):
    ranged_profiles = []
    melee_profiles = []

    for weapon in weapon_list:
        profiles = weapon.profiles if hasattr(weapon, "profiles") else [weapon]
        for profile in profiles:
            if profile.range == "Melee":
                melee_profiles.append(profile)
            else:
                ranged_profiles.append(profile)

    return ranged_profiles, melee_profiles

def pick_archetype(event):
    global current_archetype

    faction = factionchosen.get()

    if faction in FACTION_TO_ARCH:
        current_archetype = FACTION_TO_ARCH[faction]

    archetypechosen["values"] = [s.name for s in current_archetype]

    if archetypechosen:
        archetypechosen.current(0)
    pick_abilities(event)
    pick_specialism(event)
    refresh_weapons()

def get_archetype():
    index = archetypechosen.current()

    if index >= 0 and index < len(current_archetype):
        return current_archetype[index]

    return None

def toggle_weapon_selection_style():
    archetype = get_archetype()
    if archetype.name == "Venerable Battle-Brother":
        primary_container.grid_remove()
        pistols_container.grid_remove()
        melee_container.grid_remove()
        dreadie_frame_1.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
        dreadie_frame_2.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky="ew")  # or grid_remove(), per its own dependency check
        dreadie_frame_3.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
        dreadie_frame_4.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky="ew")  # or grid_remove(), per its own dependency check
    else:
        primary_container.grid()
        pistols_container.grid()
        melee_container.grid()
        dreadie_frame_1.grid_remove()
        dreadie_frame_2.grid_remove()
        dreadie_frame_3.grid_remove()
        dreadie_frame_4.grid_remove()

def pick_specialism(event):
    global current_specialisms

    archetype = archetypechosen.get()
    faction = factionchosen.get()

    key = (archetype, faction)

    if key in SPECIALISM_MAP:
        current_specialisms = list(SPECIALISM_MAP[key])
    else:
        current_specialisms = list(SPECIALISM_MAP.get((archetype, None), []))

    current_specialisms.insert(0, no_specialism)

    specialismchosen["values"] = [s.name for s in current_specialisms]

    if current_specialisms:
        specialismchosen.current(0)

def get_specialisms():
    index = specialismchosen.current()

    if index >= 0 and index < len(current_specialisms):
        return current_specialisms[index]

    return None

def pick_abilities(event):
    global current_ability

    archetype = archetypechosen.get()
    faction = factionchosen.get()

    key = (archetype, faction)

    if key in Abilities_Map:
        current_ability  = Abilities_Map[key]
    else:
        current_ability = Abilities_Map.get((archetype, None), [])

    abilitychosen["values"] = [s.name for s in current_ability]

    if current_ability:
        abilitychosen.current(0)
    refresh_weapons()

def get_abilities():
    index = abilitychosen.current()

    if index >= 0 and index < len(current_ability):
        return current_ability[index]

    return None

def toggle_ability_selection_style():
    archetype = get_archetype()
    if archetype.name == "Tri-Lobe Vectors":
        abilitychosen.grid_remove()
        tlv_ability_frame.grid()
    else:
        abilitychosen.grid()
        tlv_ability_frame.grid_remove()

def fill_tlv_ability_choices():
    # current_ability already holds the correct pool for this archetype,
    # set up by pick_abilities() using the same Abilities_Map lookup.
    names = [" "] + [a.name for a in current_ability]

    tlv_ability_1_chosen["values"] = names
    tlv_ability_2_chosen["values"] = names
    tlv_ability_3_chosen["values"] = names

    if not tlv_ability_1_var.get():
        tlv_ability_1_chosen.current(0)
    if not tlv_ability_2_var.get():
        tlv_ability_2_chosen.current(0)
    if not tlv_ability_3_var.get():
        tlv_ability_3_chosen.current(0)

def update_ability_exclusions(*args):
    all_names = [" "] + [a.name for a in current_ability]

    chosen_1 = tlv_ability_1_var.get()
    chosen_2 = tlv_ability_2_var.get()
    chosen_3 = tlv_ability_3_var.get()

    # Each box offers every name except whatever the OTHER two have already taken,
    # but always keeps its own current selection available to itself.
    tlv_ability_1_chosen["values"] = [n for n in all_names if n == " " or n == chosen_1 or (n != chosen_2 and n != chosen_3)]
    tlv_ability_2_chosen["values"] = [n for n in all_names if n == " " or n == chosen_2 or (n != chosen_1 and n != chosen_3)]
    tlv_ability_3_chosen["values"] = [n for n in all_names if n == " " or n == chosen_3 or (n != chosen_1 and n != chosen_2)]

def _get_tlv_ability(name):
    for a in current_ability:
        if a.name == name:
            return a
    return None

def get_tlv_ability_1():
    return _get_tlv_ability(tlv_ability_1_var.get())

def get_tlv_ability_2():
    return _get_tlv_ability(tlv_ability_2_var.get())

def get_tlv_ability_3():
    return _get_tlv_ability(tlv_ability_3_var.get())

def weapon_table(list_name,frame_name,row):
    for weapon in list_name:
        profiles = weapon.profiles if hasattr(weapon, "profiles") else [weapon]

        for profile in profiles:
            tk.Label(frame_name, text=profile.name).grid(row=row, column=0)
            tk.Label(frame_name, text=profile.range).grid(row=row, column=1)
            tk.Label(frame_name, text=profile.attacks).grid(row=row, column=2)
            tk.Label(frame_name, text=profile.skill).grid(row=row, column=3)
            tk.Label(frame_name, text=profile.strength).grid(row=row, column=4)
            tk.Label(frame_name, text=profile.AP).grid(row=row, column=5)
            tk.Label(frame_name, text=profile.Damage).grid(row=row, column=6)
            traits = ", ".join(profile.Traits) if profile.Traits else ""
            tk.Label(frame_name, text=traits).grid(row=row, column=7)
            row += 1

    return row

def resolve_stat(archetype_value,specialism_value):

    if specialism_value is None:

        final_stats = archetype_value

    else:
        final_stats = specialism_value

    return final_stats

def final_leader():
    archetype = get_archetype()
    specialism = get_specialisms()

    if specialism is None:
        final_leader = archetype.leader

    else:
        final_leader = resolve_stat(archetype.leader,specialism.leader)

    return final_leader

def get_extra_weapon_points():

    primary_list, pistols_list, melee_list = get_selected_weapons()
    archetype = get_archetype()

    if archetype.name == "Venerable Battle-Brother":

        dreadie_weapons = get_selected_dreadie_weapons()
        extra_weapons = 0
        for weapon in dreadie_weapons:
            if weapon.points is not None:
                extra_weapons += weapon.points
        return extra_weapons

    else:
        total_weapons = len(primary_list) + len(pistols_list) + len(melee_list)

        free_weapons = 2 * archetype.model_count
        extra_weapons = max(0, total_weapons - free_weapons)
        return extra_weapons * 5


def total_points():
    archetype = get_archetype()
    specialism = get_specialisms()

    if archetype.name == "Tri-Lobe Vectors":
        ability_1 = get_tlv_ability_1()
        ability_2 = get_tlv_ability_2()
        ability_3 = get_tlv_ability_3()

        ability_points = sum(
            ability.abilpoint
            for ability in (ability_1, ability_2, ability_3)
            if ability is not None
        )
    else:
        ability = get_abilities()
        ability_points = ability.abilpoint if ability is not None else 0

    total_points = (
            archetype.archpoints
            + ability_points
            + specialism.spepoint
            + get_extra_weapon_points()
    )

    return total_points

def make_final_stats():
    archetype = get_archetype()
    specialism = get_specialisms()

    if specialism is None:
        final_m = archetype.m
        final_t = archetype.t
        final_sv = archetype.sv
        final_ivl = archetype.ivl
        final_w = archetype.w


    else:
        final_m = resolve_stat(archetype.m,specialism.m)
        final_t = resolve_stat(archetype.t,specialism.t)
        final_sv = resolve_stat(archetype.sv,specialism.sv)
        final_ivl = resolve_stat(archetype.ivl,specialism.inv_sv)
        final_w = resolve_stat(archetype.w,specialism.w)

    stat_line ={"m": final_m,
     "t": final_t,
     "sv": final_sv,
     "ivl": final_ivl,
     "w": final_w}

    return stat_line

def open_character_sheet_window():
    archetype = get_archetype()

    if archetype.name == "Venerable Battle-Brother":
        dreadie_weapons = get_selected_dreadie_weapons()
        primary_list, melee_list = split_dreadie_by_type(dreadie_weapons)
        pistols_list = []

    else:
        primary_list, pistols_list, melee_list = get_selected_weapons()

    root = tk.Toplevel()
    for i in range(10):
        root.grid_rowconfigure(i, weight=1)

    root.grid_columnconfigure(0, weight=3)  # Left
    root.grid_columnconfigure(1, weight=1)  # Right
    root.title("Character sheet")
    root.geometry("1200x1100")

    def generic_frame(framename, row, col,Rowspan):
        frame = tk.Frame(root)
        frame.config(highlightbackground="black", highlightthickness=2)
        frame.grid(row=row, column=col, rowspan=Rowspan, sticky="nsew", padx=5, pady=5)
        label = tk.Label(frame, text=framename)
        label.grid(row=0, column=0, sticky="w")
        return frame

    def stats_row():
        frame = tk.Frame(root)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        frame.config(highlightbackground="black", highlightthickness=2)
        textbox = tk.Entry(frame, width=40)
        textbox.grid(row=0, column=0, sticky="w")
        character_stats = ["M", "T", "SV", "INV", "W", "LD", "OC","PTS"]
        for i in range(8):
            stat = character_stats[i]
            label = tk.Label(frame, text=stat)
            label.grid(padx= 20, row=0, column=i + 1)

        archetype =  get_archetype()
        stats = make_final_stats()
        points = total_points()

        tk.Label(frame, text=f'{stats["m"]}"').grid(row=1, column=1)
        tk.Label(frame, text=f'{stats["t"]}').grid(row=1, column=2)
        tk.Label(frame, text=f'{stats["sv"]}+').grid(row=1, column=3)
        tk.Label(frame, text=f'{stats["ivl"]}+').grid(row=1, column=4)
        tk.Label(frame, text=f'{stats["w"]}').grid(row=1, column=5)
        tk.Label(frame, text=archetype.ld).grid(row=1, column=6)
        tk.Label(frame, text=archetype.oc).grid(row=1, column=7)
        tk.Label(frame, text=points).grid(row=1, column=8)

        return frame

    Character_Row = stats_row()

    ranged_frame = tk.Frame(root)
    ranged_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    ranged_frame.config(highlightbackground="black", highlightthickness=2)

    #Ranged frame
    stats = ["RNG", "A", "BS", "S", "AP", "D","Traits"]
    for i in range(len(stats)):
        stat = stats[i]
        label = tk.Label(ranged_frame, text=stat)
        label.grid(padx=20, row=0, column=i + 1)

    label = tk.Label(ranged_frame, text="Ranged Weapons".title(), bg="red")
    label.grid(row=0, column=0, sticky="w")

    row = weapon_table(primary_list,ranged_frame,1)

    weapon_table(pistols_list,ranged_frame,row)

    #Melee frame
    melee_frame = tk.Frame(root)
    melee_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
    melee_frame.config(highlightbackground="black", highlightthickness=2)

    stats = ["RNG", "A", "WS", "S", "AP", "D","Traits"]
    for i in range(len(stats)):
        stat = stats[i]
        label = tk.Label(melee_frame, text=stat)
        label.grid(padx=20, row=0, column=i + 1)

    label = tk.Label(melee_frame, text="Melee Weapons".title(), bg="red")
    label.grid(row=0, column=0, sticky="w")

    weapon_table(melee_list,melee_frame,1)

    Leader_Frame = generic_frame("Leader", 3, 0,1)

    leader = final_leader()
    label = tk.Label(Leader_Frame, text=leader)
    label.grid(row=1, column=0, sticky="w", rowspan=3)

    Unit_Frame = generic_frame("Unit Composition", 4, 0,1)
    archetype = get_archetype()
    compositionlabel = tk.Label(Unit_Frame, text=archetype.composition)
    compositionlabel.grid(row=2, column=0, sticky="w")

    Ability_Frame = generic_frame("Ability", 0, 1,2)
    archetype = get_archetype()

    if archetype.name == "Tri-Lobe Vectors":
        tlv_abilities = [get_tlv_ability_1(), get_tlv_ability_2(), get_tlv_ability_3()]

        row = 1
        for i, ability in enumerate(tlv_abilities, start=1):
            model_label = tk.Label(Ability_Frame, text=f"Model {i}:")
            model_label.grid(row=row, column=0, sticky="w")
            row += 1

            if ability is None:
                label = tk.Label(Ability_Frame, text="No ability selected", wraplength=400, justify="left", anchor="nw")
                label.grid(row=row, column=0, sticky="w")
                row += 1
            else:
                label = tk.Label(Ability_Frame, text=ability.name)
                label.grid(row=row, column=0, sticky="w")
                row += 1
                label = tk.Label(Ability_Frame, text=ability.description, wraplength=400, justify="left", anchor="nw")
                label.grid(row=row, column=0, sticky="w")
                row += 1

        label = tk.Label(Ability_Frame, text=archetype.ability, wraplength=400, justify="left", anchor="nw")
        label.grid(row=row, column=0, sticky="w")
    else:
        ability = get_abilities()
        label  = tk.Label(Ability_Frame, text=ability.name)
        label.grid(row=1, column=0, sticky="w")
        label = tk.Label(Ability_Frame, text=ability.description,wraplength=400,justify="left",anchor="nw")
        label.grid(row=2, column=0, sticky="w")
        label = tk.Label(Ability_Frame, text=archetype.ability,wraplength=400,justify="left",anchor="nw")
        label.grid(row=3, column=0, sticky="w")

    Specialism_Frame = generic_frame("Specialism", 2, 1,1)
    specialism = get_specialisms()
    label = tk.Label(Specialism_Frame, text = specialism.name)
    label.grid(row=1, column=0, sticky="w")
    label = tk.Label(Specialism_Frame, text = specialism.description,wraplength=400,justify="left",anchor="nw")
    label.grid(row=2, column=0, sticky="w")

    Keyword_Frame = generic_frame("Keywords", 3, 1,1)
    archetype = get_archetype()
    keywords = list(archetype.keywords)
    grab_specialism = get_specialisms()
    remove_keywords = grab_specialism.remove_keywords

    for kw in remove_keywords:
        if kw in keywords:
            keywords.remove(kw)

    add_keywords = grab_specialism.add_keywords

    keywords.extend(add_keywords)
    label = tk.Label(Keyword_Frame, text=keywords)
    label.grid(row=1, column=0, sticky="w",rowspan=3)

    FactionKeyword_Frame = generic_frame("Faction Keywords", 4, 1,1)
    label = tk.Label(FactionKeyword_Frame, text=factionchosen.get())
    label.grid(row=1, column=0, sticky="w")
    root.mainloop()

# create window
parent = tk.Tk()
parent.title("Crucible of champions")
parent.geometry("600x600")

# Configure grid weights for proper resizing
parent.grid_rowconfigure(0, weight=1)
parent.grid_columnconfigure(0, weight=1)

# Canvas
input_canvas = tk.Canvas(parent, width=600, height=600)
input_canvas.grid(row=0, column=0, sticky="nsew")

# Scrollbar
input_scrollbar = ttk.Scrollbar(parent, orient="vertical", command=input_canvas.yview)
input_scrollbar.grid(row=0, column=1, sticky="ns")

# Configure canvas scrolling
input_canvas.config(yscrollcommand=input_scrollbar.set)

# Create a frame inside the canvas for all content
main_frame = tk.Frame(input_canvas)
canvas_window = input_canvas.create_window((0, 0), window=main_frame, anchor="nw")

# Update scroll region when frame changes size
def configure_scroll_region(event):
    input_canvas.config(scrollregion=input_canvas.bbox("all"))

main_frame.bind("<Configure>", configure_scroll_region)

# Also update canvas window width when canvas resizes
def configure_canvas_width(event):
    input_canvas.itemconfig(canvas_window, width=event.width)

input_canvas.bind("<Configure>", configure_canvas_width)

# FIX 2: Add mouse wheel scrolling
def on_mousewheel(event):
    input_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def on_mousewheel_linux(event):
    input_canvas.yview_scroll(-1 * event.num, "units")

# Bind mousewheel events for different platforms
input_canvas.bind("<MouseWheel>", on_mousewheel)  # Windows/Mac
input_canvas.bind("<Button-4>", on_mousewheel_linux)  # Linux scroll up
input_canvas.bind("<Button-5>", on_mousewheel_linux)  # Linux scroll down

# Make sure the canvas gets focus for scrolling
input_canvas.bind("<Enter>", lambda e: input_canvas.focus_set())
input_canvas.bind("<Leave>", lambda e: input_canvas.focus_set())

# Title of window
title_label = ttk.Label(main_frame, text="Crucible of champions",
                        background="white", foreground="black",
                        font=("Arial", 12))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Faction selection (row 1)
ttk.Label(main_frame, text="Choose Faction:",
          font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")

n = tk.StringVar()
factionchosen = ttk.Combobox(main_frame, values=factions, width=40, textvariable=n)
factionchosen.grid(row=1, column=1, padx=10, pady=5, sticky="w")
factionchosen.current(0)
factionchosen.bind("<<ComboboxSelected>>", pick_archetype)

# Archetype selection (row 2)
ttk.Label(main_frame, text="Choose Archetype:",
          font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")

m = tk.StringVar()
archetypechosen = ttk.Combobox(main_frame, values=[" "], width=40, textvariable=m)
archetypechosen.grid(row=2, column=1, padx=10, pady=5, sticky="w")
archetypechosen.current(0)

# Specialism selection (row 3)
ttk.Label(main_frame, text="Choose Specialism:",
          font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")

o = tk.StringVar()
specialismchosen = ttk.Combobox(main_frame, values=[" "], width=40, textvariable=o)
specialismchosen.grid(row=3, column=1, padx=10, pady=5, sticky="w")
specialismchosen.current(0)

#Ability selection (row 4)
ttk.Label(main_frame, text="Choose Ability",
          font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="e")

p = tk.StringVar()
abilitychosen = ttk.Combobox(main_frame, values=[" "], width=40, textvariable=p)
abilitychosen.grid(row=4, column=1, padx=10, pady=5, sticky="w")
abilitychosen.current(0)

# Tri-lobe Vectors: three independent ability pickers, one per model.
# Hidden by default; only shown for Tri-lobe Vectors via toggle_ability_selection_style().
# Wrapped in their own frame so they don't depend on main_frame's columns 2/3,
# which were never configured with a width (only columns 0 and 1 were).
tlv_ability_frame = tk.Frame(main_frame)
tlv_ability_frame.grid(row=4, column=1, padx=10, pady=5, sticky="w")

tlv_ability_1_var = tk.StringVar()
tlv_ability_1_chosen = ttk.Combobox(tlv_ability_frame, values=[" "], width=20, textvariable=tlv_ability_1_var)
tlv_ability_1_chosen.grid(row=0, column=0, padx=2)

tlv_ability_2_var = tk.StringVar()
tlv_ability_2_chosen = ttk.Combobox(tlv_ability_frame, values=[" "], width=20, textvariable=tlv_ability_2_var)
tlv_ability_2_chosen.grid(row=0, column=1, padx=2)

tlv_ability_3_var = tk.StringVar()
tlv_ability_3_chosen = ttk.Combobox(tlv_ability_frame, values=[" "], width=20, textvariable=tlv_ability_3_var)
tlv_ability_3_chosen.grid(row=0, column=2, padx=2)

tlv_ability_frame.grid_remove()

tlv_ability_1_var.trace_add("write", update_ability_exclusions)
tlv_ability_2_var.trace_add("write", update_ability_exclusions)
tlv_ability_3_var.trace_add("write", update_ability_exclusions)


#Weapons selection

primary_container = tk.LabelFrame(main_frame,text = "Ranged", padx=10, pady=10)
primary_container.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

dreadie_frame_1 = tk.LabelFrame(main_frame,text = "Option 1", padx=10, pady=10)

def get_selected_weapons():
    primary_list = []
    for weapon, var in primary_check_vars:
        count = var.get()
        for i in range(count):
            primary_list.append(weapon)

    pistols_list = []
    for weapon, var in pistol_check_vars:
        count = var.get()
        for i in range(count):
            pistols_list.append(weapon)

    melee_list = []
    for weapon, var in melee_check_vars:
        count = var.get()
        for i in range(count):
            melee_list.append(weapon)

    return primary_list, pistols_list, melee_list

def get_selected_dreadie_weapons():
    dreadie_weapons = []

    choice_1 = get_dreadie_choice_1()
    if choice_1 is not None:
        dreadie_weapons.append(choice_1)

    choice_2 = get_dreadie_choice_2()
    if choice_2 is not None:
        dreadie_weapons.append(choice_2)

    choice_3 = get_dreadie_choice_3()
    if choice_3 is not None:
        dreadie_weapons.append(choice_3)

    if dreadie_choice_4.get():
        dreadie_weapons.append(Weapons.dreadie_4[0])

    return dreadie_weapons

max_rows = 4

primary_check_vars = []

dreadie_vars_1 = []
def fill_dreadie_frame_1():
    global dreadie_choice_1
    dreadie_vars_1.clear()

    for widget in dreadie_frame_1.winfo_children():
        widget.destroy()

    archetype = get_archetype()

    if archetype.name == "Venerable Battle-Brother":
        option_1_list = Weapons.dreadie_1

    else:
        option_1_list = []

    max_rows = 4

    dreadie_choice_1 = tk.IntVar(value=0)

    dreadie_choice_1.trace_add("write", update_group_2_visibility)

    for i, weapon in enumerate(option_1_list):

        row = i % max_rows
        col = i // max_rows

        dreadie_vars_1.append(weapon)

        radiobutton = tk.Radiobutton(
            dreadie_frame_1,
            variable=dreadie_choice_1,
            value=i,
            text=weapon.name
        )
        radiobutton.grid(row=row,column=col, sticky="w", pady=2)

dreadie_vars_2 = []

def fill_dreadie_frame_2():
    global dreadie_choice_2
    dreadie_vars_2.clear()

    for widget in dreadie_frame_2.winfo_children():
        widget.destroy()

    option_2_list = Weapons.dreadie_2
    dreadie_choice_2 = tk.IntVar(value=0)

    for i, weapon in enumerate(option_2_list):
        row = i % max_rows
        col = i // max_rows

        dreadie_vars_2.append(weapon)

        label = tk.Label(dreadie_frame_2, text=weapon.name)
        label.grid(row=i, column=0, sticky="w", padx=(10, 2), pady=2)

        radiobutton = tk.Radiobutton(
            dreadie_frame_2,
            variable=dreadie_choice_2,
            value=i,
            text=weapon.name
        )
        radiobutton.grid(row=i, column=col, sticky="w", pady=2)


dreadie_vars_3 = []

def fill_dreadie_frame_3():
    global dreadie_choice_3
    dreadie_vars_3.clear()

    for widget in dreadie_frame_3.winfo_children():
        widget.destroy()

    option_3_list = Weapons.dreadie_3
    dreadie_choice_3 = tk.IntVar(value=0)
    dreadie_choice_3.trace_add("write", update_group_4_visibility)

    for i, weapon in enumerate(option_3_list):
        row = i % max_rows
        col = i // max_rows

        dreadie_vars_3.append(weapon)

        label = tk.Label(dreadie_frame_3, text=weapon.name)
        label.grid(row=i, column=0, sticky="w", padx=(10, 2), pady=2)

        radiobutton = tk.Radiobutton(
            dreadie_frame_3,
            variable=dreadie_choice_3,
            value=i,
            text=weapon.name
        )
        radiobutton.grid(row=i, column=col, sticky="w", pady=2)

def fill_primary_container(event=None):
    primary_check_vars.clear()
    # Clear existing widgets from pistols_container YOU NEED THIS TO REFRESH THE FRAME
    for widget in primary_container.winfo_children():
        widget.destroy()

    archetype = get_archetype()
    specialism = get_specialisms()
    key = (archetype.name, specialism.name)

    if key in Arch_to_primary:
        primary_list = Arch_to_primary[key]
    else:
        primary_list = Arch_to_primary.get((archetype.name, None), [])

    pri_max_rows = 4

    for i, weapon in enumerate(primary_list):
        row = i % pri_max_rows
        col = i // pri_max_rows

        var = tk.IntVar(value=0)
        primary_check_vars.append((weapon, var))

        label = tk.Label(primary_container, text=weapon.name)
        label.grid(row=row, column=col * 2, sticky="w", padx=(10, 2), pady=2)

        spinbox_limit = archetype.primary_limit * archetype.model_count

        spinbox = tk.Spinbox(
            primary_container,
            from_=0,
            to=spinbox_limit,
            textvariable=var,
            width=3
        )
        spinbox.grid(row=row, column=col * 2 + 1, sticky="w", pady=2)

dreadie_choice_4 = tk.BooleanVar(value=False)

def fill_dreadie_frame_4():
    for widget in dreadie_frame_4.winfo_children():
        widget.destroy()

    weapon = Weapons.dreadie_4[0]

    checkbutton = tk.Checkbutton(
        dreadie_frame_4,
        variable=dreadie_choice_4,
        text=weapon.name
    )
    checkbutton.grid(row=0, column=0, sticky="w", padx=(10, 2), pady=2)

def get_dreadie_choice_1():
    index = dreadie_choice_1.get()
    if 0 <= index < len(dreadie_vars_1):
        return dreadie_vars_1[index]
    return None

def get_dreadie_choice_2():
    index = dreadie_choice_2.get()
    if 0 <= index < len(dreadie_vars_2):
        return dreadie_vars_2[index]
    return None

def get_dreadie_choice_3():
    index = dreadie_choice_3.get()
    if 0 <= index < len(dreadie_vars_3):
        return dreadie_vars_3[index]
    return None

def update_group_2_visibility(*args):
    choice = get_dreadie_choice_1()
    if choice is not None and choice.name in (Weapons.brutalis_bolt_rifles_fists.name, Weapons.brutalis_talons.name):
        dreadie_frame_2.grid_remove()
    else:
        dreadie_frame_2.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

def update_group_4_visibility(*args):
    choice = get_dreadie_choice_3()
    if choice is not None and choice.name in (Weapons.twin_bolter_icarus.name, Weapons.twin_multi_melta_icarus.name):
        dreadie_frame_4.grid_remove()
    else:
        dreadie_frame_4.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

# Store checkbox variables if you need to access them later
pistol_check_vars = []

# pistols tick boxes
pistols_container = tk.LabelFrame(main_frame,text = "Pistols", padx=10, pady=10)
pistols_container.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

dreadie_frame_2 = tk.LabelFrame(main_frame,text = "Option 2  (all +10 pts)", padx=10, pady=10)

def fill_pistols_container(event=None):
    pistol_check_vars.clear()
    # Clear existing widgets from pistols_container YOU NEED THIS TOO REFRESH THE FRAME
    for widget in pistols_container.winfo_children():
        widget.destroy()

    archetype = get_archetype()
    specialism = get_specialisms()
    key = (archetype.name, specialism.name)

    if key in Arch_to_pistol:
        pistols_list = Arch_to_pistol[key]
    else:
        pistols_list = Arch_to_pistol.get((archetype.name, None), [])

    max_rows = 4

    for i, weapon in enumerate(pistols_list):
        row = i % max_rows
        col = i // max_rows

        var = tk.IntVar(value=0)
        pistol_check_vars.append((weapon, var))

        label = tk.Label(pistols_container, text=weapon.name)
        label.grid(row=row, column=col * 2, sticky="w", padx=(10, 2), pady=2)

        spinbox = tk.Spinbox(
            pistols_container,
            from_=0,
            to=archetype.pistol_limit,
            textvariable=var,
            width=3
        )
        spinbox.grid(row=row, column=col * 2 + 1, sticky="w", pady=2)

#melee weapons tick box
melee_container = tk.LabelFrame(main_frame,text = "Melee", padx=10, pady=10)
melee_container.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

melee_check_vars = []

dreadie_frame_3 = tk.LabelFrame(main_frame,text = "Option 3", padx=10, pady=10)

def fill_melee_container(event=None):
    melee_check_vars.clear()

    for widget in melee_container.winfo_children():
        widget.destroy()

    archetype = get_archetype()
    specialism = get_specialisms()
    key = (archetype.name, specialism.name)

    if key in Arch_to_melee:
        melee_list = Arch_to_melee[key]
    else:
        melee_list = Arch_to_melee.get((archetype.name, None), [])

    max_rows = 4

    for i, weapon in enumerate(melee_list):
        row = i % max_rows
        col = i // max_rows

        var = tk.IntVar(value=0)
        melee_check_vars.append((weapon, var))

        label = tk.Label(melee_container, text=weapon.name)
        label.grid(row=row, column=col * 2, sticky="w", padx=(10, 2), pady=2)

        spinbox = tk.Spinbox(
            melee_container,
            from_=0,
            to=archetype.melee_limit,
            textvariable=var,
            width=3
        )
        spinbox.grid(row=row, column=col * 2 + 1, sticky="w", pady=2)

dreadie_frame_4 = tk.LabelFrame(main_frame,text = "Option 4 (If no ironhail)", padx=10, pady=10)

def combined_handler(event):
    pick_specialism(event)
    refresh_weapons(event)
    pick_abilities(event)

def refresh_weapons(event=None):
    toggle_weapon_selection_style()
    toggle_ability_selection_style()
    fill_tlv_ability_choices()
    fill_dreadie_frame_1()
    fill_dreadie_frame_2()
    fill_dreadie_frame_3()
    fill_dreadie_frame_4()
    fill_primary_container(event)
    fill_pistols_container(event)
    fill_melee_container(event)

#bind archetype to pistol
archetypechosen.bind("<<ComboboxSelected>>", combined_handler)
specialismchosen.bind("<<ComboboxSelected>>", lambda event: refresh_weapons(event))

# Button (row 5) - positioned after checkboxes
ttk.Button(main_frame, text="Make character sheet",
           command=open_character_sheet_window,
           style="Accent.TButton").grid(row=9, column=0, columnspan=2, pady=20)

# Configure column weights for main_frame to allow proper stretching
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=2)

#Styling the program


# Configure styles for better appearance
style = ttk.Style()
style.theme_use('clam')

# Color scheme
canvas_bg = "#FFFFFF"  # White canvas
frame_bg = "#F0F0F0"  # Light gray for frames
border_color = "#CC0000"  # Red borders
accent_color = "#CC0000"  # Red accents
fg_color = "#333333"  # Dark text

# Configure main window and canvas
parent.config(bg=frame_bg)
input_canvas.config(bg=canvas_bg)
main_frame.config(bg=canvas_bg)

# Style for labels
style.configure("TLabel", background=canvas_bg, foreground=fg_color, font=("Segoe UI", 10))

# Style for label frames with red borders
style.configure("TLabelframe", background=frame_bg, foreground=accent_color,
               font=("Segoe UI", 10, "bold"), bordercolor=border_color, relief="solid", borderwidth=2)
style.configure("TLabelframe.Label", background=frame_bg, foreground=accent_color, font=("Segoe UI", 10, "bold"))

# Style for buttons
style.configure("TButton", background=accent_color, foreground=canvas_bg,
               font=("Segoe UI", 10, "bold"), padding=6, borderwidth=0)
style.map("TButton", background=[("active", "#DD2222"), ("pressed", "#990000")])

style.configure("Accent.TButton", background=accent_color, foreground=canvas_bg,
               font=("Segoe UI", 12, "bold"), padding=10)
style.map("Accent.TButton", background=[("active", "#DD2222"), ("pressed", "#990000")])

# Style for comboboxes
style.configure("TCombobox", fieldbackground=canvas_bg, background=frame_bg,
               foreground=fg_color, arrowcolor=accent_color, borderwidth=1)

# Title styling
title_label.configure(background=canvas_bg, foreground=accent_color, font=("Segoe UI", 16, "bold"))

# Style all labels
for child in main_frame.winfo_children():
    if isinstance(child, ttk.Label) or (isinstance(child, tk.Label) and child != title_label):
        try:
            child.configure(background=canvas_bg, foreground=fg_color)
        except:
            pass

# Style containers with patterns
primary_container.configure(bg=frame_bg, fg=accent_color, relief="solid", borderwidth=1)
pistols_container.configure(bg=frame_bg, fg=accent_color, relief="solid", borderwidth=1)
melee_container.configure(bg=frame_bg, fg=accent_color, relief="solid", borderwidth=1)

# Add subtle pattern to weapon containers (FIXED lower() issue)
def add_pattern_to_frames():
    for container in [primary_container, pistols_container, melee_container]:
        # Add subtle diagonal lines using canvas
        pattern = tk.Canvas(container, highlightthickness=0, bg=frame_bg)
        pattern.place(x=0, y=0, relwidth=1, relheight=1)
        pattern.lower("all")  # Fixed: lower with argument
        for i in range(-200, 500, 25):
            pattern.create_line(i, 0, i + 150, 150, fill="#E5E5E5", width=1)
            pattern.create_line(i - 150, 150, i, 300, fill="#E5E5E5", width=1)

# Style checkbuttons
def style_checkbuttons():
    for container in [primary_container, pistols_container, melee_container]:
        for child in container.winfo_children():
            if isinstance(child, tk.Checkbutton):
                child.configure(
                    bg=frame_bg,
                    fg=fg_color,
                    selectcolor=frame_bg,
                    activebackground=frame_bg,
                    activeforeground=accent_color,
                    font=("Segoe UI", 9)
                )

# Apply styling
add_pattern_to_frames()
style_checkbuttons()

parent.mainloop()