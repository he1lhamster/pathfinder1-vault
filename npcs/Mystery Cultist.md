---
cssclass: [monsters]
title1: Mystery Cultist
desc_short: Every step this fashionable Varisian takes seems like part of a dance,
  her dozens of strange baubles tinkling with her every movement.
title2: Mystery Cultist
CR: 2
sources:
- name: Magnimar, City of Monuments
  page: 55
  link: http://paizo.com/products/btpy8slp?Pathfinder-Campaign-Setting-Magnimar-City-of-Monuments
XP: 600
race: Female
classes:
- human cleric of Ashava 3
alignment: CG
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 2
AC:
  AC: 14
  touch: 13
  flat_footed: 11
  components:
    armor: 1
    dex: 2
    dodge: 1
HP:
  HP: 20
  long: 3d8+3
saves:
  fort: 3
  ref: 3
  will: 6
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk bladed scarf +5 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: mwk bladed scarf
      bonus:
      - 5
  - - text: dagger +4 (1d4+1/19-20)
      entries:
      - - damage: 1d4+1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 4
  ranged:
  - - text: light crossbow +4 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 4
  special:
  - channel positive energy 4/ day (DC 12, 2d6)
spell_like_abilities:
  entries:
  - name: touch of darkness
    source: default
    freq: 6/day
    other: 1 rounds
  - name: touch of good
    source: default
    freq: 6/day
    other: '+1'
  sources:
  - name: default
    CL: 3
    concentration: 6
spells:
  entries:
  - is_domain_spell: true
    name: blindness/deafness
    source: Cleric
    level: 2
    DC: 15
  - name: lesser restoration
    source: Cleric
    level: 2
  - name: command
    source: Cleric
    level: 1
    DC: 14
  - name: detect undead
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: faerie fire
    source: Cleric
    level: 1
  - name: magic weapon
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: purify food and drink
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 3
    concentration: 6
    slots:
      0: at-will
    domains:
    - good
    - moon
ability_scores:
  STR: 12
  DEX: 14
  CON: 10
  INT: 8
  WIS: 17
  CHA: 13
BAB: 2
CMB: 3
CMD: 16
feats:
- name: Dodge
- name: Mobility
- name: Weapon Finesse
skills:
  Diplomacy: 6
  Heal: 8
  Knowledge (religion): 4
  Perception: 3
languages:
- Common
- Varisian
special_qualities:
- aura
ecology:
  environment: any (Magnimar)
  organization: solitary, ensemble (2-4), or cult (5-9)
  treasure_type: NPC Gear
  treasure:
  - masterwork bladed scarf
  - light crossbow with 20 bolts
  - dagger
  - bracers of armor +1
  - potion of cure light wounds
  - other treasure
desc_long: |-
  Just as the legendary Mistress Ordellia Whilwren once prayed to a mysterious angel to save Magnimar from a devastating deluge, other dwellers of the city have likewise devoted themselves to holy figures, including angels, azatas, and agathions. Called “mystery cultists” by most Magnimarians because of their small numbers and esoteric manner of worship, the dedicated followers of the empyreal lords keep to themselves and rarely proselytize. Most mystery cults hold at least one of Magnimar's numerous monuments in high esteem, whether for their importance in local traditions or their part in Varisian legends. Practitioners of these religions often congregate around structures such as the Arvensoar, the Irespan, or the Mistress of Angels to practice their faith, sometimes forming assemblies of over a hundred worshipers. Although the cults' gatherings can occasionally be disruptive to the flow of traffic throughout the City of Monuments, Magnimar's leaders do little to dissuade the cults' practices, which are almost wholly harmless and serve to promote life, freedom, and other righteous virtues.

  Three of the most commonly worshiped figures among the mystery cults of Magnimar are the empyreal lords Ashava, Soralyon, and Ylimancha (see page 25 for more information on these empyreal lords), though smaller cults to other celestial beings are not uncommon in the City of Monuments.

---

# Mystery Cultist
Every step this fashionable Varisian takes seems like part of a dance, her dozens of strange baubles tinkling with her every movement.
**Source** Magnimar, City of Monuments pg. 55
**XP** 600
Female human _[[classes/Cleric|cleric]]_ of Ashava 3

CG Medium humanoid (human)
**Init** +2; **Senses** Perception +3

##### Defense

**AC** 14, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 11 (+1 armor, +2 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 20 (3d8+3)
**Fort** +3, **Ref** +3, **Will** +6

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Bladed scarf|bladed scarf]]_ +5 (1d6+1) or _[[items/Weapon/Dagger|dagger]]_ +4 (1d4+1/19–20)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +4 (1d8/19–20)
**Special Attacks** channel positive energy 4/ day (DC 12, 2d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +6)
6/day—touch of _[[spells/Darkness|darkness]]_ (1 rounds)
6/day—touch of good (+1)
**_Cleric_ Spells Prepared **(CL 3rd; concentration +6)
2nd—blindness/deafness (DC 15), lesser _[[spells/Restoration|restoration]]_
1st—_[[spells/Command|command]]_ (DC 14), _[[spells/Detect Undead|detect undead]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Magic Weapon|magic weapon]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Purify Food and Drink|purify food and drink]]_
**D** Domain spell; **Domains **Good, Moon*

##### Statistics
**Str** 12, **Dex** 14, **Con** 10, **Int** 8, **Wis** 17, **Cha** 13
**Base Atk** +2; **CMB** +3; **CMD** 16
**Feats** _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Diplomacy +6, _[[spells/Heal|Heal]]_ +8, Knowledge (religion) +4
**Languages** Common, Varisian
**SQ** aura

##### Ecology

**Environment** any (Magnimar)
**Organization** solitary, _[[feats/Ensemble|ensemble]]_ (2–4), or cult (5–9)
**Treasure** NPC gear (masterwork _bladed scarf_, _light crossbow_ with 20 bolts, _dagger_, _[[items/Wondrous Item/Bracers of Armor +1|bracers of armor +1]]_, potion of _[[spells/Cure Light Wounds|cure light wounds]]_, other treasure)
* See Pathfinder Campaign Setting: Dragon Empires Gazetteer.

Just as the legendary Mistress Ordellia Whilwren once prayed to a mysterious angel to save Magnimar from a devastating deluge, other dwellers of the city have likewise devoted themselves to holy figures, including angels, azatas, and agathions. _[[items/Weapon Magic Abilities/Called|Called]]_ “mystery cultists” by most Magnimarians because of their small numbers and esoteric manner of worship, the dedicated followers of the empyreal lords keep to themselves and rarely proselytize. Most mystery cults hold at least one of Magnimar’s numerous monuments in high esteem, whether for their importance in local traditions or their part in Varisian legends. Practitioners of these religions often congregate around structures such as the Arvensoar, the Irespan, or the Mistress of Angels to practice their faith, sometimes forming assemblies of over a hundred worshipers. Although the cults’ gatherings can occasionally be _[[feats/Disruptive|disruptive]]_ to the flow of traffic throughout the City of Monuments, Magnimar’s leaders do little to dissuade the cults’ practices, which are almost wholly harmless and serve to promote life, _[[spells/Freedom|freedom]]_, and other _[[items/Armor Magic Abilities/Righteous|righteous]]_ virtues.

Three of the most commonly worshiped figures among the mystery cults of Magnimar are the empyreal lords Ashava, Soralyon, and Ylimancha (see page 25 for more information on these empyreal lords), though smaller cults to other celestial beings are not uncommon in the City of Monuments.