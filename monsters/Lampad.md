---
cssclass: [monsters]
title1: Lampad
desc_short: Tears stream from this beautiful but sullen creature's eyes, forming a
  puddle beneath her delicate feet.
title2: Lampad
CR: 5
sources:
- name: Bestiary 4
  page: 178
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 1600
alignment: CN
size: Medium
type: fey
initiative:
  bonus: 5
senses:
  darkvision: 90
  low-light vision: true
auras:
- name: insane beauty
  radius: 30
AC:
  AC: 20
  touch: 20
  flat_footed: 15
  components:
    deflection: 5
    dex: 5
HP:
  HP: 52
  long: 7d6+28
saves:
  fort: 6
  ref: 10
  will: 8
DR:
- amount: 5
  weakness: cold iron
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk dagger +9 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 9
  ranged:
  - - text: mwk sling +9 (1d4)
      entries:
      - - damage: 1d4
      attack: mwk sling
      bonus:
      - 9
  special:
  - weep
spell_like_abilities:
  entries:
  - name: meld into stone
    source: default
    freq: At will
  - name: stone tell
    source: default
    freq: At will
  sources:
  - name: default
    CL: 7
    concentration: 12
spells:
  entries:
  - name: stone shape
    source: Druid
    level: 3
  - name: spider climb
    source: Druid
    level: 2
  - superscripts:
    - APG
    name: stone call
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
  - name: faerie fire
    source: Druid
    level: 1
  - name: magic stone
    source: Druid
    level: 1
  - name: detect magic
    source: Druid
    level: 0
  - name: detect poison
    source: Druid
    level: 0
  - name: light
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 5
    concentration: 8
ability_scores:
  STR: 10
  DEX: 21
  CON: 18
  INT: 14
  WIS: 17
  CHA: 21
BAB: 3
CMB: 3
CMD: 23
feats:
- name: Alertness
- name: Combat Casting
- name: Point-Blank Shot
- name: Weapon Finesse
skills:
  Diplomacy: 13
  Knowledge (dungeoneering): 9
  Knowledge (nature): 12
  Linguistics: 3
  Perception: 15
  Perform (sing): 9
  Sense Motive: 15
  Spellcraft: 9
  Stealth: 15
  Use Magic Device: 15
languages:
- Aklo
- Common
- Undercommon
special_qualities:
- guarded
ecology:
  environment: any underground
  organization: solitary
  treasure_type: standard
  treasure:
  - masterwork dagger
  - masterwork sling
  - other treasure
special_abilities:
  Guarded (Su): A lampad adds her Charisma modifier as a deflection bonus to her Armor
    Class.
  Insane Beauty (Su): This ability affects all humanoids within 30 feet who are viewing
    a lampad in conditions brighter than dim light. Those who look directly upon the
    lampad must succeed at a DC 18 Will save or gain the confused condition for 1d6
    rounds. A creature that succeeds at the save is immune to the same lampad's insane
    beauty for 24 hours. A lampad can suppress or resume this ability as a free action.
    The save DC is Charisma-based.
  Spells: A lampad casts spells as a 5th-level druid, but can't swap out prepared
    spells to cast summon spells.
  Weep (Su): As a standard action, a lampad can unsettle those near her when she cries.
    Any creature within 30 feet who can hear a lampad weeping becomes shaken unless
    it succeeds at a DC 18 Will saving throw. This ability can't cause a creature
    to become frightened or panicked. This is a mindaffecting fear effect that relies
    on audible components. The save DC is Charisma-based.
desc_long: |-
  Dark and moody cousins to nymphs, lampads sulk along natural caverns and dank tunnels, their weeping cries echoing through the darkness. These creatures are often found carrying light in caverns and dungeons, drawing creatures to them like moths to flame. Though they prefer the darkness, they know that exposing their forms under bright conditions gives them an edge over creatures viewing them.

  Just as nymphs guard nature's purest places and dryads protect their sacred trees, lampads watch over the dark places of the world. They speak to the stone that forms their murky world, and their forlorn cries ring out through the belly of the earth.

---

# Lampad
Tears stream from this beautiful but sullen creature’s eyes, forming a puddle beneath her delicate feet.
**Source** Bestiary 4 pg. 178
**XP** 1,600

CN Medium fey
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 90 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15
**Aura** insane beauty (30 ft.)

##### Defense

**AC** 20, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 _[[spells/Deflection|deflection]]_, +5 Dex)
**hp** 52 (7d6+28)
**Fort** +6, **Ref** +10, **Will** +8
**DR** 5/cold iron

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +9 (1d4/19–20)
**Ranged** mwk _[[items/Weapon/Sling|sling]]_ +9 (1d4)
**Special Attacks** weep
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +12)
At will—_[[spells/Meld into Stone|meld into stone]]_, _[[spells/Stone Tell|stone tell]]_
**_[[classes/Druid|Druid]]_ Spells Prepared **(CL 5th; concentration +8)
3rd—_[[spells/Stone Shape|stone shape]]_
2nd—_[[spells/Spider Climb|spider climb]]_, _[[spells/Stone Call|stone call]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Magic Stone|magic stone]]_
0—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Mending|mending]]_

##### Statistics
**Str** 10, **Dex** 21, **Con** 18, **Int** 14, **Wis** 17, **Cha** 21
**Base Atk** +3; **CMB** +3; **CMD** 23
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Diplomacy +13, Knowledge (dungeoneering) +9, Knowledge (nature) +12, Linguistics +3, Perception +15, Perform (sing) +9, Sense Motive +15, Spellcraft +9, Stealth +15, Use Magic Device +15
**Languages** Aklo, Common, Undercommon
**SQ** guarded

##### Ecology

**Environment** any underground
**Organization** solitary
**Treasure** standard (masterwork _dagger_, masterwork _sling_, other treasure)

### Special Abilities

**Guarded (Su)** A _[[monsters/Lampad|lampad]]_ adds her Charisma modifier as a _deflection_ bonus to her Armor Class.

**Insane Beauty (Su)** This ability affects all humanoids within 30 feet who are viewing a _lampad_ in conditions brighter than dim light. Those who look directly upon the _lampad_ must succeed at a DC 18 Will save or gain the _[[conditions/Confused|confused]]_ condition for 1d6 rounds. A creature that succeeds at the save is immune to the same _lampad_’s insane beauty for 24 hours. A _lampad_ can suppress or resume this ability as a free action. The save DC is Charisma-based.
**Spells** A _lampad_ casts spells as a 5th-level _druid_, but can’t swap out prepared spells to cast _[[universal monster rules/Summon|summon]]_ spells.

**Weep (Su)** As a standard action, a _lampad_ can unsettle those near her when she cries. Any creature within 30 feet who can hear a _lampad_ _[[items/Armor Magic Abilities/Weeping|weeping]]_ becomes _[[conditions/Shaken|shaken]]_ unless it succeeds at a DC 18 Will saving throw. This ability can’t cause a creature to become _[[conditions/Frightened|frightened]]_ or _[[conditions/Panicked|panicked]]_. This is a mindaffecting _[[universal monster rules/Fear|fear]]_ effect that relies on audible components. The save DC is Charisma-based.

##### Description

Dark and moody cousins to nymphs, lampads sulk along natural caverns and dank tunnels, their _weeping_ cries echoing through the _[[spells/Darkness|darkness]]_. These creatures are often found carrying light in caverns and dungeons, drawing creatures to them like moths to flame. Though they prefer the _darkness_, _[[spells/They Know|they know]]_ that exposing their forms under bright conditions gives them an edge over creatures viewing them.

Just as nymphs _[[npcs/Guard|guard]]_ nature’s purest places and dryads protect their _[[items/Weapon Magic Abilities/Sacred|sacred]]_ trees, lampads watch over the dark places of the world. They speak to the stone that forms their murky world, and their forlorn cries ring out through the belly of the earth.