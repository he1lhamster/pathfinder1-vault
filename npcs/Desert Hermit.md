---
cssclass: [monsters]
title1: Desert Hermit
desc_short: This weathered-looking desert dweller is dressed from head to toe in tan,
  loose-fitting robes.
title2: Desert Hermit
CR: 8
sources:
- name: Osirion, Legacy of the Pharaohs
  page: 57
  link: http://paizo.com/products/btpy93n8?Pathfinder-Campaign-Setting-Osirion-Legacy-of-Pharaohs
XP: 4800
race: Human
classes:
- druid 9
alignment: N
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 3
AC:
  AC: 18
  touch: 15
  flat_footed: 14
  components:
    armor: 3
    deflection: 1
    dex: 3
    dodge: 1
HP:
  HP: 80
  long: 9d8+36
saves:
  fort: 8
  ref: 6
  will: 11
  other: +4 vs. fey and plant-targeted effects
defensive_abilities:
- heat shimmer (6 rounds, DC 17)
immunities:
- poison
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk scimitar +9/+4 (1d6+2/18-20)
      entries:
      - - damage: 1d6+2
          crit_range: 18-20
      attack: mwk scimitar
      bonus:
      - 9
      - 4
  ranged:
  - - text: sling +9 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: sling
      bonus:
      - 9
  special:
  - wild shape 3/day
spell_like_abilities:
  entries:
  - name: lesser planar ally
    source: default
    freq: 1/day
    other: janni only
  sources:
  - name: default
    CL: 9
spells:
  entries:
  - name: control winds
    source: Druid
    level: 5
    DC: 19
  - is_domain_spell: true
    name: transmute rock to mud
    source: Druid
    level: 5
    other: create loose sand instead of mud
    DC: 19
  - name: giant vermin
    source: Druid
    level: 4
  - is_domain_spell: true
    name: hallucinatory terrain
    source: Druid
    level: 4
    DC: 17
  - superscripts:
    - APG
    name: vermin shape II
    source: Druid
    level: 4
  - superscripts:
    - UM
    name: burrow
    source: Druid
    level: 3
  - is_domain_spell: true
    superscripts:
    - APG
    name: cup of dust
    source: Druid
    level: 3
    DC: 17
  - name: greater magic fang
    source: Druid
    level: 3
  - name: neutralize poison
    source: Druid
    level: 3
  - superscripts:
    - UM
    name: spit venom
    source: Druid
    level: 3
    DC: 17
  - name: barkskin
    source: Druid
    level: 2
  - superscripts:
    - APG
    name: elemental speech
    source: Druid
    level: 2
  - superscripts:
    - UM
    name: pernicious poison
    source: Druid
    level: 2
  - name: resist energy
    source: Druid
    level: 2
  - is_domain_spell: true
    superscripts:
    - APG
    name: shifting sand
    source: Druid
    level: 2
    DC: 16
  - name: summon swarm
    source: Druid
    level: 2
  - superscripts:
    - APG
    name: alter winds
    source: Druid
    level: 1
    DC: 15
  - is_domain_spell: true
    superscripts:
    - APG
    name: cloak of shade
    source: Druid
    level: 1
  - name: faerie fire
    source: Druid
    level: 1
  - superscripts:
    - APG
    name: feather step
    source: Druid
    level: 1
  - name: longstrider
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: detect poison
    source: Druid
    level: 0
  - name: light
    source: Druid
    level: 0
  - name: virtue
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 9
    concentration: 12
    slots:
      0: at-will
    domains:
    - desert
ability_scores:
  STR: 14
  DEX: 16
  CON: 14
  INT: 10
  WIS: 16
  CHA: 8
BAB: 6
CMB: 8
CMD: 23
feats:
- name: Combat Casting
- name: Dodge
- name: Iron Will
- name: Natural Spell
- name: Spell Focus (transmutation)
- name: Toughness
skills:
  Fly: 15
  Knowledge (nature): 14
  Perception: 15
  Stealth: 12
  Survival: 17
languages:
- Common
- Druidic
- Osiriani
special_qualities:
- nature bond (Desert domain)
- nature sense
- trackless step
- wild empathy +8
- woodland stride
ecology:
  environment: any (Osirion)
  organization: solitary
  treasure_type: NPC Gear
  treasure:
  - +1 leather armor
  - mwk scimitar
  - sling with 10 bullets
  - belt of incredible dexterity +2
  - campfire bead
  - ring of protection +1
  - wand of cure moderate wounds [16 charges]
  - wand of endure elements [20 charges]
  - 40 gp
desc_long: |-
  A desert hermit seeks the solitude in the windswept wastes for two chief reasons. First, the hermit finds that isolation allows him to more easily experience nature's harsh beauty and raw power, which he seeks to emulate. Second, the wide open spaces provide the hermit with the freedom to experience the world without interference from human society, which is trapped in meaningless competitions to get ahead in a race toward an unhappy death plagued by debt, troublesome relationships, and arbitrary expectations enforced by shame, discrimination, and even violence.

  Desert hermits are often defensive and suspicious when interrupted by outsiders. They rarely form druid circles, preferring true isolation. Those who forgo their connection to the desert in favor of a bestial ally tend to select camels, cobras, jackals, and vultures.

---

# Desert Hermit
This weathered-looking _[[feats/Desert Dweller|desert dweller]]_ is dressed from head to toe in tan, loose-fitting robes.
**Source** Osirion, Legacy of the Pharaohs pg. 57
**XP** 4,800
Human _[[classes/Druid|druid]]_ 9

N Medium humanoid (human)
**Init** +3; **Senses** Perception +15

##### Defense

**AC** 18, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 armor, +1 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 80 (9d8+36)
**Fort** +8, **Ref** +6, **Will** +11; +4 vs. fey and plant-targeted effects
**Defensive Abilities** _[[universal monster rules/Heat|heat]]_ shimmer (6 rounds, DC 17); **Immune** poison

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Scimitar|scimitar]]_ +9/+4 (1d6+2/18–20)
**Ranged** _[[items/Weapon/Sling|sling]]_ +9 (1d4+2)
**Special Attacks** wild shape 3/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th)
1/day—lesser _[[spells/Planar Ally|planar ally]]_ (janni only)
**_Druid_ Spells Prepared **(CL 9th; concentration +12)
5th—_[[spells/Control Winds|control winds]]_ (DC 19), _[[spells/Transmute Rock to Mud|transmute rock to mud]]_ (create loose sand instead of mud, DC 19)
4th—_[[spells/Giant Vermin|giant vermin]]_, _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 17), _[[spells/Vermin Shape II|vermin shape II]]_
3rd—_[[universal monster rules/Burrow|burrow]]_, cup of dustAPG, D (DC 17), greater _[[spells/Magic Fang|magic fang]]_, _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Spit Venom|spit venom]]_ (DC 17)
2nd—_[[spells/Barkskin|barkskin]]_, _[[spells/Elemental Speech|elemental speech]]_, _[[spells/Pernicious Poison|pernicious poison]]_, _[[spells/Resist Energy|resist energy]]_, shifting sandAPG, D (DC 16), _[[spells/Summon Swarm|summon swarm]]_
1st—_[[spells/Alter Winds|alter winds]]_ (DC 15), cloak of shadeAPG, D, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Feather Step|feather step]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Virtue|virtue]]_
**D **Domain spell; **Domains **Desert

##### Statistics
**Str** 14, **Dex** 16, **Con** 14, **Int** 10, **Wis** 16, **Cha** 8
**Base Atk** +6; **CMB** +8; **CMD** 23
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (transmutation), _[[feats/Toughness|Toughness]]_
**Skills** Fly +15, Knowledge (nature) +14, Perception +15, Stealth +12, Survival +17
**Languages** Common, Druidic, Osiriani
**SQ** nature bond (Desert domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +8, woodland stride

##### Ecology

**Environment** any (Osirion)
**Organization** solitary
**Treasure** NPC gear (+1 _[[items/Armor/Leather armor|leather armor]]_, mwk _scimitar_, _sling_ with 10 bullets, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Campfire Bead|campfire bead]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ [16 charges], wand of _[[spells/Endure Elements|endure elements]]_ [20 charges], 40 gp)

A _[[npcs/Desert Hermit|desert hermit]]_ seeks the solitude in the windswept wastes for two chief reasons. First, the _[[npcs/Hermit|hermit]]_ finds that isolation allows him to more easily experience nature’s harsh beauty and raw power, which he seeks to emulate. Second, the wide open spaces provide the _hermit_ with the _[[spells/Freedom|freedom]]_ to experience the world without interference from human society, which is trapped in meaningless competitions to get ahead in a race toward an unhappy death plagued by debt, troublesome relationships, and arbitrary expectations enforced by shame, discrimination, and even violence.

Desert hermits are often defensive and suspicious when interrupted by outsiders. They rarely form _druid_ circles, preferring true isolation. Those who forgo their connection to the desert in favor of a bestial ally tend to select camels, cobras, jackals, and vultures.