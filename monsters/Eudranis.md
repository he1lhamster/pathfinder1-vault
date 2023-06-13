---
cssclass: [monsters]
title1: Eudranis
desc_short: Garbed in tattered robes, this emaciated humanoid creature stares out
  with unblinking white eyes. In one hand, he clutches a great blade, while his other
  hand holds an idol of some fell power.
title2: Eudranis
CR: 5
sources:
- name: Darklands Revisited
  page: 33
  link: http://paizo.com/products/btpy9j72?Pathfinder-Campaign-Setting-Darklands-Revisited
XP: 1600
race: Male
classes:
- morlock cleric of Lamashtu 4 (Pathfinder RPG Bestiary 209)
alignment: CE
size: Medium
type: monstrous humanoid
initiative:
  bonus: 3
senses:
  darkvision: 120
  scent: true
AC:
  AC: 20
  touch: 12
  flat_footed: 18
  components:
    armor: 7
    dex: 2
    natural: 1
HP:
  HP: 59
  long: 4d8+3d10+25
  HD: 7
saves:
  fort: 9
  ref: 8
  will: 14
immunities:
- disease
- poison
weaknesses:
- light blindness
speeds:
  base: 40
  base_other: 30 ft. in armor
  climb: 30
attacks:
  melee:
  - - text: mwk falchion +9/+4 (2d4+3/18-20)
      entries:
      - - damage: 2d4+3
          crit_range: 18-20
      attack: mwk falchion
      bonus:
      - 9
      - 4
  - - text: bite +3 (1d4+1)
      entries:
      - - damage: 1d4+1
      attack: bite
      bonus:
      - 3
  special:
  - channel negative energy 3/day (DC 12, 2d6)
  - sneak attack +1d6
spell_like_abilities:
  entries:
  - name: touch of chaos
    source: default
    freq: 7/day
  - name: vision of madness
    source: default
    freq: 7/day
    other: +/-2
  sources:
  - name: default
    CL: 4
    concentration: 8
spells:
  entries:
  - is_domain_spell: true
    name: align weapon
    source: Cleric
    level: 2
    other: chaos only
  - name: hold person
    source: Cleric
    level: 2
    DC: 16
  - name: resist energy
    source: Cleric
    level: 2
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - superscripts:
    - UM
    name: murderous command
    source: Cleric
    level: 1
    DC: 15
  - is_domain_spell: true
    name: protection from law
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 14
  - name: create water
    source: Cleric
    level: 0
  - name: detect magic
    source: Cleric
    level: 0
  - name: purify food and drink
    source: Cleric
    level: 0
    DC: 14
  sources:
  - name: Cleric
    type: prepared
    CL: 4
    concentration: 8
    slots:
      0: at-will
    domains:
    - chaos
    - madness
ability_scores:
  STR: 14
  DEX: 16
  CON: 16
  INT: 7
  WIS: 18
  CHA: 10
BAB: 6
CMB: 8
CMD: 21
feats:
- name: Combat Casting
- name: Extra Channel
- name: Iron Will
- name: Power Attack
skills:
  Acrobatics: 8
  Climb: 18
  Knowledge (planes): 4
  Knowledge (religion): 4
  Perception: 8
  Sense Motive: 8
  Stealth: -1
    in caverns: 3
  _racial_mods:
    Acrobatics:
      _: 8
    Climb:
      _: 8
languages:
- Undercommon
special_qualities:
- +4 stealth in caverns
- expert climber
- leap attack
- swarming
gear:
  combat:
  - potion of bestow curse
  - scroll of daze monster
  - wand of cure light wounds (30 charges)
  other:
  - +1 chainmail
  - mwk falchion
  - cloak of resistance +1
  - silver holy symbol of Lamashtu
desc_long: |-
  A devotee of the goddess Lamashtu, Eudranis found himself as a speaker for the Mother of Monsters following his tribe's encounter with a group of Pathfinder Society agents. These agents presented themselves as the morlocks' ancestors, effectively turning Eudranis's tribe into indentured slave labor for the Pathfinders' archaeological endeavors. Though he was initially honored to serve his revered ancestors, Eudranis became suspicious when they appeared to have only their own interests in mind, ignoring the well-being of their “descendants.” Following a vivid nightmare in which the Pathfinders abandoned the morlocks and absconded with the treasures of their ancestors, Eudranis spied on the resting agents. Overhearing the Pathfinders' mockery of the simple morlocks shattered Eudranis's faith in his ancestor worship. He began preaching against the Pathfinders in secret and gathered his tribe for a retributive strike.

  Following a night of bloodshed, the morlocks tortured and slew the Pathfinders, whose screams echoed through the ruins of the ancient Azlanti city they had come to plunder. The morlocks soon hailed Eudranis as a prophet of the tribe's new true goddess, Lamashtu. Guiding his tribe fully into Lamashtu's worship, Eudranis has vowed never to be tricked by humanity again. The morlocks of his tribe have embraced their monstrous physiques and abandoned the reverence their race traditionally holds for their human ancestors.

---

# Eudranis
Garbed in tattered robes, this emaciated humanoid creature stares out with unblinking white eyes. In one hand, he clutches a great blade, while his other hand holds an idol of some fell power.
**Source** Darklands Revisited pg. 33
**XP** 1,600
Male _[[monsters/Morlock|morlock]]_ _[[classes/Cleric|cleric]]_ of Lamashtu 4 (Pathfinder RPG Bestiary 209)
CE Medium monstrous humanoid
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Scent|scent]]_; Perception +8

##### Defense

**AC** 20, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+7 armor, +2 Dex, +1 natural)
**hp** 59 (7 HD; 4d8+3d10+25)
**Fort** +9, **Ref** +8, **Will** +14
**Immune** disease, poison
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 40 ft. (30 ft. in armor), _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** mwk _[[items/Weapon/Falchion|falchion]]_ +9/+4 (2d4+3/18–20) or bite +3 (1d4+1)
**Special Attacks** channel negative energy 3/day (DC 12, 2d6), sneak attack +1d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +8)
7/day—touch of chaos, _[[spells/Vision|vision]]_ of madness (+/–2)
**_Cleric_ Spells Prepared **(CL 4th; concentration +8)
2nd—_[[spells/Align Weapon|align weapon]]_ (chaos only), _[[spells/Hold Person|hold person]]_ (DC 16), _[[spells/Resist Energy|resist energy]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Murderous Command|murderous command]]_ (DC 15), _[[spells/Protection From Law|protection from law]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 14), _[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Purify Food and Drink|purify food and drink]]_ (DC 14)
**D** Domain spell; **Domains** Chaos, Madness

##### Statistics
**Str** 14, **Dex** 16, **Con** 16, **Int** 7, **Wis** 18, **Cha** 10
**Base Atk** +6; **CMB** +8; **CMD** 21
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Acrobatics +8, _Climb_ +18, Knowledge (planes) +4, Knowledge (religion) +4, Perception +8, Sense Motive +8, Stealth –1 (+3 in caverns); **Racial Modifiers** +8 Acrobatics, +8 _Climb_
**Languages** Undercommon
**SQ** +4 stealth in caverns, expert climber, leap attack, swarming
**Combat Gear** potion of _[[spells/Bestow Curse|bestow curse]]_, scroll of _[[spells/Daze Monster|daze monster]]_, wand of _cure light wounds_ (30 charges); **Other Gear** +1 _[[items/Armor/Chainmail|chainmail]]_, mwk _falchion_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, silver holy symbol of Lamashtu

##### Description

A devotee of the goddess Lamashtu, _[[monsters/Eudranis|Eudranis]]_ found himself as a speaker for the Mother of Monsters following his tribe’s encounter with a group of Pathfinder Society agents. These agents presented themselves as the morlocks’ ancestors, effectively turning _Eudranis_’s tribe into indentured _[[items/Mundane/Slave|slave]]_ labor for the Pathfinders’ archaeological endeavors. Though he was initially honored to serve his revered ancestors, _Eudranis_ became suspicious when they appeared to have only their own interests in mind, ignoring the well-being of their “descendants.” Following a vivid _[[spells/Nightmare|nightmare]]_ in which the Pathfinders abandoned the morlocks and absconded with the treasures of their ancestors, _Eudranis_ spied on the resting agents. Overhearing the Pathfinders’ mockery of the simple morlocks shattered _Eudranis_’s faith in his ancestor worship. He began preaching against the Pathfinders in secret and gathered his tribe for a retributive strike.

Following a night of bloodshed, the morlocks tortured and slew the Pathfinders, whose screams echoed through the ruins of the ancient Azlanti city they had come to plunder. The morlocks soon hailed _Eudranis_ as a _[[feats/Prophet|prophet]]_ of the tribe’s new true goddess, Lamashtu. Guiding his tribe fully into Lamashtu’s worship, _Eudranis_ has vowed never to be tricked by humanity again. The morlocks of his tribe have embraced their monstrous physiques and abandoned the reverence their race traditionally holds for their human ancestors.