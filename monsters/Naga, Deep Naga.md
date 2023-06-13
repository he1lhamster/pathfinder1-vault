---
cssclass: [monsters]
title1: Naga, Deep Naga
desc_short: This creature's massive, serpentine body is covered in dark purple scales.
  Its humanoid head has a wide mouth filled with fangs.
title2: Deep Naga
CR: 12
sources:
- name: 'Pathfinder #118: Siege of Stone'
  page: 90
  link: http://paizo.com/products/btpy9pn4
XP: 19200
alignment: NE
size: Huge
type: aberration
initiative:
  bonus: 9
senses:
  darkvision: 120
  low-light vision: true
AC:
  AC: 27
  touch: 13
  flat_footed: 22
  components:
    dex: 5
    natural: 14
    size: -2
HP:
  HP: 161
  long: 17d8+85
saves:
  fort: 10
  ref: 10
  will: 15
defensive_abilities:
- spell siphon
SR: 23
weaknesses:
- ley-line dependent
speeds:
  base: 40
  burrow: 20
  swim: 20
attacks:
  melee:
  - - text: bite +20 (2d6+9/19-20 plus magical disruption)
      entries:
      - - damage: 2d6+9
          crit_range: 19-20
        - effect: magical disruption
      attack: bite
      bonus:
      - 20
    - text: tail slap +17 (2d6+4)
      entries:
      - - damage: 2d6+4
      attack: tail slap
      bonus:
      - 17
  special:
  - breath weapon (80-ft. line, 12d6 force damage plus magical disruption, Reflex
    DC 23 for half, usable every 1d4 rounds)
space: 15
reach: 15
spells:
  entries:
  - name: commune with nature
    source: Sorcerer
    level: 5
  - name: telekinesis
    source: Sorcerer
    level: 5
  - name: bestow curse
    source: Sorcerer
    level: 4
    DC: 17
  - name: cure serious wounds
    source: Sorcerer
    level: 4
  - name: illusory wall
    source: Sorcerer
    level: 4
    DC: 17
  - name: aversion
    source: Sorcerer
    level: 3
    DC: 16
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: greater magic fang
    source: Sorcerer
    level: 3
  - name: snare
    source: Sorcerer
    level: 3
  - name: barkskin
    source: Sorcerer
    level: 2
  - name: false life
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: scare
    source: Sorcerer
    level: 2
    DC: 15
  - name: web
    source: Sorcerer
    level: 2
    DC: 15
  - name: cure light wounds
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: obscuring mist
    source: Sorcerer
    level: 1
  - name: pass without trace
    source: Sorcerer
    level: 1
  - name: true strike
    source: Sorcerer
    level: 1
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 13
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 13
  - name: guidance
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: open/close
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  - name: virtue
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 11
    concentration: 14
    slots:
      5: 4
      4: 6
      3: 7
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 28
  DEX: 21
  CON: 20
  INT: 13
  WIS: 16
  CHA: 17
BAB: 12
CMB: 23
CMD: 38
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Multiattack
- name: Step Up
- name: Vital Strike
- name: Weapon Focus (bite)
skills:
  Acrobatics: 8
  Intimidate: 18
  Knowledge (arcana): 12
  Knowledge (local): 15
  Perception: 21
  Sense Motive: 15
  Spellcraft: 16
    to attune to ley lines: 20
  Stealth: 12
  Swim: 17
  _racial_mods:
    Spellcraft:
      to attune to ley lines: 4
languages:
- Aklo
- Undercommon
ecology:
  environment: any underground
  organization: solitary, pair, or nest (3-4)
  treasure_type: standard
special_abilities:
  Ley-Line Dependent (Su): Deep nagas draw their power from ley lines deep underground.
    While attuned to a ley line (Pathfinder RPG Occult Adventures 233), a deep naga
    gains an additional +1 bonus to its effective caster level, increasing the maximum
    bonus possible from a ley line to +6. If the deep naga is more than 100 feet from
    its attuned ley line or its attunement is broken for any reason, the deep naga
    takes 1d6 points of nonlethal damage per caster level of the ley line, cannot
    use its breath weapon, and must succeed at a concentration check (DC = 15 + spell
    level) in order to cast spells until it attunes itself to a new ley line or its
    attunement to its previous ley line is restored.
  Magical Disruption (Su): A deep naga's bite and breath weapon have powerful dispelling
    effects. A creature that takes damage from either attack has any ongoing spell
    effects on it disrupted as though targeted by a dispel magic spell (CL 11th).
  Spell Siphon (Su): A deep naga draws magical energy from its surroundings. Any spell
    that fails to penetrate the naga's spell resistance is absorbed. Once per round,
    as an immediate action while absorbing a spell in such a manner, the deep naga
    can decrease the time until it can use its breath weapon by 1 round, attempt a
    new saving throw against an ongoing magical effect, or regain a spell slot of
    a level equal to or lower than the level of the absorbed spell.
  Spells: A deep naga casts spells as per an 11th-level sorcerer and can cast spells
    from the druid list as well as those normally available to a sorcerer. Druid spells
    are considered arcane spells for a deep naga.
desc_long: |-
  More bestial than their surface cousins, deep nagas jealously guard their lairs in the lightless depths of the Darklands. Deep nagas live near ley lines and other places of power because they hunger for magical energy, which they are able to siphon from their surroundings. Their volatile natures make them dangerous to deal with, but creatures who manage to appease them can earn safety within their territory. Most deep nagas measure 40 feet in length and weigh 1,800 pounds.

   Some deep nagas are infused from birth with energy native to another plane of existence. These variant deep nagas replace their breath weapon damage with one of the following damage types: acid, cold, electricity, fire, or negative energy. They set up lairs in places where the borders between planes are thin rather than along ley lines, and their appearances often reflect the influence of those elemental planes.

---

# Naga, Deep Naga
This creature’s massive, serpentine body is covered in dark purple scales. Its humanoid head has a wide mouth filled with fangs.
**Source** Pathfinder #118: Siege of Stone pg. 90
**XP** 19,200

NE Huge aberration
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +21

##### Defense

**AC** 27, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+5 Dex, +14 natural, –2 size)
**hp** 161 (17d8+85)
**Fort** +10, **Ref** +10, **Will** +15
**Defensive Abilities** _[[items/Weapon Magic Abilities/Spell Siphon|spell siphon]]_; **SR** 23
**Weaknesses** ley-line dependent

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., swim 20 ft.
**Melee** bite +20 (2d6+9/19–20 plus magical _[[items/Weapon Magic Abilities/Disruption|disruption]]_), tail slap +17 (2d6+4)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (80-ft. line, 12d6 force damage plus magical _disruption_, Reflex DC 23 for half, usable every 1d4 rounds)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 11th; concentration +14)
5th (4)—_[[spells/Commune with Nature|commune with nature]]_, _[[spells/Telekinesis|telekinesis]]_
4th (6)—_[[spells/Bestow Curse|bestow curse]]_ (DC 17), _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Illusory Wall|illusory wall]]_ (DC 17)
3rd (7)—_[[spells/Aversion|aversion]]_ (DC 16), _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ _[[spells/Magic Fang|magic fang]]_, _[[spells/Snare|snare]]_
2nd (7)—_[[spells/Barkskin|barkskin]]_, _[[spells/False Life|false life]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Scare|scare]]_ (DC 15), web (DC 15)
1st (7)—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Pass without Trace|pass without trace]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Guidance|guidance]]_, _[[spells/Mage Hand|mage hand]]_, open/close, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Virtue|virtue]]_

##### Statistics
**Str** 28, **Dex** 21, **Con** 20, **Int** 13, **Wis** 16, **Cha** 17
**Base Atk** +12; **CMB** +23; **CMD** 38 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Step Up|Step Up]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Acrobatics +8, Intimidate +18, Knowledge (arcana) +12, Knowledge (local) +15, Perception +21, Sense Motive +15, Spellcraft +16 (+20 to attune to ley lines), Stealth +12, Swim +17; **Racial Modifiers** +4 Spellcraft to attune to ley lines
**Languages** Aklo, Undercommon

##### Ecology

**Environment** any underground
**Organization** solitary, pair, or nest (3–4)
**Treasure** standard

### Special Abilities

**Ley-Line Dependent (Su)** Deep nagas draw their power from ley lines deep underground. While attuned to a ley line (Pathfinder RPG Occult Adventures 233), a deep naga gains an additional +1 bonus to its effective caster level, increasing the maximum bonus possible from a ley line to +6. If the deep naga is more than 100 feet from its attuned ley line or its attunement is _[[conditions/Broken|broken]]_ for any reason, the deep naga takes 1d6 points of nonlethal damage per caster level of the ley line, cannot use its _breath weapon_, and must succeed at a concentration check (DC = 15 + spell level) in order to cast spells until it attunes itself to a new ley line or its attunement to its previous ley line is restored.

**Magical _Disruption_ (Su)** A deep naga’s bite and _breath weapon_ have powerful _[[items/Weapon Magic Abilities/Dispelling|dispelling]]_ effects. A creature that takes damage from either attack has any ongoing spell effects on it disrupted as though targeted by a _[[spells/Dispel Magic|dispel magic]]_ spell (CL 11th).
**_Spell Siphon_ (Su)** A deep naga draws magical energy from its surroundings. Any spell that fails to penetrate the naga’s _[[universal monster rules/Spell Resistance|spell resistance]]_ is absorbed. Once per round, as an immediate action while absorbing a spell in such a manner, the deep naga can decrease the time until it can use its _breath weapon_ by 1 round, attempt a new saving throw against an ongoing magical effect, or regain a spell slot of a level equal to or lower than the level of the absorbed spell.
**Spells** A deep naga casts spells as per an 11th-level _sorcerer_ and can cast spells from the _[[classes/Druid|druid]]_ list as well as those normally available to a _sorcerer_. _Druid_ spells are considered arcane spells for a deep naga.

##### Description

More bestial than their surface cousins, deep nagas jealously _[[npcs/Guard|guard]]_ their lairs in the lightless depths of the Darklands. Deep nagas live near ley lines and other places of power because they hunger for magical energy, which they are able to siphon from their surroundings. Their volatile natures make them dangerous to deal with, but creatures who manage to appease them can earn safety within their territory. Most deep nagas measure 40 feet in length and weigh 1,800 pounds.

Some deep nagas are infused from birth with energy native to another plane of existence. These variant deep nagas replace their _breath weapon_ damage with one of the following damage types: acid, cold, electricity, fire, or negative energy. They set up lairs in places where the borders between planes are thin rather than along ley lines, and their appearances often reflect the influence of those elemental planes.