---
cssclass: [monsters]
title1: Blight, Tundra Blight
desc_short: This churning mound of snow-like material has several large red eyes and
  four tentacles tipped with icy stingers.
title2: Tundra Blight
CR: 16
sources:
- name: Bestiary 6
  page: 45
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 76800
alignment: NE
size: Medium
type: ooze
subtypes:
- blight
- cold
initiative:
  bonus: 14
senses:
  blindsight: 120
AC:
  AC: 32
  touch: 21
  flat_footed: 21
  components:
    dex: 10
    dodge: 1
    natural: 11
HP:
  HP: 243
  long: 18d8+162
  fast_healing: 15
saves:
  fort: 15
  ref: 18
  will: 14
defensive_abilities:
- rejuvenation
immunities:
- acid
- cold
- ooze traits
weaknesses:
- vulnerable to fire
speeds:
  base: 30
  burrow: 30
  burrow_other: snow and ice only
  climb: 30
attacks:
  melee:
  - - text: 4 stings +26 (1d8+13 plus 1d6 cold and curse)
      entries:
      - - damage: 1d8+13
        - damage: 1d6
          type: cold
        - effect: curse
      count: 4
      attack: stings
      bonus:
      - 26
  special:
  - creeping cold
  - curse of winter
  - frozen domain
space: 5
reach: 15
spell_like_abilities:
  entries:
  - name: blight
    source: default
    freq: 1/day
    DC: 22
  - name: command plants
    source: default
    freq: 1/day
    DC: 21
  - name: cone of cold
    source: default
    freq: 1/day
    DC: 22
  - name: dominate monster
    source: default
    freq: 1/day
    other: animals and magical beasts only
    DC: 26
  - name: greater curse terrain
    source: default
    freq: 1/day
  - name: hallucinatory terrain
    source: default
    freq: 1/day
    DC: 21
  sources:
  - name: default
    CL: 16
    concentration: 23
ability_scores:
  STR: 36
  DEX: 30
  CON: 29
  INT: 17
  WIS: 23
  CHA: 24
BAB: 13
CMB: 26
CMD: 47
CMD_other: can't be tripped
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Power Attack
- name: Spring Attack
skills:
  Climb: 39
  Intimidate: 25
  Knowledge (geography): 21
  Perception: 24
  Stealth: 28
    in ice or snow: 36
  _racial_mods:
    Stealth:
      in ice or snow: 8
languages:
- Aklo
- Auran
- domain telepathy
special_qualities:
- cursed domain
- favored terrain (cold)
- icewalking
ecology:
  environment: cold plains or glaciers
  organization: solitary
  treasure_type: standard
special_abilities:
  Creeping Cold (Su): A tundra blight's stings deal an additional 1d6 points of cold
    damage. In addition, this cold clings to the target and continues to deal an additional
    1d6 points of cold damage each round at the start of the affected creature's turn.
    This creeping cold effect can be stopped by a successful DC 15 Heal check or through
    the application of any magical healing. This additional cold damage does not stack
    with multiple stings.
  Curse of Winter (Su): A creature struck by a tundra blight's sting attack must succeed
    at a DC 26 Will save or gain vulnerability to cold. Creatures immune to cold damage
    that fail this save do not become vulnerable, but are instead no longer immune
    to cold (they cannot then be made vulnerable to cold from this curse, as its effects
    do not stack in this manner). This curse persists until it is removed. This is
    a cold curse effect. The save DC is Charisma-based.
  Frozen Domain (Su): A tundra blight's domain is always treated as being one category
    colder than the region would otherwise dictate (see page 442 of the Pathfinder
    RPG Core Rulebook). If a region is normally treated as extreme cold, it deals
    1d6 points of lethal damage per round of exposure instead of per minute. Anyone
    attempting a saving throw against the effects of these cold temperatures or a
    saving throw against cold effects takes a -4 penalty on the save within a tundra
    blight's frozen domain. When a character attempts to cast any spell with the fire
    descriptor in this domain, she must succeed at a DC 30 caster level check or the
    spell is negated when it is cast.
  Icewalking (Ex): A tundra blight can navigate icy surfaces as if under the effect
    of spider climb. It can move across icy surfaces without penalty and does not
    need to attempt Acrobatics checks to run or charge on ice.
desc_long: |-
  Tundra blights dwell in the frozen reaches of the world, bringing their freezing domains to borderland settlements. 

  Tundra blights are 7 feet across and weight 450 pounds.

---

# Blight, Tundra Blight
This churning mound of snow-like material has several large red eyes and four tentacles tipped with icy stingers.
**Source** Bestiary 6 pg. 45
**XP** 76,800

NE Medium ooze (_[[spells/Blight|blight]]_, cold)
**Init** +14; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 120 ft.; Perception +24

##### Defense

**AC** 32, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+10 Dex, +1 _[[feats/Dodge|dodge]]_, +11 natural)
**hp** 243 (18d8+162); _[[universal monster rules/Fast Healing|fast healing]]_ 15
**Fort** +15, **Ref** +18, **Will** +14
**Defensive Abilities** rejuvenation; **Immune** acid, cold, ooze traits
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 30 ft. (snow and ice only), _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** 4 stings +26 (1d8+13 plus 1d6 cold and curse)
**Space** 5 ft., **Reach** 15 ft.
**Special Attacks** _[[items/Armor Magic Abilities/Creeping|creeping]]_ cold, curse of winter, frozen domain
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +23)
1/day—_blight_ (DC 22), _[[spells/Command Plants|command plants]]_ (DC 21), _[[spells/Cone of Cold|cone of cold]]_ (DC 22), _[[spells/Dominate Monster|dominate monster]]_ (animals and magical beasts only, DC 26), greater _[[spells/Curse Terrain|curse terrain]]_, _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 21)

##### Statistics
**Str** 36, **Dex** 30, **Con** 29, **Int** 17, **Wis** 23, **Cha** 24
**Base Atk** +13; **CMB** +26; **CMD** 47 (can’t be tripped)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_
**Skills** _Climb_ +39, Intimidate +25, Knowledge (geography) +21, Perception +24, Stealth +28 (+36 in ice or snow); Racial Modifiers +8 Stealth in ice or snow
**Languages** Aklo, Auran; domain _[[universal monster rules/Telepathy|telepathy]]_
**SQ** cursed domain, favored terrain (cold), icewalking

##### Ecology

**Environment** cold plains or glaciers
**Organization** solitary
**Treasure** standard

### Special Abilities

**_Creeping_ Cold (Su)** A tundra _blight_’s stings deal an additional 1d6 points of cold damage. In addition, this cold clings to the target and continues to deal an additional 1d6 points of cold damage each round at the start of the affected creature’s turn. This _creeping_ cold effect can be stopped by a successful DC 15 _[[spells/Heal|Heal]]_ check or through the application of any magical healing. This additional cold damage does not stack with multiple stings.

**Curse of Winter (Su)** A creature struck by a tundra _blight_’s sting attack must succeed at a DC 26 Will save or gain _[[curses/Vulnerability|vulnerability]]_ to cold. Creatures immune to cold damage that fail this save do not become vulnerable, but are instead no longer immune to cold (they cannot then be made vulnerable to cold from this curse, as its effects do not stack in this manner). This curse persists until it is removed. This is a cold curse effect. The save DC is Charisma-based.

**Frozen Domain (Su)** A tundra _blight_’s domain is always treated as being one category colder than the region would otherwise dictate (see page 442 of the Pathfinder RPG Core Rulebook). If a region is normally treated as extreme cold, it deals 1d6 points of lethal damage per round of exposure instead of per minute. Anyone attempting a saving throw against the effects of these cold temperatures or a saving throw against cold effects takes a –4 penalty on the save within a tundra _blight_’s frozen domain. When a character attempts to cast any spell with the fire descriptor in this domain, she must succeed at a DC 30 caster level check or the spell is negated when it is cast.

**Icewalking (Ex)** A tundra _blight_ can navigate icy surfaces as if under the effect of _[[spells/Spider Climb|spider climb]]_. It can move across icy surfaces without penalty and does not need to attempt Acrobatics checks to run or charge on ice.

##### Description

Tundra blights dwell in the frozen reaches of the world, bringing their freezing domains to borderland settlements.

Tundra blights are 7 feet across and weight 450 pounds.