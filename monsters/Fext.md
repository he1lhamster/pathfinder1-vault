---
cssclass: [monsters]
title1: Fext
desc_short: This creature's pallid skin and dead, vacant eyes belie its healthy, powerful
  physique. It is clad in fearsome armor.
title2: Fext
CR: 10
sources:
- name: Bestiary 5
  page: 115
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: 'Pathfinder #71: Rasputin Must Die!'
  page: 88
  link: http://paizo.com/products/btpy8yv5?Pathfinder-Adventure-Path-71-Rasputin-Must-Die
XP: 9600
alignment: LE
size: Medium
type: undead
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 25
  touch: 12
  flat_footed: 23
  components:
    armor: 9
    dex: 1
    dodge: 1
    natural: 2
    shield: 2
HP:
  HP: 127
  long: 15d8+60
saves:
  fort: 9
  ref: 9
  will: 11
DR:
- amount: 10
  weakness: glass or obsidian
immunities:
- cold
- undead traits
resistances:
  electricity: 10
  fire: 10
SR: 21
speeds:
  base: 40
  base_other: 30 ft. in armor
attacks:
  melee:
  - - text: +1 bastard sword +20/+15/+10 (1d10+8/17-20)
      entries:
      - - damage: 1d10+8
          crit_range: 17-20
      attack: +1 bastard sword
      bonus:
      - 20
      - 15
      - 10
  - - text: slam +18 (1d4+10 plus energy drain)
      entries:
      - - damage: 1d4+10
        - effect: energy drain
      attack: slam
      bonus:
      - 18
  special:
  - energy drain (1d4 levels, DC 21)
spell_like_abilities:
  entries:
  - name: death knell
    source: default
    freq: At will
    DC: 16
  - name: protection from good
    source: default
    freq: At will
  - name: speak with dead
    source: default
    freq: At will
    DC: 17
  - name: bestow curse
    source: default
    freq: 3/day
    DC: 17
  sources:
  - name: default
    CL: 15
    concentration: 19
ability_scores:
  STR: 25
  DEX: 18
  CON:
  INT: 13
  WIS: 15
  CHA: 18
BAB: 11
CMB: 18
CMD: 33
feats:
- name: Cleave
- name: Dodge
- name: Great Cleave
- name: Improved Critical (bastard sword)
- name: Mobility
- name: Power Attack
- name: Spring Attack
- name: Weapon Focus (bastard sword)
skills:
  Acrobatics: 4
  Disguise: 15
  Intimidate: 20
  Knowledge (engineering): 12
  Knowledge (religion): 12
  Perception: 20
  Sense Motive: 9
  Stealth: 11
languages:
- Common
- Infernal
special_qualities:
- unkillable
ecology:
  environment: any
  organization: solitary
  treasure_type: standard
  treasure:
  - +1 bastard sword
  - full plate
  - heavy steel shield
  - other gear
special_abilities:
  Unkillable (Su): When reduced to 0 hit points by anything other than a glass weapon
    or an obsidian weapon, a fext is not destroyed,but instead becomes unconscious.
    Additionally, 1d4 minutes after falling unconscious, a fext gains fast healing
    1. To be completely destroyed, a fext must be reduced to 0 hit points by a glass
    or obsidian weapon, or once it is rendered unconscious, its head must be severed
    and anointed with holy water. Once destroyed, a fext dissolves into fine ash.
desc_long: |-
  Any good general forbids mention of fexts among his ranks, but such strictures do little to prevent soldiers from whispering tales of undying officers leading enemy units.

   These supernatural officers almost never seem to fall in battle, and when they do, they return for the next clash unfazed. Soldiers whisper that these deathless commanders are vulnerable only to glass weapons. Stories of fexts, usually dismissed as camp folktales derived from soldiers' frustration at failed campaigns and lost battles, are most frighteningly true-a truth living officers keep from the normal rank and file, for it takes a truly callous leader to send his soldiers against an unkillable foe. While these abominations often serve corrupt monarchs or power-hungry and desperate tyrants, some fexts infiltrate good armies and act as double agents, defying their nation's ideals. They use politics and miscommunication to distort the truth of their battlefield atrocities and cow those under their command into obedience.

   Though a fext normally acts as a commander on the battlefield, when engaged in combat, it favors its martial prowess, intermingling quick strikes and deadly blows with disruptive curses and its energy drain ability.

---

# Fext
This creature’s pallid skin and dead, vacant eyes belie its healthy, powerful physique. It is clad in fearsome armor.
**Source** Bestiary 5 pg. 115, Pathfinder #71: Rasputin Must Die! pg. 88
**XP** 9,600

LE Medium undead
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +20

##### Defense

**AC** 25, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+9 armor, +1 Dex, +1 _[[feats/Dodge|dodge]]_, +2 natural, +2 _[[spells/Shield|shield]]_)
**hp** 127 (15d8+60)
**Fort** +9, **Ref** +9, **Will** +11
**DR** 10/glass or obsidian; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** electricity 10, fire 10; **SR** 21

##### Offense
**Speed** 40 ft. (30 ft. in armor)
**Melee** +1 _[[items/Weapon/Bastard sword|bastard sword]]_ +20/+15/+10 (1d10+8/17–20) or slam +18 (1d4+10 plus _[[universal monster rules/Energy Drain|energy drain]]_)
**Special Attacks** _energy drain_ (1d4 levels, DC 21)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +19)
At will—_[[spells/Death Knell|death knell]]_ (DC 16), _[[spells/Protection From Good|protection from good]]_, _[[spells/Speak with Dead|speak with dead]]_ (DC 17)
3/day—_[[spells/Bestow Curse|bestow curse]]_ (DC 17)

##### Statistics
**Str** 25, **Dex** 18, **Con** —, **Int** 13, **Wis** 15, **Cha** 18
**Base Atk** +11; **CMB** +18; **CMD** 33
**Feats** _[[feats/Cleave|Cleave]]_, _Dodge_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (_bastard sword_), _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_bastard sword_)
**Skills** Acrobatics +4, Disguise +15, Intimidate +20, Knowledge (engineering) +12, Knowledge (religion) +12, Perception +20, Sense Motive +9, Stealth +11
**Languages** Common, Infernal
**SQ** unkillable

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** standard (+1 _bastard sword_, _[[items/Armor/Full plate|full plate]]_, _[[items/Shield/Heavy steel shield|heavy steel shield]]_, other gear)

### Special Abilities

**Unkillable (Su)** When reduced to 0 hit points by anything other than a glass weapon or an obsidian weapon, a _[[monsters/Fext|fext]]_ is not destroyed,but instead becomes _[[conditions/Unconscious|unconscious]]_. Additionally, 1d4 minutes after falling _unconscious_, a _fext_ gains _[[universal monster rules/Fast Healing|fast healing]]_ 1. To be completely destroyed, a _fext_ must be reduced to 0 hit points by a glass or obsidian weapon, or once it is rendered _unconscious_, its head must be severed and anointed with _[[items/Mundane/Holy water|holy water]]_. Once destroyed, a _fext_ dissolves into fine ash.

##### Description

Any good general forbids mention of fexts among his ranks, but such strictures do little to prevent soldiers from whispering tales of undying officers leading enemy units.

These supernatural officers almost never seem to fall in battle, and when they do, they return for the next clash unfazed. Soldiers whisper that these _[[spells/Deathless|deathless]]_ commanders are vulnerable only to glass weapons. Stories of fexts, usually dismissed as camp folktales derived from soldiers’ frustration at failed campaigns and lost battles, are most frighteningly true—a truth living officers keep from the normal rank and file, for it takes a truly callous leader to send his soldiers against an unkillable foe. While these abominations often serve corrupt monarchs or power-hungry and desperate tyrants, some fexts infiltrate good armies and act as double agents, defying their nation’s ideals. They use politics and miscommunication to distort the truth of their battlefield atrocities and cow those under their _[[spells/Command|command]]_ into obedience.

Though a _fext_ normally acts as a commander on the battlefield, when engaged in combat, it favors its martial prowess, intermingling quick strikes and _[[items/Weapon Magic Abilities/Deadly|deadly]]_ blows with _[[feats/Disruptive|disruptive]]_ curses and its _energy drain_ ability.