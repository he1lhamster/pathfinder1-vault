---
cssclass: [monsters]
title1: Yuki-Onna
desc_short: This beautiful but sad-looking woman wears an ornate robe and is surrounded
  by a whirling mass of snow.
title2: Yuki-Onna
CR: 8
sources:
- name: Bestiary 3
  page: 287
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 4800
alignment: LE
size: Medium
type: undead
subtypes:
- cold
- incorporeal
initiative:
  bonus: 8
senses:
  darkvision: 60
auras:
- name: snowstorm
  radius: 200
AC:
  AC: 21
  touch: 21
  flat_footed: 16
  components:
    deflection: 6
    dex: 4
    dodge: 1
HP:
  HP: 94
  long: 9d8+54
saves:
  fort: 9
  ref: 7
  will: 11
defensive_abilities:
- incorporeal
immunities:
- cold
- undead traits
weaknesses:
- vulnerable to fire
- snow dependency
speeds:
  fly: 30
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 touches +10 (4d6 cold plus chilling touch)
      entries:
      - - damage: 4d6
          type: cold
        - effect: chilling touch
      count: 2
      attack: touches
      bonus:
      - 10
  special:
  - chilling touch
  - fascinating gaze
spell_like_abilities:
  entries:
  - name: blur
    source: default
    freq: Constant
  - name: cone of cold
    source: default
    freq: 3/day
    DC: 21
  - name: eyebite
    source: default
    freq: 3/day
    other: comatose and panicked only
    DC: 22
  - name: ice storm
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 10
    concentration: 16
ability_scores:
  STR:
  DEX: 18
  CON:
  INT: 17
  WIS: 21
  CHA: 22
BAB: 6
CMB: 10
CMD: 27
feats:
- name: Combat Casting
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Spring Attack
skills:
  Bluff: 15
  Fly: 12
  Intimidate: 18
  Perception: 17
  Sense Motive: 17
  Spellcraft: 15
  Stealth: 16
  Survival: 14
languages:
- Common
ecology:
  environment: any cold
  organization: solitary
  treasure_type: standard
special_abilities:
  Chilling Touch (Su): A yuki-onna's touch causes 4d6 cold damage. Whenever a creature
    takes cold damage in this manner, it must make a DC 20 Fortitude save to avoid
    being staggered by the supernatural cold for 1 round. This duration stacks. The
    save DC is Charisma-based.
  Fascinating Gaze (Su): Fascinated for 1d4 rounds, 30 feet, Will DC 20 negates. The
    save DC is Charisma-based.
  Snow Dependency (Ex): A yuki-onna is staggered if she is ever in an area without
    snow while her snowstorm aura is suppressed or otherwise not functioning.
  Snowstorm (Su): A yuki-onna is surrounded by whirling blasts of snow, even in areas
    that wouldn't allow for such weather, that comprise a 200-foot-radius spread.
    Within this area, the snowfall and wind gusts cause a -4 penalty on Perception
    checks and ranged attacks. The wind itself blows in a clockwise rotation around
    the yuki-onna, and functions as severe wind (Core Rulebook 439). A yuki-onna is
    unaffected by snowstorms or blizzards of any kind. Any effect that causes these
    winds to drop below severe (such as control weather or control winds) cancels
    the snowstorm effect entirely.
desc_long: |-
  A yuki-onna is the restless spirit of a woman who froze to death in the snow and was never given a proper burial. She roams the wilderness, constantly searching for intelligent creatures to kill and always appearing surrounded by swirling mists of snow and ice. Eternally jaded by her unjust departure to the afterlife, a yuki-onna seeks to impose the same cruel fate upon those who still live, particularly men and those who sympathize or cooperate with them. Many foolish individuals are lured to their deaths by a yuki-onna's unparalleled beauty, which remains even as the evil spirit steadily freezes and kills her victims with her powers over frost.

  The transition from life to undeath corrupts a yuki-onna's soul, and even a well-intentioned, good-hearted individual who freezes in the snow may become a treacherous yuki-onna. Most yuki-onnas immediately seek out those who wronged them in life, after which they reside in an area near what was their home, haunting and killing anyone who dares to come near. Yuki-onnas hardly ever make their presences known in rural areas with larger populations, and they prefer inhabiting the countryside and wilderness.

  When a yuki-onna is destroyed, her body melts as though ice, leaving only a small pool of water in its stead. A yuki-onna is 5-1/2 feet tall.

---

# Yuki-Onna
This beautiful but sad-looking woman wears an ornate robe and is surrounded by a whirling mass of snow.
**Source** Bestiary 3 pg. 287
**XP** 4,800

LE Medium undead (cold, _[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +17
**Aura** snowstorm (200 ft.)

##### Defense

**AC** 21, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 _[[spells/Deflection|deflection]]_, +4 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 94 (9d8+54)
**Fort** +9, **Ref** +7, **Will** +11
**Defensive Abilities** _incorporeal_; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_
**Weaknesses** vulnerable to fire, snow dependency

##### Offense
**Speed** fly 30 ft. (perfect)
**Melee** 2 touches +10 (4d6 cold plus chilling touch)
**Special Attacks** chilling touch, fascinating _[[universal monster rules/Gaze|gaze]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +16)
Constant—_[[spells/Blur|blur]]_
3/day—_[[spells/Cone of Cold|cone of cold]]_ (DC 21), _[[spells/Eyebite|eyebite]]_ (comatose and _[[conditions/Panicked|panicked]]_ only, DC 22), _[[spells/Ice Storm|ice storm]]_

##### Statistics
**Str** —, **Dex** 18, **Con** —, **Int** 17, **Wis** 21, **Cha** 22
**Base Atk** +6; **CMB** +10; **CMD** 27
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_
**Skills** Bluff +15, Fly +12, Intimidate +18, Perception +17, Sense Motive +17, Spellcraft +15, Stealth +16, Survival +14
**Languages** Common

##### Ecology

**Environment** any cold
**Organization** solitary
**Treasure** standard

### Special Abilities

**Chilling Touch (Su)** A _[[monsters/Yuki-Onna|yuki-onna]]_’s touch causes 4d6 cold damage. Whenever a creature takes cold damage in this manner, it must make a DC 20 Fortitude save to avoid being _[[conditions/Staggered|staggered]]_ by the supernatural cold for 1 round. This duration stacks. The save DC is Charisma-based.

**Fascinating _Gaze_ (Su)** _[[conditions/Fascinated|Fascinated]]_ for 1d4 rounds, 30 feet, Will DC 20 negates. The save DC is Charisma-based.
**Snow Dependency (Ex)** A _yuki-onna_ is _staggered_ if she is ever in an area without snow while her snowstorm aura is suppressed or otherwise not functioning.
**Snowstorm (Su)** A _yuki-onna_ is surrounded by whirling blasts of snow, even in areas that wouldn’t allow for such weather, that comprise a 200-foot-radius spread. Within this area, the snowfall and wind gusts cause a –4 penalty on Perception checks and ranged attacks. The wind itself blows in a clockwise rotation around the _yuki-onna_, and functions as severe wind (Core Rulebook 439). A _yuki-onna_ is unaffected by snowstorms or blizzards of any kind. Any effect that causes these winds to drop below severe (such as _[[spells/Control Weather|control weather]]_ or _[[spells/Control Winds|control winds]]_) cancels the snowstorm effect entirely.

##### Description

A _yuki-onna_ is the restless spirit of a woman who froze to death in the snow and was never given a proper burial. She roams the wilderness, constantly searching for intelligent creatures to kill and always appearing surrounded by swirling mists of snow and ice. Eternally jaded by her unjust departure to the afterlife, a _yuki-onna_ seeks to impose the same _[[items/Weapon Magic Abilities/Cruel|cruel]]_ fate upon those who still live, particularly men and those who sympathize or cooperate with them. Many foolish individuals are lured to their deaths by a _yuki-onna_’s unparalleled beauty, which remains even as the evil spirit steadily freezes and kills her victims with her powers over frost.

The transition from life to undeath corrupts a _yuki-onna_’s soul, and even a well-intentioned, good-hearted individual who freezes in the snow may become a treacherous _yuki-onna_. Most yuki-onnas immediately seek out those who wronged them in life, after which they reside in an area near what was their home, haunting and killing anyone who dares to come near. Yuki-onnas hardly ever make their presences known in rural areas with larger populations, and they prefer inhabiting the countryside and wilderness.

When a _yuki-onna_ is destroyed, her body melts as though ice, leaving only a small pool of water in its stead. A _yuki-onna_ is 5-1/2 feet tall.