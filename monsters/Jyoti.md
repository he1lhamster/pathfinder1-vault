---
cssclass: [monsters]
title1: Jyoti
desc_short: This phoenix-like humanoid is surrounded by a halo of radiant energy.
  Its spear is tipped with a carved crystal blade.
title2: Jyoti
CR: 9
sources:
- name: Bestiary 2
  page: 171
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 6400
alignment: N
size: Medium
type: outsider
subtypes:
- extraplanar
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 24
  touch: 16
  flat_footed: 18
  components:
    armor: 4
    dex: 5
    dodge: 1
    natural: 4
HP:
  HP: 104
  long: 11d10+44
  fast_healing: 10
saves:
  fort: 11
  ref: 8
  will: 11
  other: +2 vs. divine
defensive_abilities:
- divine aversion
- positive energy affinity
immunities:
- death attacks
- disease
- energy drain
- poison
resistances:
  acid: 10
  cold: 10
  electricity: 10
  fire: 10
  sonic: 10
SR: 20
speeds:
  base: 30
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 ghost touch spear +14/+9/+4 (1d8+4/×3 plus 1d6 fire)
      entries:
      - - damage: 1d8+4
          crit_multiplier: 3
        - damage: 1d6
          type: fire
      attack: +1 ghost touch spear
      bonus:
      - 14
      - 9
      - 4
    - text: bite +8 (1d6+1 plus 1d6 fire)
      entries:
      - - damage: 1d6+1
        - damage: 1d6
          type: fire
      attack: bite
      bonus:
      - 8
  ranged:
  - - text: ray +16 ranged touch (by spell)
      entries:
      - - effect: by spell
      attack: ray
      bonus:
      - 16
      touch: true
  special:
  - breath weapon (60-ft. cone, 11d6 fire, Reflex DC 19 half, usable once every 1d4
    rounds)
  - positive energy
spell_like_abilities:
  entries:
  - name: mage armor
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: 3/day
  - name: cure serious wounds
    source: default
    freq: 3/day
  - name: daylight
    source: default
    freq: 3/day
  - name: dimension door
    source: default
    freq: 3/day
  - name: lesser restoration
    source: default
    freq: 3/day
  - name: searing light
    source: default
    freq: 3/day
  - name: breath of life
    source: default
    freq: 1/day
  - name: disrupting weapon
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 11
    concentration: 13
ability_scores:
  STR: 14
  DEX: 20
  CON: 19
  INT: 12
  WIS: 15
  CHA: 15
BAB: 11
CMB: 13
CMD: 29
feats:
- name: Combat Casting
- name: Dodge
- name: Flyby Attack
- name: Iron Will
- name: Mobility
- name: Wind Stance
skills:
  Fly: 9
  Heal: 16
  Intimidate: 16
  Knowledge (planes): 19
  Knowledge (religion): 19
  Perception: 20
  Sense Motive: 16
  Stealth: 19
  _racial_mods:
    Knowledge (planes):
      _: 4
    Knowledge (religion):
      _: 4
    Perception:
      _: 4
languages:
- Aquan
- Auran
- Common
- Ignan
- Terran
ecology:
  environment: any (Positive Energy Plane)
  organization: solitary, pair, or flight (3-8)
  treasure_type: double
  treasure:
  - +1 ghost touch spear
  - other treasure
special_abilities:
  Breath Weapon (Su): A jyoti's breath weapon is a focused burst of searing fire infused
    with positive energy. Undead in the area take 11d8 damage rather than 11d6.
  Divine Aversion (Su): Jyoti dislike deities and are never divine spellcasters. Jyoti
    gain a +2 racial bonus on saves against divine magical effects.
  Positive Energy (Su): A jyoti's natural weapons and any weapons it wields strike
    as if they were ghost touch weapons. In addition, any weapon (natural or manufactured)
    a jyoti uses deals +1d6 fire damage on a hit.
  Positive Energy Affinity (Ex): A jyoti can exist comfortably on the Positive Energy
    Plane, and does not benefit (or suffer) from that plane's overwhelming infusions
    of life-giving energies. Whenever a jyoti is subjected to a magical healing effect,
    that effect functions at its full potential, as if enhanced by Maximize Spell.
desc_long: |-
  Enigmatic and swift to anger, the avian race known as the jyoti are xenophobic natives of the Positive Energy Plane. Though some believe the jyoti are inherently good because their home plane is the source of all life, these beliefs are quite in error, for the jyoti react to all other races with wary suspicion at best, and usually assume the worst and attack before they can themselves be attacked. They guard their crystalline cities from all intrusion, especially by creatures from other planes and servants of the gods. They have been known to hold dangerous artifacts in their vaults on behalf of desperate visitors, though in the case of holy or unholy artifacts, the jyoti are more likely to destroy the artifacts as soon as possible.

  Jyoti loathe natives of the Shadow Plane and the Negative Energy Plane in particular, though there is an element of pity in their actions toward undead. They never discuss the sceaduinar, and even hearing that name inflames jyoti into immediate anger. Those who dare argue on the sceaduinar's behalf are immediately attacked.

---

# Jyoti
This phoenix-like humanoid is surrounded by a halo of _[[items/Armor Magic Abilities/Radiant|radiant]]_ energy. Its _[[items/Weapon/Spear|spear]]_ is tipped with a carved crystal blade.
**Source** Bestiary 2 pg. 171
**XP** 6,400

N Medium outsider (extraplanar)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +20

##### Defense

**AC** 24, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +5 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 104 (11d10+44); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +11, **Ref** +8, **Will** +11; +2 vs. divine
**Defensive Abilities** divine _[[spells/Aversion|aversion]]_, positive energy affinity; **Immune** death attacks, disease, _[[universal monster rules/Energy Drain|energy drain]]_, poison; **Resist** acid 10, cold 10, electricity 10, fire 10, sonic 10; **SR** 20

##### Offense
**Speed** 30 ft., fly 90 ft. (good)
**Melee** +1 _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ _spear_ +14/+9/+4 (1d8+4/×3 plus 1d6 fire), bite +8 (1d6+1 plus 1d6 fire)
**Ranged** ray +16 ranged touch (by spell)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 11d6 fire, Reflex DC 19 half, usable once every 1d4 rounds), positive energy
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +13)
Constant—_[[spells/Mage Armor|mage armor]]_
3/day—aid, _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Daylight|daylight]]_, _[[spells/Dimension Door|dimension door]]_, lesser _[[spells/Restoration|restoration]]_, _[[spells/Searing Light|searing light]]_
1/day—_[[spells/Breath Of Life|breath of life]]_, _[[spells/Disrupting Weapon|disrupting weapon]]_

##### Statistics
**Str** 14, **Dex** 20, **Con** 19, **Int** 12, **Wis** 15, **Cha** 15
**Base Atk** +11; **CMB** +13; **CMD** 29
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Fly +9, _[[spells/Heal|Heal]]_ +16, Intimidate +16, Knowledge (planes) +19, Knowledge (religion) +19, Perception +20, Sense Motive +16, Stealth +19; **Racial Modifiers** +4 Knowledge (planes), +4 Knowledge (religion), +4 Perception
**Languages** Aquan, Auran, Common, Ignan, Terran

##### Ecology

**Environment** any (Positive Energy Plane)
**Organization** solitary, pair, or _[[universal monster rules/Flight|flight]]_ (3–8)
**Treasure** double (+1 _ghost touch_ _spear_, other treasure)

### Special Abilities

**_Breath Weapon_ (Su)** A _[[monsters/Jyoti|jyoti]]_’s _breath weapon_ is a focused burst of searing fire infused with positive energy. Undead in the area take 11d8 damage rather than 11d6.

**Divine _Aversion_ (Su)** _Jyoti_ dislike deities and are never divine spellcasters. _Jyoti_ gain a +2 racial bonus on saves against divine magical effects.

**Positive Energy (Su)** A _jyoti_’s natural weapons and any weapons it wields strike as if they were _ghost touch_ weapons. In addition, any weapon (natural or manufactured) a _jyoti_ uses deals +1d6 fire damage on a hit.

**Positive Energy Affinity (Ex)** A _jyoti_ can exist comfortably on the Positive Energy Plane, and does not benefit (or suffer) from that plane’s overwhelming infusions of life-giving energies. Whenever a _jyoti_ is subjected to a magical healing effect, that effect functions at its full potential, as if enhanced by _[[feats/Maximize Spell|Maximize Spell]]_.

##### Description

Enigmatic and swift to anger, the avian race known as the _jyoti_ are xenophobic natives of the Positive Energy Plane. Though some believe the _jyoti_ are inherently good because their home plane is the source of all life, these beliefs are quite in error, for the _jyoti_ react to all other races with wary suspicion at best, and usually assume the worst and attack before they can themselves be attacked. They _[[npcs/Guard|guard]]_ their crystalline cities from all intrusion, especially by creatures from other planes and servants of the gods. They have been known to hold dangerous artifacts in their vaults on behalf of desperate visitors, though in the case of holy or _[[items/Weapon Magic Abilities/Unholy|unholy]]_ artifacts, the _jyoti_ are more likely to destroy the artifacts as soon as possible.

_Jyoti_ loathe natives of the _[[items/Armor Magic Abilities/Shadow|Shadow]]_ Plane and the Negative Energy Plane in particular, though there is an element of pity in their actions toward undead. They never discuss the _[[monsters/Sceaduinar|sceaduinar]]_, and even hearing that name inflames _jyoti_ into immediate anger. Those who dare argue on the _sceaduinar_’s behalf are immediately attacked.