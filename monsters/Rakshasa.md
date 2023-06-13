---
cssclass: [monsters]
title1: Rakshasa
desc_short: Fine jewelry and clothing accentuate this tiger-headed figure's striped
  fur and formidable fangs.
title2: Mythic Rakshasa
CR: 12
MR: 5
sources:
- name: Mythic Adventures
  page: 215
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 19200
alignment: LE
size: Medium
type: outsider
subtypes:
- mythic
- native
- shapechanger
initiative:
  bonus: 14
senses:
  darkvision: 60
  scent: true
AC:
  AC: 35
  touch: 21
  flat_footed: 29
  components:
    dex: 5
    dodge: 1
    insight: 5
    natural: 14
HP:
  HP: 165
  long: 10d10+110
saves:
  fort: 9
  ref: 12
  will: 8
defensive_abilities:
- telepathic dodge
DR:
- amount: 15
  weakness: epic and good and piercing
SR: 27
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 kukri +16/+11 (1d4+6/15-20)
      entries:
      - - damage: 1d4+6
          crit_range: 15-20
      attack: +1 kukri
      bonus:
      - 16
      - 11
    - text: bite +5 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: bite
      bonus:
      - 5
    - text: claw +10 (1d4+5)
      entries:
      - - damage: 1d4+5
      attack: claw
      bonus:
      - 10
  special:
  - detect thoughts
  - modify memory
  - mythic power (5/day, surge +1d8)
  - wild arcana (see page 14)
spells:
  entries:
  - name: charm monster
    source: '?'
    level: 4
    DC: 19
  - name: dimension door
    source: '?'
    level: 4
  - is_mythic_spell: true
    name: lightning bolt
    source: '?'
    level: 3
    DC: 18
  - is_mythic_spell: true
    name: suggestion
    source: '?'
    level: 3
    DC: 18
  - name: vampiric touch
    source: '?'
    level: 3
  - name: acid arrow
    source: '?'
    level: 2
  - is_mythic_spell: true
    name: invisibility
    source: '?'
    level: 2
  - name: minor image
    source: '?'
    level: 2
    DC: 17
  - name: mirror image
    source: '?'
    level: 2
  - name: charm person
    source: '?'
    level: 1
    DC: 16
  - name: mage armor
    source: '?'
    level: 1
  - is_mythic_spell: true
    name: magic missile
    source: '?'
    level: 1
  - name: shield
    source: '?'
    level: 1
  - is_mythic_spell: true
    name: silent image
    source: '?'
    level: 1
    DC: 16
  - name: dancing lights
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
    DC: 15
  - name: mage hand
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 7
    concentration: 12
    slots:
      4: 5
      3: 7
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 16
  DEX: 20
  CON: 22
  INT: 13
  WIS: 13
  CHA: 21
BAB: 10
CMB: 13
CMD: 34
feats:
- is_mythic: true
  name: Combat Expertise
- name: Dodge
- name: Improved Critical (kukri)
- is_mythic: true
  name: Improved Initiative
- is_mythic: true
  name: Weapon Finesse
skills:
  Bluff: 22
  Diplomacy: 18
  Disguise: 26
  Perception: 14
  Perform (any one): 18
  Sense Motive: 14
  Stealth: 18
  _racial_mods:
    Bluff:
      _: 4
    Disguise:
      _: 8
languages:
- Common
- Infernal
- Undercommon
special_qualities:
- change shape (any humanoid; alter self)
- mythic spellcasting (see page 50)
ecology:
  environment: any
  organization: solitary, pair, or cult (3-12)
  treasure_type: double
  treasure:
  - +1 kukri
  - other treasure
special_abilities:
  Detect Thoughts (Su): A rakshasa can detect thoughts as the spell (CL 18th). It
    can suppress or resume this ability as a free action. When a rakshasa uses this
    ability, it always functions as if it had spent 3 rounds concentrating and thus
    gains the maximum amount of information possible. A creature can resist this effect
    with a successful DC 20 Will save. The save DC is Charisma-based.
  Modify Memory (Sp): A mythic rakshasa can expend one use of mythic power as a swift
    action to modify the memory of a creature whose mind it is reading, as the modify
    memory spell (CL 18th). The creature can resist with a successful DC 20 Will save.
    The save DC is Charisma-based.
  Telepathic Dodge (Su): A mythic rakshasa gains an insight bonus to its AC against
    creatures whose minds it can read. It doesn't need to use its detect thoughts
    ability to gain this bonus. The rakshasa doesn't gain this bonus against creatures
    that are mindless or whose minds can't be read (such as from a mind blank spell).
desc_long: A mythic rakshasa is a natural mind reader and uses its abilities to tempt
  great heroes into failure and ruin-all toward to ultimate goal of seeding an entire
  civilization's destruction.

---

# Rakshasa
This figure’s backward-bending fingers and its bestial, snarling visage leave little doubt as to its fiendish nature.
**Source** Pathfinder RPG Bestiary pg. 231
**XP** 9,600

LE Medium outsider (native, shapechanger)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +14

##### Defense

**AC** 25, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+5 Dex, +1 _[[feats/Dodge|dodge]]_, +9 natural)
**hp** 115 (10d10+60)
**Fort** +9, **Ref** +12, **Will** +8
**DR** 15/good and piercing; **SR** 25

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Kukri|kukri]]_ +16/+11 (1d4+4/15–20), claw +10 (1d4+1), bite +10 (1d6+1)
**Special Attacks** _[[spells/Detect Thoughts|detect thoughts]]_
**Spells Known **(CL 7th)
3rd (5/day)—_[[spells/Lightning Bolt|lightning bolt]]_ (DC 16), _[[spells/Suggestion|suggestion]]_ (DC 16)
2nd (7/day)—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Minor Image|minor image]]_
1st (7/day)—_[[spells/Charm Person|charm person]]_ (DC 14), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/Silent Image|silent image]]_
0—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_

##### Statistics
**Str** 16, **Dex** 20, **Con** 22, **Int** 13, **Wis** 13, **Cha** 17
**Base Atk** +10; **CMB** +13; **CMD** 29
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_kukri_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +20, Diplomacy +16, Disguise +24, Perception +14, Perform +16, Sense Motive +14, Stealth +18; **Racial Modifiers** +4 Bluff, +8 Disguise
**Languages** Common, Infernal, Undercommon
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any humanoid, _[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** any
**Organization** solitary, pair, or cult (3–12)
**Treasure** double (+1 _kukri_, other treasure)

### Special Abilities

**_Detect Thoughts_ (Su)** A _[[monsters/Rakshasa|rakshasa]]_ can _detect thoughts_ as per the spell of the same name (CL 18th). It can suppress or resume this ability as a free action. When a _rakshasa_ uses this ability, it always functions as if it had spent three rounds concentrating and thus gains the maximum amount of information possible. A creature can resist this effect with a DC 18 Will save. The save DC is Charisma-based.

##### Description

The _rakshasa_ is an evil spirit that cloaks itself in the guise of a humanoid creature that it might walk _[[items/Weapon Magic Abilities/Unseen|unseen]]_ among its prey. They embody what is taboo among most societies, and in the shape of those it seeks to defile, a _rakshasa_ gorges itself on these hideous acts. Were they human, these acts of cannibalism, _[[spells/Blasphemy|blasphemy]]_, and worse would mark them as criminals condemned to the cruelest of hells.

When not disguised as a humanoid, the otherwise humanoid _rakshasa_ has the head of an animal. Often, they possess the heads of great cats (such as a _[[monsters/Tiger|tiger]]_ or panther) or a snake (like a cobra or viper), yet other heads are not _[[monsters/Unknown|unknown]]_—apes, jackals, vultures, elephants, mantises, lizards, rhinos, boars, and more are possible. In most cases, the type of head a _rakshasa_ possesses speaks in some way to its personality—a tiger-headed _rakshasa_ is _[[feats/Stealthy|stealthy]]_ and _[[curses/Ravenous|ravenous]]_, while a boar-headed one might be gluttonous and crude. These changes rarely _[[items/Weapon Magic Abilities/Impact|impact]]_ the _rakshasa_’s base statistics, although there are more powerful variants of the standard _rakshasa_ that possess multiple heads, more _[[items/Weapon Magic Abilities/Potent|potent]]_ spellcasting powers, and additional _[[items/Weapon Magic Abilities/Deadly|deadly]]_ and unusual special abilities.

Rakshasas scoff at religion—they understand the power of the divine, but see themselves as the only thing worthy of worship from the mortal races. _Rakshasa_ clerics are thus quite rare. Although rakshasas are outsiders, they are also very much creatures of the Material Plane, and many believe the first rakshasas chose this exile over some other role offered them by a long-forgotten god. Although they usually work alone, it isn’t unheard of to find extended families of rakshasas working together to ruin a mortal civilization from the inside out over the course of many generations. A _rakshasa_ is 6 feet tall and weighs 180 lbs.