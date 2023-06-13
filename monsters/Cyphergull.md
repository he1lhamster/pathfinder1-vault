---
cssclass: [monsters]
title1: Cyphergull
desc_short: The eyes of this large gull glow eerily blue. Gray feathers cover much
  of its robust body, and its long, black-tipped wings are marked with enigmatic symbols.
  The bird's yellow bill is heavy and hooked, and its webbed feet bear sharp talons.
title2: Cyphergull
CR: 2
sources:
- name: "Pathfinder #133: Secrets of Roderic's Cove"
  page: 82
  link: http://paizo.com/products/btpy9y26?Pathfinder-Adventure-Path-133-Secrets-of-Rodericks-Cove
XP: 600
alignment: N
size: Tiny
type: magical beast
initiative:
  bonus: 3
senses:
  arcane sight: true
  darkvision: 60
  low-light vision: true
AC:
  AC: 15
  touch: 15
  flat_footed: 12
  components:
    dex: 3
    size: 2
HP:
  HP: 19
  long: 3d10+3
saves:
  fort: 4
  ref: 6
  will: 4
speeds:
  base: 10
  fly: 50
  fly_maneuverability: good
  swim: 10
attacks:
  melee:
  - - text: bite +3 (1d4-1)
      entries:
      - - damage: 1d4-1
      attack: bite
      bonus:
      - 3
    - text: 2 talons +3 (1d3-1)
      entries:
      - - damage: 1d3-1
      count: 2
      attack: talons
      bonus:
      - 3
  special:
  - arcane attacks
  - natural thief
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - name: arcane sight
    source: default
    freq: Constant
  - name: read magic
    source: default
    freq: Constant
  - name: arcane mark
    source: default
    freq: At will
  sources:
  - name: default
    CL: 3
    concentration: 2
ability_scores:
  STR: 6
  DEX: 17
  CON: 13
  INT: 6
  WIS: 13
  CHA: 8
BAB: 3
CMB: 4
CMD: 12
feats:
- name: Flyby Attack
- name: Iron Will
skills:
  Acrobatics: 15
  Fly: 15
  Perception: 5
  Swim: 11
  _racial_mods:
    Acrobatics:
      _: 8
languages:
- Common (can't speak)
special_qualities:
- cypher synergy
- devour scroll
ecology:
  environment: temperate coasts
  organization: solitary, pair, flock (3-12), or colony
  treasure_type: incidental
special_abilities:
  Arcane Attacks (Su): A cyphergull's natural weapons have a +1 bonus to damage and
    are treated as magic for the purpose of overcoming damage reduction. For every
    5 Hit Dice the cyphergull has, this bonus increases by 1.
  Cypher Synergy (Ex): 'If the master of a cyphergull familiar is a cyphermage, the
    cyphergull gains the following cypher lore discoveries if its master has them:
    analyze scroll, bypass symbol, defensive scrollcaster, and glyph finder. Defensive
    scrollcaster affects spells the cyphergull casts using its devour scroll ability.'
  Devour Scroll (Su): When a cyphergull eats a scroll (a full-round action), the spells
    in the scroll are stored in the gull's body. Thereafter, it can cast the spells
    as though it were a wizard of a level equal to half the cyphergull's Hit Dice
    casting spells from a scroll. The cyphergull intuitively understands how the spells
    function and counts as having the requisite ability score for casting the spell.
    A cyphergull can store a maximum number of spell levels equal to its Hit Dice.
  Natural Thief (Ex): If a cyphergull succeeds at an Acrobatics check to move through
    a threatened square without provoking an attack of opportunity from an enemy,
    the cyphergull also doesn't provoke an attack of opportunity when performing a
    steal combat maneuver against that enemy on the same turn.
desc_long: |-
  The noisy, enigmatic cyphergulls are a common sight in the coastal city of Riddleport, where they often circle above the ancient rune-carved Cyphergate as if they own it. Their appearance and behavior greatly resembles those of their mundane cousins-seagulls-but they are far more intelligent, and their connection to Riddleport's ancient Thassilonian stone arch grants them many magical abilities.

   A cyphergull is a little over 2 feet long, has a wingspan of up to 5 feet, and weighs 3 pounds.

---

# Cyphergull
The eyes of this large gull glow eerily blue. _[[monsters/Gray|Gray]]_ feathers cover much of its robust body, and its long, black-tipped wings are marked with enigmatic symbols. The bird’s yellow _[[items/Weapon/Bill|bill]]_ is heavy and hooked, and its webbed feet bear sharp talons.
**Source** Pathfinder #133: Secrets of Roderic's Cove pg. 82
**XP** 600

N Tiny magical beast
**Init** +3; **Senses** _[[spells/Arcane Sight|arcane sight]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5

##### Defense

**AC** 15, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+3 Dex, +2 size)
**hp** 19 (3d10+3)
**Fort** +4, **Ref** +6, **Will** +4

##### Offense
**Speed** 10 ft., fly 50 ft. (good), swim 10 ft.
**Melee** bite +3 (1d4–1), 2 talons +3 (1d3–1)
**Space** 2-1/2 ft., **Reach** 0 ft.
**Special Attacks** arcane attacks, natural thief
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +2)
Constant—_arcane sight_, _[[spells/Read Magic|read magic]]_
At will—_[[spells/Arcane Mark|arcane mark]]_

##### Statistics
**Str** 6, **Dex** 17, **Con** 13, **Int** 6, **Wis** 13, **Cha** 8
**Base Atk** +3; **CMB** +4; **CMD** 12
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Iron Will|Iron Will]]_
**Skills** Acrobatics +15, Fly +15, Perception +5, Swim +11; **Racial Modifiers** +8 Acrobatics
**Languages** Common (can't speak)
**SQ** cypher synergy, devour scroll

##### Ecology

**Environment** temperate coasts
**Organization** solitary, pair, flock (3-12), or colony
**Treasure** incidental

### Special Abilities

**Arcane Attacks (Su)** A _[[monsters/Cyphergull|cyphergull]]_'s natural weapons have a +1 bonus to damage and are treated as magic for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_. For every 5 Hit Dice the _cyphergull_ has, this bonus increases by 1.

**Cypher Synergy (Ex)** If the master of a _cyphergull_ familiar is a _[[npcs/Cyphermage|cyphermage]]_, the _cyphergull_ gains the following cypher lore discoveries if its master has them: analyze scroll, bypass symbol, defensive scrollcaster, and glyph finder. Defensive scrollcaster affects spells the _cyphergull_ casts using its devour scroll ability.

**Devour Scroll (Su)** When a _cyphergull_ eats a scroll (a full-round action), the spells in the scroll are stored in the gull's body. Thereafter, it can cast the spells as though it were a _[[classes/Wizard|wizard]]_ of a level equal to half the _cyphergull_'s Hit Dice casting spells from a scroll. The _cyphergull_ intuitively understands how the spells function and counts as having the requisite ability score for casting the spell. A _cyphergull_ can store a maximum number of spell levels equal to its Hit Dice.

**Natural Thief (Ex)** If a _cyphergull_ succeeds at an Acrobatics check to move through a threatened square without provoking an attack of opportunity from an enemy, the _cyphergull_ also doesn't provoke an attack of opportunity when performing a steal combat maneuver against that enemy on the same turn.

##### Description

The noisy, enigmatic cyphergulls are a common sight in the coastal city of Riddleport, where they often circle above the ancient rune-carved Cyphergate as if they own it. Their appearance and behavior greatly resembles those of their mundane cousins—seagulls—but they are far more intelligent, and their connection to Riddleport’s ancient Thassilonian stone arch grants them many magical abilities.

A _cyphergull_ is a little over 2 feet long, has a wingspan of up to 5 feet, and weighs 3 pounds.