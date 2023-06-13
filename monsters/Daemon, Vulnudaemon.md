---
cssclass: [monsters]
title1: Daemon, Vulnudaemon
desc_short: A bloody, tooth-filled mouth that looks almost like a horrific gash gasps
  in the neck of this pale, childlike horror.
title2: Vulnudaemon
CR: 4
sources:
- name: Bestiary 3
  page: 63
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 1200
alignment: NE
size: Small
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 3
senses:
  darkvision: 60
  detect good: true
  detect magic: true
auras:
- name: aura of doom
  radius: 30
  DC: 18
AC:
  AC: 17
  touch: 14
  flat_footed: 14
  components:
    dex: 3
    natural: 3
    size: 1
HP:
  HP: 39
  long: 6d10+6
saves:
  fort: 6
  ref: 5
  will: 6
DR:
- amount: 5
  weakness: good or silver
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
speeds:
  base: 30
attacks:
  melee:
  - - text: short sword +10/+5 (1d4+2/19-20 plus bleed)
      entries:
      - - damage: 1d4+2
          crit_range: 19-20
        - effect: bleed
      attack: short sword
      bonus:
      - 10
      - 5
    - text: bite +5 (1d3+1)
      entries:
      - - damage: 1d3+1
      attack: bite
      bonus:
      - 5
  special:
  - bleed (1d4)
  - sneak attack +1d6
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: blur
    source: default
    freq: 3/day
  - name: death knell
    source: default
    freq: 3/day
    DC: 15
  - name: invisibility
    source: default
    freq: 3/day
  - name: minor image
    source: default
    freq: 3/day
    DC: 15
  - name: inflict critical wounds
    source: default
    freq: 1/day
    DC: 17
  - name: summon
    source: default
    freq: 1/day
    level: 2
    summons:
    - name: cacodaemons
      amount: 1d4
      chance: 40%
  sources:
  - name: default
    CL: 7
    concentration: 10
ability_scores:
  STR: 14
  DEX: 17
  CON: 13
  INT: 12
  WIS: 13
  CHA: 16
BAB: 6
CMB: 7
CMD: 20
feats:
- name: Ability Focus (aura of doom)
- name: Combat Casting
- name: Weapon Finesse
skills:
  Bluff: 12
  Diplomacy: 10
  Fly: 11
  Knowledge (arcana): 7
  Knowledge (planes): 8
  Perception: 10
  Sense Motive: 10
  Spellcraft: 8
  Stealth: 16
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or murder (3-12)
  treasure_type: standard
special_abilities:
  Aura of Doom (Su): As a free action, a vulnudaemon can radiate an aura of dread
    and hopelessness. Any creature within 30 feet of the vulnudaemon must succeed
    at a DC 18 Will save or become shaken for as long as it remains in the aura.
desc_long: |-
  These deceptive daemons personify death resulting from murder accented with betrayal. Most often formed from the souls of evil creatures killed by family or friends, vulnudaemons spread their insanity throughout the worlds by deceiving and killing all creatures they meet.

  Vulnudaemons stalk their prey, infecting them with a sense of impending doom and watching their reactions, learning their responses before attacking and savoring their death. These daemons serve as excellent assassins, hiding in the shadows before debilitating their enemies, or striking from the protection of invisibility in order to deliver the killing blow. When facing stronger enemies, vulnudaemons seek to wear them down through a series of attacks, nicking at them and darting off, then repeating the process until their opponents bleed out.

  Vulnudaemons often find themselves called to the Material Plane by cultists of deities associated with murder and assassination. These cultists often see vulnudaemons as sacred creatures favored by their deity, and rather than simply use the daemons as assassins, cultists often grant them a shocking degree of freedom to wander the region as they will, picking victims to fit their own agendas and murdering whomever they wish. Cultists who conjure vulnudaemons into the world usually take care to show the daemons a secret hand sign or other code that members of the cult can show them, lest the monsters decide to target one of the believers for an attack. Whether or not an accidentally targeted cultist has the time to flash her safety sign to the daemon should the creature attack her at a later date is, of course, another matter.

  Vulnudaemons stand 3 feet tall and weigh 25 pounds.

---

# Daemon, Vulnudaemon
A bloody, tooth-filled mouth that looks almost like a horrific gash gasps in the neck of this pale, _[[feats/Childlike|childlike]]_ horror.
**Source** Bestiary 3 pg. 63
**XP** 1,200

NE Small outsider (daemon, evil, extraplanar)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_; Perception +10
**Aura** _[[spells/Aura of Doom|aura of doom]]_ (30 ft., DC 18)

##### Defense

**AC** 17, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 Dex, +3 natural, +1 size)
**hp** 39 (6d10+6)
**Fort** +6, **Ref** +5, **Will** +6
**DR** 5/good or silver; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Short sword|short sword]]_ +10/+5 (1d4+2/19–20 plus _[[universal monster rules/Bleed|bleed]]_), bite +5 (1d3+1)
**Special Attacks** _bleed_ (1d4), sneak attack +1d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +10)
Constant—_detect good_, _detect magic_
3/day—_[[spells/Blur|blur]]_, _[[spells/Death Knell|death knell]]_ (DC 15), _[[spells/Invisibility|invisibility]]_, _[[spells/Minor Image|minor image]]_ (DC 15)
1/day—_[[spells/Inflict Critical Wounds|inflict critical wounds]]_ (DC 17), _[[universal monster rules/Summon|summon]]_ (level 2, 1d4 cacodaemons 40%)

##### Statistics
**Str** 14, **Dex** 17, **Con** 13, **Int** 12, **Wis** 13, **Cha** 16
**Base Atk** +6; **CMB** +7; **CMD** 20
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_aura of doom_), _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +12, Diplomacy +10, Fly +11, Knowledge (arcana) +7, Knowledge (planes) +8, Perception +10, Sense Motive +10, Spellcraft +8, Stealth +16
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or murder (3–12)
**Treasure** standard

### Special Abilities

**_Aura of Doom_ (Su)** As a free action, a vulnudaemon can radiate an aura of dread and hopelessness. Any creature within 30 feet of the vulnudaemon must succeed at a DC 18 Will save or become _[[conditions/Shaken|shaken]]_ for as long as it remains in the aura.

##### Description

These _[[items/Weapon Magic Abilities/Deceptive|deceptive]]_ daemons personify death resulting from murder accented with betrayal. Most often formed from the souls of evil creatures killed by family or friends, vulnudaemons spread their _[[spells/Insanity|insanity]]_ throughout the worlds by _[[items/Armor Magic Abilities/Deceiving|deceiving]]_ and killing all creatures they meet.

Vulnudaemons stalk their prey, infecting them with a sense of impending _[[spells/Doom|doom]]_ and watching their reactions, learning their responses before attacking and savoring their death. These daemons serve as excellent assassins, hiding in the shadows before _[[items/Weapon Magic Abilities/Debilitating|debilitating]]_ their enemies, or striking from the protection of _invisibility_ in order to deliver the killing blow. When facing stronger enemies, vulnudaemons seek to wear them down through a series of attacks, nicking at them and darting off, then repeating the process until their opponents _bleed_ out.

Vulnudaemons often find themselves _[[items/Weapon Magic Abilities/Called|called]]_ to the Material Plane by cultists of deities associated with murder and assassination. These cultists often see vulnudaemons as _[[items/Weapon Magic Abilities/Sacred|sacred]]_ creatures favored by their deity, and rather than simply use the daemons as assassins, cultists often grant them a shocking degree of _[[spells/Freedom|freedom]]_ to wander the region as they will, picking victims to fit their own agendas and murdering whomever they _[[spells/Wish|wish]]_. Cultists who conjure vulnudaemons into the world usually take care to show the daemons a secret hand sign or other code that members of the cult can show them, lest the monsters decide to target one of the believers for an attack. Whether or not an accidentally targeted _[[npcs/Cultist|cultist]]_ has the time to flash her safety sign to the daemon should the creature attack her at a later date is, of course, another matter.

Vulnudaemons stand 3 feet tall and weigh 25 pounds.