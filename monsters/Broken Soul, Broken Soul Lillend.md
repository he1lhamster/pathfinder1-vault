---
cssclass: [monsters]
title1: Broken Soul, Broken Soul Lillend
desc_short: Once a beautiful celestial with the torso of a winged woman and a snakelike
  body below, this creature is a mess of blood and scars.
title2: Broken Soul Lillend
CR: 9
sources:
- name: Bestiary 4
  page: 24
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 6400
alignment: CE
size: Large
type: outsider
subtypes:
- azata
- chaotic
- extraplanar
- evil
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 24
  touch: 12
  flat_footed: 21
  components:
    dex: 3
    natural: 12
    size: -1
HP:
  HP: 101
  long: 7d10+63
saves:
  fort: 12
  ref: 10
  will: 6
DR:
- amount: 5
  weakness: '-'
immunities:
- electricity
- petrification
- poison
resistances:
  acid: 5
  cold: 10
  fire: 10
  sonic: 5
speeds:
  base: 20
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: +1 longsword +12/+7 (2d6+8/19-20)
      entries:
      - - damage: 2d6+8
          crit_range: 19-20
      attack: +1 longsword
      bonus:
      - 12
      - 7
    - text: tail slap +6 (2d6+2 plus grab)
      entries:
      - - damage: 2d6+2
        - effect: grab
      attack: tail slap
      bonus:
      - 6
  - - text: torturous touch +11 touch (2d6 plus 1d6 Dex damage and convulsions)
      entries:
      - - damage: 2d6
        - damage: 1d6
          type: Dex damage
        - effect: convulsions
      attack: torturous touch
      bonus:
      - 11
      touch: true
    - text: tail slap +6 (2d6+2 plus grab)
      entries:
      - - damage: 2d6+2
        - effect: grab
      attack: tail slap
      bonus:
      - 6
  special:
  - agonized wail (DC 18)
  - baleful gaze (DC 18)
  - bardic performance (21 rounds/day)
  - constrict (2d6+5)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: darkness
    source: default
    freq: 3/day
  - name: hallucinatory terrain
    source: default
    freq: 3/day
    DC: 19
  - name: knock
    source: default
    freq: 3/day
  - name: light
    source: default
    freq: 3/day
  - name: charm person
    source: default
    freq: 1/day
    DC: 16
  - name: speak with animals
    source: default
    freq: 1/day
  - name: speak with plants
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 7
    concentration: 2
spells:
  entries:
  - name: crushing despair
    source: Bard
    level: 3
    DC: 18
  - superscripts:
    - UM
    name: terrible remorse
    source: Bard
    level: 3
    DC: 18
  - name: blindness/deafness
    source: Bard
    level: 2
    DC: 17
  - superscripts:
    - UM
    name: piercing shriek
    source: Bard
    level: 2
    DC: 17
  - name: rage
    source: Bard
    level: 2
  - name: suggestion
    source: Bard
    level: 2
    DC: 17
  - name: cause fear
    source: Bard
    level: 1
    DC: 16
  - name: charm person
    source: Bard
    level: 1
    DC: 16
  - superscripts:
    - UM
    name: ear-piercing scream
    source: Bard
    level: 1
    DC: 16
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 16
  - name: lesser confusion
    source: Bard
    level: 1
    DC: 16
  - name: dancing lights
    source: Bard
    level: 0
  - name: daze
    source: Bard
    level: 0
    DC: 15
  - name: detect magic
    source: Bard
    level: 0
  - name: ghost sound
    source: Bard
    level: 0
    DC: 15
  - name: read magic
    source: Bard
    level: 0
  - name: resistance
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 7
    concentration: 2
    slots:
      3: 2
      2: 4
      1: 6
      0: at-will
ability_scores:
  STR: 20
  DEX: 17
  CON: 27
  INT: 14
  WIS: 8
  CHA: 21
BAB: 7
CMB: 13
CMB_other: +17 grapple
CMD: 26
CMD_other: can't be tripped
feats:
- name: Combat Casting
- is_bonus: true
  name: Diehard
- is_bonus: true
  name: Endurance
- is_bonus: true
  name: Great Fortitude
- name: Hover
- name: Iron Will
- name: Lightning Reflexes
- is_bonus: true
  name: Toughness
skills:
  Bluff: 15
  Fly: 11
  Intimidate: 13
  Knowledge (nature): 9
  Perception: 9
  Perform (string): 17
  Sense Motive: 9
  Stealth: 9
  Survival: 10
  _racial_mods:
    Intimidate:
      _: 8
    Survival:
      _: 4
languages:
- Celestial
- Draconic
- Infernal
- truespeech
ecology:
  environment: any
  organization: solitary
  treasure_type: standard
  treasure:
  - +1 longsword
  - masterwork harp
  - other treasure
special_abilities:
  Bardic Performance: A lillend has the bardic performance ability of a 7th-level
    bard, granting her access to the countersong, fascinate, inspire courage, inspire
    competence, and suggestion aspects of bardic performance.
  Spells: A lillend casts spells as a 7th-level bard.
desc_long: |-
  A broken soul is torment and pain made manifest. Tortured to the extremes of both physical and mental endurance, and then taken beyond those barriers, a broken soul gains extraordinary reserves of fortitude and resilience as well as the ability to inflict a measure of its own terrible suffering on others.

  Each broken soul has a unique appearance, the torture it has endured plainly visible on its body. Its skin is a mass of scar tissue, marred with bruises that do not fade and scored with countless scars. In some cases, a broken soul's flesh has been flayed away, revealing the musculature and bone underneath. Weeping sores and open cuts cover a broken soul's body, wounds that never fully heal. Its limbs are often twisted, the result of broken bones that were never set properly, and it might be missing fingers, toes, ears, or other appendages. A broken soul's existence is one of unending suffering, and the constant pain often drives the creature irrevocably mad. In their insanity, these unfortunates hate all other creatures and seek to inflict their wounds and their agony on all they encounter.

  The creation of a broken soul can happen in a number of ways. Some broken souls arise spontaneously, the result of horrific treatment at the hands of cruel abusers. With no way to escape their torment, these creatures embrace the pain and anguish and transcend them, making them a part of their very being. In so doing, they become something both more and less than they were. Other broken souls are purposefully created out of helpless prisoners by sadistic torturers through a harrowing gauntlet of mental and physical torments. By breaking a creature's mind and body, these torturers hope to create guardians or servants whose loyalty is ensured by the constant pain they must endure. Even more harrowing, some broken souls take it upon themselves to create more of their kind, fashioning gruesome works of living, mutilated art in an effort to share their suffering. These “artists” often turn on their own torturers first, perfecting their skills on those who created them before turning their attention to any other unfortunate creatures they can find.

---

# Broken Soul, Broken Soul Lillend
Once a beautiful celestial with the torso of a winged woman and a snakelike body below, this creature is a mess of blood and scars.
**Source** Bestiary 4 pg. 24
**XP** 6,400
CE Large outsider (azata, chaotic, extraplanar, evil)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9

##### Defense

**AC** 24, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+3 Dex, +12 natural, –1 size)
**hp** 101 (7d10+63)
**Fort** +12, **Ref** +10, **Will** +6
**DR** 5/—; **Immune** electricity, petrification, poison; **Resist** acid 5, cold 10, fire 10, sonic 5

##### Offense
**Speed** 20 ft., fly 60 ft. (average)
**Melee** +1 _[[items/Weapon/Longsword|longsword]]_ +12/+7 (2d6+8/19–20), tail slap +6 (2d6+2 plus _[[universal monster rules/Grab|grab]]_) or torturous touch +11 touch (2d6 plus 1d6 Dex damage and convulsions), tail slap +6 (2d6+2 plus _grab_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** agonized wail (DC 18), baleful _[[universal monster rules/Gaze|gaze]]_ (DC 18), bardic performance (21 rounds/day), _[[universal monster rules/Constrict|constrict]]_ (2d6+5)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +2)
3/day—_[[spells/Darkness|darkness]]_, _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 19), _[[spells/Knock|knock]]_, light
1/day—_[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Speak with Animals|speak with animals]]_, _[[spells/Speak with Plants|speak with plants]]_
**_[[classes/Bard|Bard]]_ Spells Known **(CL 7th; concentration +2)
3rd (2/day)—_[[spells/Crushing Despair|crushing despair]]_ (DC 18), _[[spells/Terrible Remorse|terrible remorse]]_ (DC 18)
2nd (4/day)—blindness/deafness (DC 17), _[[spells/Piercing Shriek|piercing shriek]]_ (DC 17), _[[spells/Rage|rage]]_, _[[spells/Suggestion|suggestion]]_ (DC 17)
1st (6/day)—_[[spells/Cause Fear|cause fear]]_ (DC 16), _charm person_ (DC 16), _[[spells/Ear-Piercing Scream|ear-piercing scream]]_ (DC 16), _[[spells/Hideous Laughter|hideous laughter]]_ (DC 16), lesser _[[spells/Confusion|confusion]]_ (DC 16)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 15), _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 20, **Dex** 17, **Con** 27, **Int** 14, **Wis** 8, **Cha** 21
**Base Atk** +7; **CMB** +13 (+17 grapple); **CMD** 26 (can’t be tripped)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Diehard|Diehard]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Hover|Hover]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Toughness|Toughness]]_
**Skills** Bluff +15, Fly +11, Intimidate +13, Knowledge (nature) +9, Perception +9, Perform (string) +17, Sense Motive +9, Stealth +9, Survival +10; **Racial Modifiers** +8 Intimidate, +4 Survival
**Languages** Celestial, Draconic, Infernal; truespeech

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** standard (+1 _longsword_, masterwork harp, other treasure)

### Special Abilities

**Bardic Performance** A lillend has the bardic performance ability of a 7th-level _bard_, granting her access to the countersong, fascinate, inspire courage, inspire competence, and _suggestion_ aspects of bardic performance.
**Spells** A lillend casts spells as a 7th-level _bard_.

##### Description

A _[[conditions/Broken|broken]]_ soul is torment and pain made manifest. Tortured to the extremes of both physical and mental _endurance_, and then taken beyond those barriers, a _broken_ soul gains extraordinary reserves of fortitude and resilience as well as the ability to inflict a measure of its own terrible suffering on others.

Each _broken_ soul has a unique appearance, the torture it has endured plainly visible on its body. Its skin is a mass of scar tissue, marred with bruises that do not fade and scored with countless scars. In some cases, a _broken_ soul’s flesh has been flayed away, revealing the musculature and bone underneath. _[[items/Armor Magic Abilities/Weeping|Weeping]]_ sores and open cuts cover a _broken_ soul’s body, wounds that never fully _[[spells/Heal|heal]]_. Its limbs are often twisted, the result of _broken_ bones that were never set properly, and it might be missing fingers, toes, ears, or other appendages. A _broken_ soul’s existence is one of unending suffering, and the constant pain often drives the creature irrevocably mad. In their _[[spells/Insanity|insanity]]_, these unfortunates hate all other creatures and seek to inflict their wounds and their agony on all they encounter.

The creation of a _broken_ soul can happen in a number of ways. Some _broken_ souls arise spontaneously, the result of horrific treatment at the hands of _[[items/Weapon Magic Abilities/Cruel|cruel]]_ abusers. With no way to escape their torment, these creatures embrace the pain and anguish and transcend them, making them a part of their very being. In so doing, they become something both more and less than they were. Other _broken_ souls are purposefully created out of _[[conditions/Helpless|helpless]]_ prisoners by sadistic torturers through a _[[spells/Harrowing|harrowing]]_ _[[items/Weapon/Gauntlet|gauntlet]]_ of mental and physical torments. By _[[items/Weapon Magic Abilities/Breaking|breaking]]_ a creature’s mind and body, these torturers hope to create guardians or servants whose loyalty is ensured by the constant pain they must endure. Even more _harrowing_, some _broken_ souls take it upon themselves to create more of their kind, fashioning gruesome works of living, mutilated art in an effort to share their suffering. These “artists” often turn on their own torturers first, perfecting their skills on those who created them before turning their attention to any other unfortunate creatures they can find.