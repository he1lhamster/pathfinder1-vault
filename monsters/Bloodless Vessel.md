---
cssclass: [monsters]
title1: Bloodless Vessel
is_3.5: true
desc_short: This pale youth's wispy beard does little to make him look older. He stares
  with misty white eyes, and there is something unnatural about the way he stands,
  blank-faced and emotionless. He moves like a puppet, a thing guided by unseen hands.
  He holds a scythe that should be too heavy for his spindly arms, but the weight
  doesn't seem to bother him.
title2: Bloodless Vessel
CR: 12
sources:
- name: Blood of Dragonscar
  page: 30
  link: http://paizo.com/store/paizo/pathfinder/modules/35E/v5748btpy8739
alignment: NE
size: Medium
type: undead
initiative:
  bonus: 8
senses:
  darkvision: 60
AC:
  AC: 24
  touch: 18
  flat_footed: 20
  components:
    deflection: 4
    dex: 4
    natural: 6
HP:
  HP: 123
  long: 18d12+6
saves:
  fort: 6
  ref: 10
  will: 14
immunities:
- undead immunities
speeds:
  base: 30
attacks:
  melee:
  - - text: scythe +19 (2d4+13/19-20/x4)
      entries:
      - - damage: 2d4+13
          crit_range: 19-20
          crit_multiplier: 4
      attack: scythe
      bonus:
      - 19
  - - text: slam +18 (1d6+9)
      entries:
      - - damage: 1d6+9
      attack: slam
      bonus:
      - 18
  ranged:
  - - text: necrotic blast +14 ranged touch (5d6 negative energy damage)
      entries:
      - - damage: 5d6
          type: negative energy damage
      attack: necrotic blast
      bonus:
      - 14
      touch: true
spell_like_abilities:
  entries: []
  sources:
  - name: default
    CL: 10
  varies: true
ability_scores:
  STR: 28
  DEX: 19
  CON:
  INT: 14
  WIS: 16
  CHA: 19
BAB: 9
grapple_3.5: 18
feats:
- name: Combat Reflexes
- name: Improved Critical (scythe)
- name: Improved Initiative
- name: Improved Trip
- name: Toughness
- name: Weapon Focus (scythe)
skills:
  Climb: 16
  Concentration: 14
  Intimidation: 18
  Jump: 19
  Knowledge (arcana): 12
  Knowledge (history): 15
  Knowledge (religion): 10
  Sense Motive: 15
  Spellcraft: 10
  Tumble: 15
  Listen: 12
  Spot: 18
languages:
- Common and 1d4 other languages
special_qualities:
- Host to Many
special_abilities:
  Host to Many (Ex): A bloodless vessel is an undead creature, but it is host to many
    spirits. As such, it responds to turn attempts in an unusual manner. A successful
    turn attempt against the vessel drives away some of the inhabiting spirits for
    1 minute (these flee visibly in the form of flying shadows, returning when the
    turn effect expires). This negates the vessel's deflection bonus to armor class
    for the duration of the turning.
  Spell-like Abilities (Sp): |-
    Between its undead nature and the diverse backgrounds of the spirits that comprise a vessel's collective soul, a vessel has an unpredictable set of spell-like abilities. Some spread fear and disease, others focus on weakness and despair. Some have more in common with vampires, while others are more like ghouls. Choose one spell-like ability at each spell level from the following list; the vessel can cast up to 14 spell levels' worth of these abilities per day.

    1st level (save DC 15) cause fear, charm person, mage armor, ray of enfeeblement
    2nd level (save DC 16) blindness/deafness, command undead, ghoul touch, invisibility
    3rd level (save DC 17) dispel magic, gaseous form, ray of exhaustion, vampiric touch
    4th level (save DC 18) confusion, contagion, crushing despair, enervation, fear
    5th level (save DC 19) dominate person, feeblemind, nightmare, waves of fatigue

    Here are a few common combinations of powers.

    Commander: charm person, confusion, dispel magic, dominate person, invisibility
    Brawler: enervation, ghoul touch, mage armor, vampiric touch, waves of fatigue
    Terror: blindness/deafness, cause fear, fear, feeblemind, gaseous form
  Quickness (Su): A vessel is supernaturally quick. It can take an extra standard
    action or move action during its turn each round. in combat, it normally uses
    this ability to make a second attack.
  Necrotic Blast (Su): A vessel can fire a blast of negative energy once per round
    as a ranged touch attack (100-ft. range, 5d6 negative energy damage).
desc_long: |-
  A bloodless vessel is an undead creature formed when agents of the dark powers infuse the prepared body of a virgin humanoid with the essence of multiple restless spirits. The vessel is physically and mentally empowered by the host of spirits possessing it, giving it surprising speed, deadly strength, and strange magic. While quite intelligent, bloodless vessels rarely speak or show signs of emotion. The spirits that are sharing the body have lost touch with their humanity due to the horrors they have suffered, and have difficulty summoning any strong emotion; their individual memories are remote, though the memories of things they have in common (such as historical events) remain quite strong.

  As the vessel suffers damage, flesh is cut away and bones may be broken, revealing pulsing threads of spectral energy running  through its veins instead of blood.  This is the concentrated essence of the spirits empowering the vessel, which can keep the vessel moving even after ghastly injuries. The necrotic blast attack used by a vessel draws on this same energy, literally hurling angry spirits at its victims.

---

# Bloodless Vessel
This pale youth’s wispy beard does little to make him look older. He stares with misty white eyes, and there is something unnatural about the way he stands, blank-faced and emotionless. He moves like a puppet, a thing _[[items/Weapon Magic Abilities/Guided|guided]]_ by _[[items/Weapon Magic Abilities/Unseen|unseen]]_ hands. He holds a _[[items/Weapon/Scythe|scythe]]_ that should be too heavy for his spindly arms, but the weight doesn’t seem to bother him.
**Source** Blood of Dragonscar pg. 30

NE Medium undead
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Listen +12, Spot +18

##### Defense

**AC** 24, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+4 _[[spells/Deflection|deflection]]_, +4 Dex, +6 natural)
**hp** 123 (18d12+6)
**Fort** +6, **Ref** +10, **Will** +14
**Immune** undead immunities

##### Offense
**Speed** 30 ft.
**Melee** _scythe_ +19 (2d4+13/19-20/x4) or slam +18 (1d6+9)
**Ranged** necrotic blast +14 ranged touch (5d6 negative energy damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th)
Varies

##### Statistics
**Str** 28, **Dex** 19, **Con** —, **Int** 14, **Wis** 16, **Cha** 19
**Base Atk** +9; **Grapple** +18
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Critical|Improved Critical]]_ (_scythe_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scythe_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +16, Concentration +14, Intimidate +18, _[[spells/Jump|Jump]]_ +19, Knowledge (arcana) +12, Knowledge (history) +15, Knowledge (religion) +10, Sense Motive +15, Spellcraft +10, Tumble +15
**Languages** Common and 1d4 other languages
**SQ** Host to Many

### Special Abilities

**Host to Many (Ex)** A _[[monsters/Bloodless Vessel|bloodless vessel]]_ is an undead creature, but it is host to many spirits. As such, it responds to turn attempts in an unusual manner. A successful turn attempt against the vessel drives away some of the inhabiting spirits for 1 minute (these flee visibly in the form of flying shadows, returning when the turn effect expires). This negates the vessel’s _deflection_ bonus to armor class for the duration of the turning.
**_Spell-like Abilities_ (Sp)** Between its undead nature and the diverse backgrounds of the spirits that comprise a vessel’s collective soul, a vessel has an unpredictable set of _spell-like abilities_. Some spread _[[universal monster rules/Fear|fear]]_ and disease, others focus on weakness and despair. Some have more in common with vampires, while others are more like ghouls. Choose one spell-like ability at each spell level from the following list; the vessel can cast up to 14 spell levels’ worth of these abilities per day.

1st level (save DC 15) _[[spells/Cause Fear|cause fear]]_, _[[spells/Charm Person|charm person]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_
2nd level (save DC 16) blindness/deafness, _[[spells/Command Undead|command undead]]_, _[[spells/Ghoul touch|ghoul touch]]_, _[[spells/Invisibility|invisibility]]_
3rd level (save DC 17) _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Gaseous Form|gaseous form]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_, _[[spells/Vampiric Touch|vampiric touch]]_
4th level (save DC 18) _[[spells/Confusion|confusion]]_, _[[spells/Contagion|contagion]]_, _[[spells/Crushing Despair|crushing despair]]_, _[[spells/Enervation|enervation]]_, _fear_
5th level (save DC 19) _[[spells/Dominate Person|dominate person]]_, _[[spells/Feeblemind|feeblemind]]_, _[[spells/Nightmare|nightmare]]_, _[[spells/Waves of Fatigue|waves of fatigue]]_

Here are a few common combinations of powers.

Commander: _charm person_, _confusion_, _dispel magic_, _dominate person_, _invisibility_
_[[classes/Brawler|Brawler]]_: _enervation_, _ghoul touch_, _mage armor_, _vampiric touch_, _waves of fatigue_
Terror: blindness/deafness, _cause fear_, _fear_, _feeblemind_, _gaseous form_

**Quickness (Su)** A vessel is supernaturally quick. It can take an extra standard action or move action during its turn each round. in combat, it normally uses this ability to make a second attack.

**Necrotic Blast (Su)** A vessel can fire a blast of negative energy once per round as a ranged touch attack (100-ft. range, 5d6 negative energy damage).

##### Description

A _bloodless vessel_ is an undead creature formed when agents of the dark powers infuse the prepared body of a virgin humanoid with the essence of multiple restless spirits. The vessel is physically and mentally empowered by the host of spirits possessing it, giving it surprising speed, _[[items/Weapon Magic Abilities/Deadly|deadly]]_ strength, and strange magic. While quite intelligent, bloodless vessels rarely speak or show signs of emotion. The spirits that are sharing the body have lost touch with their humanity due to the horrors they have suffered, and have difficulty summoning any strong emotion; their individual memories are remote, though the memories of things they have in common (such as historical events) remain quite strong.

As the vessel suffers damage, flesh is cut away and bones may be _[[conditions/Broken|broken]]_, revealing pulsing threads of spectral energy running through its veins instead of blood. This is the concentrated essence of the spirits empowering the vessel, which can keep the vessel moving even after ghastly injuries. The necrotic blast attack used by a vessel draws on this same energy, literally hurling angry spirits at its victims.