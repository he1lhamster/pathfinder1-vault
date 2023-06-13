---
cssclass: [monsters]
title1: Worm That Walks, Locust Variant
desc_short: Hordes of swarming locusts coalesce to make up the form of a humanoid
  woman carrying a scythe, a demonic symbol emblazoned on her chest.
title2: Locust Variant
CR: 8
sources:
- name: "Pathfinder #75: Demon's Heresy"
  page: 74
  link: http://paizo.com/products/btpy91dm?Pathfinder-Adventure-Path-75-Demons-Heresy
XP: 4800
race: Female
classes:
- human worm that walks cleric of Deskari 7
alignment: CE
size: Medium
type: vermin
subtypes:
- augmented human
initiative:
  bonus: 2
senses:
  blindsight: 30
  darkvision: 60
AC:
  AC: 19
  touch: 19
  flat_footed: 16
  components:
    deflection: 1
    dex: 2
    dodge: 1
    insight: 5
HP:
  HP: 77
  long: 7d8+42
  fast_healing: 8
saves:
  fort: 9
  ref: 4
  will: 10
defensive_abilities:
- worm that walks traits
DR:
- amount: 15
  weakness: '-'
immunities:
- disease
- paralysis
- poison
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk scythe +8 (2d4+1/x4)
      entries:
      - - damage: 2d4+1
          crit_multiplier: 4
      attack: mwk scythe
      bonus:
      - 8
  - - text: slam +6 (1d4+1 plus grab)
      entries:
      - - damage: 1d4+1
        - effect: grab
      attack: slam
      bonus:
      - 6
  special:
  - discorporate
  - channel negative energy 6/day (DC 16, 4d6)
  - destructive smite (+3, 8/day)
  - squirming embrace
  - tenacious
spell_like_abilities:
  entries:
  - name: touch of evil
    source: default
    freq: 8/day
    other: 3 rounds
  sources:
  - name: default
    CL: 7
    concentration: 12
spells:
  entries:
  - name: air walk
    source: Cleric
    level: 4
  - name: divine power
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: unholy blight
    source: Cleric
    level: 4
    DC: 19
  - name: contagion
    source: Cleric
    level: 3
    DC: 18
  - name: dispel magic
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic circle against good
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
  - name: cure moderate wounds
    source: Cleric
    level: 2
  - name: darkness
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 17
  - is_domain_spell: true
    name: shatter
    source: Cleric
    level: 2
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: command
    source: Cleric
    level: 1
    DC: 16
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: doom
    source: Cleric
    level: 1
    DC: 16
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: protection from good
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: true strike
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 7
    concentration: 12
    slots:
      0: at-will
    domains:
    - destruction
    - evil
ability_scores:
  STR: 13
  DEX: 14
  CON: 18
  INT: 8
  WIS: 20
  CHA: 12
BAB: 5
CMB: 6
CMB_other: +14 grapple
CMD: 29
CMD_other: 33 vs. grapple
feats:
- is_bonus: true
  name: Diehard
- name: Dodge
- name: Extra Channel
- name: Improved Channel
- name: Toughness
- name: Weapon Focus (scythe)
skills:
  Knowledge (planes): 6
  Knowledge (religion): 5
  Perception: 15
  Sense Motive: 13
  Spellcraft: 7
  Stealth: 10
  _racial_mods:
    Perception:
      _: 8
    Sense Motive:
      _: 8
    Stealth:
      _: 8
languages:
- Common
gear:
  gear:
  - mwk scythe
  - headband of inspired wisdom +2
  - ring of protection +1
desc_long: |-
  Because of the odd and usually accidental circumstances through which worms that walk are born, the process of such birth is far from standardized. Thus, the worms themselves can take more shapes than simply the most common one. For purposes of clarity, all of the variants presented below are referred to as worms that walk, even if their main components are not actually worms. These variants are created using the same statistics presented in Pathfinder RPG Bestiary 2, and usually the only changes are cosmetic in nature (though see locust variant, below).

  Army Ants: Common in Garund's deserts and lush, tropical jungles, army ants swarm over the land like a living carpet, devouring everything they come across. A worm that walks composed of army ants likewise consumes everything in its path-including the body of the spellcaster it once was. Disturbingly, these worms that walk spend little of their time in humanoid-shaped form, preferring to crawl as a biting swarm of legs and pincers. This form of worms that walk is mostly likely to be encountered in underground-dwelling; these horrific creatures are said to include one who calls the dangerous sands of Thuvia home.

  Cockroaches: Cockroaches can be found in great numbers anywhere civilization stains the landscape with its refuse. Worms that walk composed of cockroaches are more likely to be found in urban areas, especially in large cities where they can go unnoticed by most, usually arising when both corpses and magical eff luent are deposited in sewers and garbage dumps. A worm that walks composed of cockroaches is a creature of stealth and guile. Frequently keeping to the shadows and sewers of the city, these worms that walk broker information and engage in blackmail, augmenting their unnatural talents with strong illusion and enchantment magic. Some say that a powerful enchantress worm that walks made of cockroaches runs a guild of thieves in Absalom, but no reliable sources can say they've met her.

  Locusts: Found in any area that sports-or once sported-verdant plant life, this worm that walks variant has plague-like nuances and can be particularly hard to kill. Made up of ravenous locusts, these worms that walk make meals of any creatures weaker than they, and are particularly attuned to their animalistic instincts. One of these particularly appalling worms that walk is said to threaten the agriculture-rich lands of Geb, and due to the inf luence of Deskari in the Worldwound, a few of these creatures have been spotted in the ruins of Sarkoris.

  Wasps: Typically found in warm, moist regions, these worms that walk are made from hundreds of thousands of buzzing, swarming wasps. Aggressive and cruel, these worms that walk favor poison and other debilitating substances, and commonly focus their arcane knowledge on creating potent toxins. Rumor has it that one of these horrific creatures rules over a tribe of hunters along one of the winding tributaries threading throughout the Mwangi Expanse.

---

# Worm That Walks, Locust Variant
Hordes of swarming locusts coalesce to make up the form of a humanoid woman carrying a _[[items/Weapon/Scythe|scythe]]_, a demonic symbol emblazoned on her chest.
**Source** Pathfinder #75: Demon's Heresy pg. 74
**XP** 4,800
Female human _[[monsters/Worm That Walks|worm that walks]]_ _[[classes/Cleric|cleric]]_ of Deskari 7
CE Medium vermin (augmented human)
**Init** +2; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +15

##### Defense

**AC** 19, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+1 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +5 insight)
**hp** 77 (7d8+42); _[[universal monster rules/Fast Healing|fast healing]]_ 8
**Fort** +9, **Ref** +4, **Will** +10
**Defensive Abilities** _worm that walks_ traits; **DR** 15/—; **Immune** disease, _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep

##### Offense
**Speed** 30 ft.
**Melee** mwk _scythe_ +8 (2d4+1/x4) or slam +6 (1d4+1 plus _[[universal monster rules/Grab|grab]]_)
**Special Attacks** discorporate, channel negative energy 6/day (DC 16, 4d6), destructive smite (+3, 8/day), squirming embrace, tenacious
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +12)
8/day—_[[feats/Touch Of Evil|touch of evil]]_ (3 rounds)
**_Cleric_ Spells Prepared **(CL 7th; concentration +12)
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Divine Power|divine power]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
3rd—_[[spells/Contagion|contagion]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Protection from Energy|protection from energy]]_
2nd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Darkness|darkness]]_, _[[spells/Hold Person|hold person]]_ (DC 17), _[[spells/Shatter|shatter]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Command|command]]_ (DC 16), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Doom|doom]]_ (DC 16), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Protection From Good|protection from good]]_, _[[spells/Shield Of Faith|shield of faith]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**D** domain spell; **Domains** _[[spells/Destruction|Destruction]]_, Evil

##### Statistics
**Str** 13, **Dex** 14, **Con** 18, **Int** 8, **Wis** 20, **Cha** 12
**Base Atk** +5; **CMB** +6 (+14 grapple); **CMD** 29 (33 vs. grapple)
**Feats** _[[feats/Diehard|Diehard]]_, _Dodge_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scythe_)
**Skills** Knowledge (planes) +6, Knowledge (religion) +5, Perception +15, Sense Motive +13, Spellcraft +7, Stealth +10; **Racial Modifiers** +8 Perception, +8 Sense Motive, +8 Stealth
**Languages** Common
**Gear** mwk _scythe_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_

##### Description

Because of the odd and usually accidental circumstances through which worms that walk are born, the process of such birth is far from standardized. Thus, the worms themselves can take more shapes than simply the most common one. For purposes of _[[items/Weapon/Clarity|clarity]]_, all of the variants presented below are referred to as worms that walk, even if their main components are not actually worms. These variants are created using the same statistics presented in Pathfinder RPG Bestiary 2, and usually the only changes are cosmetic in nature (though see locust variant, below).

**Army Ants**: Common in Garund’s deserts and lush, tropical jungles, army ants swarm over the land like a living carpet, devouring everything they come across. A _worm that walks_ composed of army ants likewise consumes everything in its path—including the body of the spellcaster it once was. Disturbingly, these worms that walk spend little of their time in humanoid-shaped form, preferring to crawl as a biting swarm of legs and pincers. This form of worms that walk is mostly likely to be encountered in underground-dwelling; these horrific creatures are said to include one who calls the dangerous sands of Thuvia home.

**Cockroaches**: Cockroaches can be found in great numbers anywhere civilization stains the landscape with its refuse. Worms that walk composed of cockroaches are more likely to be found in urban areas, especially in large cities where they can _[[feats/Go Unnoticed|go unnoticed]]_ by most, usually arising when both corpses and magical eff luent are deposited in sewers and garbage dumps. A _worm that walks_ composed of cockroaches is a creature of stealth and guile. Frequently keeping to the shadows and sewers of the city, these worms that walk broker information and engage in blackmail, augmenting their unnatural talents with strong illusion and enchantment magic. Some say that a powerful enchantress _worm that walks_ made of cockroaches runs a guild of thieves in Absalom, but no reliable sources can say they’ve met her.

**Locusts**: Found in any area that sports—or once sported—verdant plant life, this _worm that walks_ variant has plague-like nuances and can be particularly hard to kill. Made up of _[[curses/Ravenous|ravenous]]_ locusts, these worms that walk make meals of any creatures weaker than they, and are particularly attuned to their animalistic instincts. One of these particularly appalling worms that walk is said to threaten the agriculture-rich lands of Geb, and due to the inf luence of Deskari in the Worldwound, a few of these creatures have been spotted in the ruins of Sarkoris.

**Wasps**: Typically found in warm, moist regions, these worms that walk are made from hundreds of thousands of buzzing, swarming wasps. Aggressive and _[[items/Weapon Magic Abilities/Cruel|cruel]]_, these worms that walk favor poison and other _[[items/Weapon Magic Abilities/Debilitating|debilitating]]_ substances, and commonly focus their arcane knowledge on creating _[[items/Weapon Magic Abilities/Potent|potent]]_ toxins. Rumor has it that one of these horrific creatures rules over a tribe of hunters along one of the winding tributaries threading throughout the Mwangi Expanse.