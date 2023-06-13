---
cssclass: [monsters]
title1: Daughter of Urgathoa
desc_short: What was once a woman now towers as a monstrosity of ectoplasmic flesh,
  horns, and a tremendous scythelike claw.
title2: Daughter of Urgathoa
CR: 8
sources:
- name: Inner Sea World Guide
  page: 309
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderChronicles/v5748btpy8ief
- name: 'Pathfinder #8: Seven Days to the Grave'
  page: 82
  link: http://paizo.com/pathfinder/adventurePath/curseOfTheCrimsonThrone/v5748btpy82qy
XP: 4800
alignment: NE
size: Large
type: undead
initiative:
  bonus: 7
senses:
  darkvision: 60
auras:
- name: desecrate
  radius: 20
AC:
  AC: 21
  touch: 12
  flat_footed: 18
  components:
    dex: 3
    natural: 9
    size: -1
HP:
  HP: 115
  long: 11d8+66
saves:
  fort: 9
  ref: 7
  will: 11
defensive_abilities:
- channel resistance +4
immunities:
- undead traits
speeds:
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: great claw +16 (2d6+9/x4 plus disease)
      entries:
      - - damage: 2d6+9
          crit_multiplier: 4
        - effect: disease
      attack: great claw
      bonus:
      - 16
    - text: claw +16 (1d8+9)
      entries:
      - - damage: 1d8+9
      attack: claw
      bonus:
      - 16
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: desecrate
    source: default
    freq: Constant
    other: centered on self
  sources:
  - name: default
    CL: 11
    concentration: 16
spells:
  entries:
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 16
  - name: contagion
    source: Cleric
    level: 3
    DC: 16
  - is_domain_spell: true
    name: dispel magic
    source: Cleric
    level: 3
  - name: inflict serious wounds
    source: Cleric
    level: 3
    DC: 16
  - is_domain_spell: true
    name: death knell
    source: Cleric
    level: 2
    DC: 15
  - name: hold person
    source: Cleric
    level: 2
    DC: 15
  - name: inflict moderate wounds
    source: Cleric
    level: 2
    DC: 15
  - name: resist energy
    source: Cleric
    level: 2
  - name: spiritual weapon
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: cause fear
    source: Cleric
    level: 1
    DC: 14
  - name: command
    source: Cleric
    level: 1
    DC: 14
  - name: divine favor
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 13
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 6
    concentration: 9
    domains:
    - death
    - magic
ability_scores:
  STR: 27
  DEX: 17
  CON:
  INT: 18
  WIS: 16
  CHA: 21
BAB: 8
CMB: 17
CMD: 30
feats:
- name: Ability Focus (disease)
- name: Combat Casting
- name: Combat Reflexes
- name: Improved Initiative
- name: Power Attack
- name: Vital Strike
skills:
  Acrobatics: 14
  Bluff: 16
  Fly: 23
  Intimidate: 19
  Knowledge (religion): 18
  Perception: 17
  Sense Motive: 17
  Spellcraft: 18
  Stealth: 0
languages:
- Abyssal
- Common
- Infernal
- Necril
ecology:
  environment: any
  organization: solitary or cult (1 daughter plus 2d8 human clerics)
  treasure_type: double
special_abilities:
  Desecrate (Sp): The bonuses granted from the daughter of Urgathoa's constant desecrate
    spell-like ability (which is always centered on herself) are calculated into the
    stats above.
  Disease (Su): 'Bubonic Plague: Great claw-injury; save Fortitude DC 20; onset immediate;
    frequency 1/day; effect 1d4 Con damage and target is fatigued; cure 2 consecutive
    saves. The save DC is Charisma-based.'
  Great Claw (Ex): One of the daughter's hands is a tremendous scythe-shaped claw.
    This attack inflicts ×4 damage on a critical hit, and is treated as an evil weapon
    for the purposes of penetrating damage reduction.
  Spells: A daughter of Urgathoa casts spells as a 6th-level cleric of Urgathoa-but
    although she selects two domains to determine bonus spells, she does not gain
    any domain powers.
desc_long: Within the church of the goddess of undeath, few more coveted stations
  exist than daughter of Urgathoa, yet no high priest can bestow the title, and no
  living worshiper can take the role. Rather, daughters of Urgathoa are selected by
  the fickle goddess herself, chosen from her most zealous and accomplished priestesses
  only at the moment of their deaths. Even after their transformations into things
  of pestilence and dead flesh, daughters of Urgathoa remain social beings who typically
  surround themselves with fanatical cults.

---

# Daughter of Urgathoa
What was once a woman now towers as a monstrosity of ectoplasmic flesh, horns, and a tremendous scythelike claw.
**Source** Inner Sea World Guide pg. 309, Pathfinder #8: Seven Days to the Grave pg. 82
**XP** 4,800

NE Large undead
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +17
**Aura** _[[spells/Desecrate|desecrate]]_ (20-ft. radius)

##### Defense

**AC** 21, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+3 Dex, +9 natural, -1 size)
**hp** 115 (11d8+66)
**Fort** +9, **Ref** +7, **Will** +11
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** fly 40 ft. (perfect)
**Melee** great claw +16 (2d6+9/x4 plus disease), claw +16 (1d8+9)
**Space** 10 ft., **Reach** 10 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +16)
Constant - _desecrate_ (centered on self)
**_[[classes/Cleric|Cleric]]_ Spells Prepared** (CL 6th; concentration +9)
3rd — _[[spells/Bestow Curse|bestow curse]]_ (DC 16), _[[spells/Contagion|contagion]]_ (DC 16), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Inflict Serious Wounds|inflict serious wounds]]_ (DC 16)
2nd — _[[spells/Death Knell|death knell]]_ (DC 15), _[[spells/Hold Person|hold person]]_ (DC 15), _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_ (DC 15), _[[spells/Resist Energy|resist energy]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_
1st — _[[spells/Cause Fear|cause fear]]_ (DC 14), _[[spells/Command|command]]_ (DC 14), _[[spells/Divine Favor|divine favor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 — _[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[universal monster rules/Resistance|resistance]]_
**D** domain spell; **Domains** Death, Magic

##### Statistics
**Str** 27, **Dex** 17, **Con** —, **Int** 18, **Wis** 16, **Cha** 21
**Base Atk** +8; **CMB** +17; **CMD** 30
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (disease), _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +14, Bluff +16, Fly +23, Intimidate +19, Knowledge (religion) +18, Perception +17, Sense Motive +17, Spellcraft +18, Stealth +0
**Languages** Abyssal, Common, Infernal, Necril

##### Ecology

**Environment** any
**Organization** solitary or cult (1 daughter plus 2d8 human clerics)
**Treasure** double

### Special Abilities

**_Desecrate_ (Sp)** The bonuses granted from the _[[monsters/Daughter of Urgathoa|daughter of Urgathoa]]_’s constant _desecrate_ spell-like ability (which is always centered on herself) are calculated into the stats above.

**Disease (Su)** _[[diseases/Bubonic Plague|Bubonic Plague]]_: Great claw—injury; save Fortitude DC 20; onset immediate; frequency 1/day; effect 1d4 Con damage and target is _[[conditions/Fatigued|fatigued]]_; cure 2 consecutive saves. The save DC is Charisma-based.

**Great Claw (Ex)** One of the daughter’s hands is a tremendous scythe-shaped claw. This attack inflicts ×4 damage on a critical hit, and is treated as an evil weapon for the purposes of penetrating _[[universal monster rules/Damage Reduction|damage reduction]]_.
**Spells** A _daughter of Urgathoa_ casts spells as a 6th-level _cleric_ of Urgathoa—but although she selects two domains to determine bonus spells, she does not gain any domain powers.

##### Description

Within the church of the goddess of undeath, few more coveted stations exist than _daughter of Urgathoa_, yet no high priest can bestow the title, and no living worshiper can take the role. Rather, daughters of Urgathoa are selected by the fickle goddess herself, chosen from her most zealous and accomplished priestesses only at the moment of their deaths. Even after their transformations into things of pestilence and dead flesh, daughters of Urgathoa remain social beings who typically surround themselves with fanatical cults.