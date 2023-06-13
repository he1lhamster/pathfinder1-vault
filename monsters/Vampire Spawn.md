---
cssclass: [monsters]
title1: Vampire Spawn
desc_short: This pale humanoid has fangs and burning red eyes.
title2: Vampire Spawn
CR: 2
sources:
- name: Monster Codex
  page: 244
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 600
race: Human
classes:
- rogue 2
alignment: NE
size: Medium
type: undead
subtypes:
- human
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 20
  touch: 12
  flat_footed: 18
  components:
    armor: 4
    dex: 2
    natural: 4
HP:
  HP: 18
  long: 2d8+6
  fast_healing: 2
saves:
  fort: 2
  ref: 5
  will: 1
defensive_abilities:
- channel resistance +2
- evasion
DR:
- amount: 5
  weakness: silver
immunities:
- undead traits
resistances:
  cold: 10
  electricity: 10
weaknesses:
- resurrection vulnerability
- vampire weaknesses
speeds:
  base: 30
attacks:
  melee:
  - - text: slam +4 (1d4+4 plus energy drain)
      entries:
      - - damage: 1d4+4
        - effect: energy drain
      attack: slam
      bonus:
      - 4
  ranged:
  - - text: dagger +3 (1d4+3/19-20)
      entries:
      - - damage: 1d4+3
          crit_range: 19-20
      attack: dagger
      bonus:
      - 3
  special:
  - blood drain
  - dominate (DC 13)
  - energy drain (1 level, DC 13)
  - sneak attack +1d6
ability_scores:
  STR: 17
  DEX: 14
  CON:
  INT: 8
  WIS: 12
  CHA: 15
BAB: 1
CMB: 4
CMD: 16
feats:
- name: Improved Initiative
- name: Intimidating Prowess
- name: Power Attack
- is_bonus: true
  name: Skill Focus (Perception)
skills:
  Acrobatics: 13
  Climb: 6
  Intimidate: 10
  Knowledge (local): 4
  Perception: 9
  Sense Motive: 6
  Sleight of Hand: 5
  Stealth: 13
languages:
- Common
- Halfling
special_qualities:
- gaseous form
- rogue talents (strong impression)
- shadowless
- spider climb
- trapfinding +1
ecology:
  environment: any
  organization: gang (2-8) or family (vampire plus 2-8)
  treasure_type: NPC Gear
  treasure:
  - chain shirt
  - dagger
  - other treasure
desc_long: The following template can be used to create unique vampire spawn with
  class levels.

---

# Vampire Spawn
This pale humanoid has fangs and _[[items/Weapon Magic Abilities/Burning|burning]]_ red eyes.
**Source** Monster Codex pg. 244
**XP** 600
Human _[[classes/Rogue|rogue]]_ 2

NE Medium undead (human)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +9

##### Defense

**AC** 20, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +2 Dex, +4 natural)
**hp** 18 (2d8+6); _[[universal monster rules/Fast Healing|fast healing]]_ 2
**Fort** +2, **Ref** +5, **Will** +1
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2, evasion; **DR** 5/silver; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** cold 10, electricity 10
**Weaknesses** _[[spells/Resurrection|resurrection]]_ _[[curses/Vulnerability|vulnerability]]_, _[[monsters/Vampire|vampire]]_ weaknesses

##### Offense
**Speed** 30 ft.
**Melee** slam +4 (1d4+4 plus _[[universal monster rules/Energy Drain|energy drain]]_)
**Ranged** _[[items/Weapon/Dagger|dagger]]_ +3 (1d4+3/19–20)
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_, dominate (DC 13), _energy drain_ (1 level, DC 13), sneak attack +1d6

##### Statistics
**Str** 17, **Dex** 14, **Con** —, **Int** 8, **Wis** 12, **Cha** 15
**Base Atk** +1; **CMB** +4; **CMD** 16
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Acrobatics +13, _[[universal monster rules/Climb|Climb]]_ +6, Intimidate +10, Knowledge (local) +4, Perception +9, Sense Motive +6, Sleight of Hand +5, Stealth +13
**Languages** Common, Halfling
**SQ** _[[spells/Gaseous Form|gaseous form]]_, _rogue_ talents (strong impression), shadowless, _[[spells/Spider Climb|spider climb]]_, trapfinding +1

##### Ecology

**Environment** any
**Organization** gang (2–8) or family (_vampire_ plus 2–8)
**Treasure** NPC Gear (_[[items/Armor/Chain shirt|chain shirt]]_, _dagger_, other treasure)

##### Description

The following template can be used to create unique _[[monsters/Vampire Spawn|vampire spawn]]_ with class levels.