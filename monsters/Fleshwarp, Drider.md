---
cssclass: [monsters]
title1: Fleshwarp, Drider
desc_short: The dry rasping of spidery legs brings this hideous monstrosity into view-a
  nightmarish, centaurian fusion of drow and spider.
title2: Drider
CR: 7
sources:
- name: Pathfinder RPG Bestiary
  page: 113
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 3200
alignment: CE
size: Large
type: aberration
initiative:
  bonus: 2
senses:
  darkvision: 120
  detect good: true
  detect law: true
  detect magic: true
AC:
  AC: 20
  touch: 12
  flat_footed: 17
  components:
    dex: 2
    dodge: 1
    natural: 8
    size: -1
HP:
  HP: 76
  long: 9d8+36
saves:
  fort: 7
  ref: 5
  will: 9
immunities:
- sleep
SR: 18
speeds:
  base: 30
  climb: 20
attacks:
  melee:
  - - text: mwk heavy mace +9/+4 (1d8+3)
      entries:
      - - damage: 1d8+3
      attack: mwk heavy mace
      bonus:
      - 9
      - 4
    - text: bite +3 (1d4+1 plus poison)
      entries:
      - - damage: 1d4+1
        - effect: poison
      attack: bite
      bonus:
      - 3
  ranged:
  - - text: mwk composite longbow +8/+3 (1d8+2/×3)
      entries:
      - - damage: 1d8+2
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 8
      - 3
  special:
  - web (+7 ranged, DC 18, hp 9)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: dancing lights
    source: default
    freq: At will
  - name: darkness
    source: default
    freq: At will
  - name: faerie fire
    source: default
    freq: At will
  - name: clairaudience/clairvoyance
    source: default
    freq: 1/day
  - name: deeper darkness
    source: default
    freq: 1/day
  - name: dispel magic
    source: default
    freq: 1/day
  - name: levitate
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 16
  sources:
  - name: default
    CL: 9
spells:
  entries:
  - name: lightning bolt
    source: '?'
    level: 3
    DC: 16
  - name: invisibility
    source: '?'
    level: 2
  - name: web
    source: '?'
    level: 2
    DC: 15
  - name: mage armor
    source: '?'
    level: 1
  - name: magic missile
    source: '?'
    level: 1
  - name: ray of enfeeblement
    source: '?'
    level: 1
    DC: 14
  - name: silent image
    source: '?'
    level: 1
    DC: 14
  - name: bleed
    source: '?'
    level: 0
    DC: 13
  - name: daze
    source: '?'
    level: 0
    DC: 13
  - name: ghost sound
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: ray of frost
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 6
    slots:
      3: 4
      2: 6
      1: 7
      0: at-will
ability_scores:
  STR: 15
  DEX: 15
  CON: 18
  INT: 15
  WIS: 16
  CHA: 16
BAB: 6
CMB: 9
CMD: 21
CMD_other: 33 vs. trip
feats:
- name: Blind-Fight
- name: Dodge
- name: Combat Casting
- name: Weapon Focus (bite)
- name: Weapon Focus (mace)
skills:
  Climb: 22
  Intimidate: 15
  Knowledge (arcana): 14
  Perception: 15
  Spellcraft: 14
  Stealth: 14
  _racial_mods:
    Stealth:
      _: 4
languages:
- Common
- Elven
- Undercommon
special_qualities:
- undersized weapons
ecology:
  environment: any underground
  organization: solitary, pair, or group (3-8)
  treasure_type: double
  treasure:
  - masterwork heavy mace
  - masterwork composite longbow [+2 Str] with 20 arrows
  - additional treasure
special_abilities:
  Poison (Ex): Bite-injury; save Fort DC 18; frequency 1/round for 6 rounds; effect
    1d2 Str; cure 1 save. The save DC is Constitution-based.
  Spells: A drider casts spells as a 6th-level cleric, sorcerer, or wizard, but does
    not gain any other class abilities.
  Undersized Weapons (Ex): Although a drider is Large, its upper torso is the same
    size as that of a Medium humanoid's upper torso. As a result, it wields weapons
    as if it were one size category smaller than its actual size (Medium for most
    driders).
desc_long: |-
  Created from the body of a drow, warped and mutated through special poisons and elixirs to take on the characteristics of a giant spider, the drider is a dangerous creature.

  Driders are sexually dimorphic. A female drider's lower spider body is sleek and graceful, often similar to a black widow's body, while its upper drow torso retains its alluring curves and beautiful face (with the exception of sharp, poisonous fangs). A male drider's lower body is bulky like a tarantula, while its upper body is wiry and bears a hideous face more spider than drow, complete with fanged mandibles.

---

# Fleshwarp, Drider
The dry rasping of spidery legs brings this hideous monstrosity into view—a nightmarish, centaurian fusion of _[[monsters/Drow|drow]]_ and spider.
**Source** Pathfinder RPG Bestiary pg. 113
**XP** 3,200
CE Large aberration
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/Detect Magic|detect magic]]_; Perception +15

##### Defense

**AC** 20, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+2 Dex, +1 dodge, +8 natural, –1 size)
**hp** 76 (9d8+36)
**Fort** +7, **Ref** +5, **Will** +9
**Immune** sleep; **SR** 18

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** mwk _[[items/Weapon/Heavy mace|heavy mace]]_ +9/+4 (1d8+3), bite +3 (1d4+1 plus poison)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +8/+3 (1d8+2/×3)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** web (+7 ranged, DC 18, hp 9)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th)
Constant—_detect good_, _detect law_, _detect magic_
At will—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Darkness|darkness]]_, _[[spells/Faerie Fire|faerie fire]]_
1/day—clairaudience/clairvoyance, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Levitate|levitate]]_, _[[spells/Suggestion|suggestion]]_ (DC 16)
**Spells Known **(CL 6th)
3rd (4/day)—_[[spells/Lightning Bolt|lightning bolt]]_ (DC 16)
2nd (6/day)—_[[spells/Invisibility|invisibility]]_, web (DC 15)
1st (7/day)—_[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 14), _[[spells/Silent Image|silent image]]_ (DC 14)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Daze|daze]]_ (DC 13), _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 15, **Dex** 15, **Con** 18, **Int** 15, **Wis** 16, **Cha** 16
**Base Atk** +6; **CMB** +9; **CMD** 21 (33 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _Dodge_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite, mace)
**Skills** _Climb_ +22, Intimidate +15, Knowledge (arcana) +14, Perception +15, Spellcraft +14, Stealth +14; **Racial Modifiers** +4 Stealth
**Languages** Common, Elven, Undercommon
**SQ** _[[universal monster rules/Undersized Weapons|undersized weapons]]_

##### Ecology

**Environment** any underground
**Organization** solitary, pair, or group (3–8)
**Treasure** double (masterwork _heavy mace_, masterwork _composite longbow_ [+2 Str] with 20 arrows, additional treasure)

### Special Abilities

**Poison (Ex)** Bite—injury; save Fort DC 18; frequency 1/round for 6 rounds; effect 1d2 Str; cure 1 save. The save DC is Constitution-based.
**Spells **A drider casts spells as a 6th-level _[[classes/Cleric|cleric]]_, _[[classes/Sorcerer|sorcerer]]_, or _[[classes/Wizard|wizard]]_, but does not gain any other class abilities.

**_Undersized Weapons_ (Ex)** Although a drider is Large, its upper torso is the same size as that of a _[[classes/Medium|Medium]]_ humanoid’s upper torso. As a result, it wields weapons as if it were one size category smaller than its actual size (_Medium_ for most driders).

##### Description

Created from the body of a _drow_, warped and mutated through special poisons and elixirs to take on the characteristics of a giant spider, the drider is a dangerous creature.

Driders are sexually dimorphic. A female drider’s lower spider body is sleek and graceful, often similar to a black widow’s body, while its upper _drow_ torso retains its alluring curves and beautiful face (with the exception of sharp, poisonous fangs). A male drider’s lower body is bulky like a tarantula, while its upper body is wiry and bears a hideous face more spider than _drow_, complete with fanged mandibles.