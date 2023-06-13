---
cssclass: [monsters]
title1: Vampire, Vetala
desc_short: With its bloodless flesh and eyes the color of deepest night, this imperious
  being obviously no longer numbers among the living.
title2: Vetala
CR: 6
sources:
- name: Inner Sea Bestiary
  page: 54
  link: http://paizo.com/products/btpy8v2x?Pathfinder-Campaign-Setting-Inner-Sea-Bestiary
XP: 2400
race: Female
classes:
- human vetala oracle 5
alignment: NE
size: Medium
type: undead
subtypes:
- augmented humanoid
- human
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 21
  touch: 13
  flat_footed: 18
  components:
    armor: 4
    dex: 2
    dodge: 1
    natural: 4
HP:
  HP: 61
  long: 5d8+35
  fast_healing: 5
saves:
  fort: 8
  ref: 4
  will: 6
defensive_abilities:
- channel resistance +4
DR:
- amount: 10
  weakness: magic and good
immunities:
- undead traits
resistances:
  electricity: 10
  fire: 10
weaknesses:
- vetala weaknesses
speeds:
  base: 30
  climb: 30
attacks:
  melee:
  - - text: 2 claws +7 (1d6+4 plus paralysis)
      entries:
      - - damage: 1d6+4
        - effect: paralysis
      count: 2
      attack: claws
      bonus:
      - 7
  special:
  - drain prana (DC 18)
  - malevolence
  - paralysis (1d4+1 rounds, DC 18)
  - possess corpse
spells:
  entries:
  - name: death knell
    source: Oracle
    level: 2
    DC: 18
  - name: false life
    source: Oracle
    level: 2
  - name: inflict moderate wounds
    source: Oracle
    level: 2
    DC: 18
  - name: levitate
    source: Oracle
    level: 2
  - name: minor image
    source: Oracle
    level: 2
    DC: 18
  - name: silence
    source: Oracle
    level: 2
    DC: 18
  - name: cause fear
    source: Oracle
    level: 1
    DC: 17
  - name: command
    source: Oracle
    level: 1
    DC: 17
  - name: doom
    source: Oracle
    level: 1
    DC: 17
  - name: inflict light wounds
    source: Oracle
    level: 1
    DC: 17
  - name: obscuring mist
    source: Oracle
    level: 1
  - name: shield of faith
    source: Oracle
    level: 1
  - name: bleed
    source: Oracle
    level: 0
    DC: 16
  - name: detect magic
    source: Oracle
    level: 0
  - name: ghost sound
    source: Oracle
    level: 0
  - name: guidance
    source: Oracle
    level: 0
  - name: light
    source: Oracle
    level: 0
  - name: mage hand
    source: Oracle
    level: 0
  - name: read magic
    source: Oracle
    level: 0
  - name: resistance
    source: Oracle
    level: 0
  sources:
  - name: Oracle
    type: known
    CL: 5
    concentration: 11
    slots:
      2: 6
      1: 8
      0: at-will
    mystery: bones
ability_scores:
  STR: 18
  DEX: 15
  CON:
  INT: 16
  WIS: 12
  CHA: 22
BAB: 3
CMB: 7
CMD: 20
feats:
- is_bonus: true
  name: Alertness
- is_bonus: true
  name: Blind-Fight
- name: Combat Casting
- is_bonus: true
  name: Deceitful
- name: Dodge
- name: Extra Revelation
- is_bonus: true
  name: Improved Initiative
- name: Mobility
- is_bonus: true
  name: Skill Focus (Disguise)
skills:
  Bluff: 16
  Climb: 10
  Diplomacy: 14
  Disguise: 27
  Knowledge (religion): 11
  Perception: 16
  Sense Motive: 19
  Spellcraft: 11
  Stealth: 16
  _racial_mods:
    Disguise:
      _: 8
    Perception:
      _: 8
    Sense Motive:
      _: 8
    Stealth:
      _: 8
languages:
- Common
- Infernal
- Vudrani
special_qualities:
- oracle's curse (haunted)
- revelations (death's touch, undead servitude, voice of the grave)
ecology:
  environment: any (Vudra)
  organization: solitary
  treasure_type: NPC Gear
  treasure:
  - chain shirt
  - cloak of resistance +1
  - potions of invisibility [2]
  - other treasure
desc_long: |-
  While most of the Inner Sea's vampires lust for living blood, the mysterious vetalas hunger for a more intangible force: the energy that infuses mortal minds. Referred to as consciousness or psyche by some, the academics of Vudra- from where most vetalas hail-call this fundamental vital force prana. Regardless of their desire's name, vetalas prey upon those who show creative promise, possess potent force of will, or seem destined for greatness, draining the most brilliant sources of mortal light to fuel their own unnatural embers. Their dark mastery of life force allows vetalas to possess corpses or even overwhelm the minds of living creatures. With these stolen masks and the resources of abducted lives, they work their foul wills.

  Vetalas are said to be the spirits of children “born evil,” who never received burial rites upon their deaths. Sometimes one of these evil spirits takes hold of a corpse- not necessarily its own-which becomes its anchor to the mortal world. Such young souls seek out experiences and life energy, becoming as wicked as any other vampire as they endlessly indulge their profane, deathless desires.

---

# Vampire, Vetala
With its bloodless flesh and eyes the color of deepest night, this imperious being obviously no longer numbers among the living.
**Source** Inner Sea Bestiary pg. 54
**XP** 2,400
Female human vetala _[[classes/Oracle|oracle]]_ 5

NE Medium undead (augmented humanoid, human)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +16

##### Defense

**AC** 21, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 61 (5d8+35); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +8, **Ref** +4, **Will** +6
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 10/magic and good; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** electricity 10, fire 10
**Weaknesses** vetala weaknesses

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** 2 claws +7 (1d6+4 plus _[[universal monster rules/Paralysis|paralysis]]_)
**Special Attacks** drain prana (DC 18), malevolence, _paralysis_ (1d4+1 rounds, DC 18), possess corpse
**_Oracle_ Spells Known **(CL 5th; concentration +11)
2nd (6/day)—_[[spells/Death Knell|death knell]]_ (DC 18), _[[spells/False Life|false life]]_, _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_ (DC 18), _[[spells/Levitate|levitate]]_, _[[spells/Minor Image|minor image]]_ (DC 18), _[[spells/Silence|silence]]_ (DC 18)
1st (8/day)—_[[spells/Cause Fear|cause fear]]_ (DC 17), _[[spells/Command|command]]_ (DC 17), _[[spells/Doom|doom]]_ (DC 17), _[[spells/Inflict Light Wounds|inflict light wounds]]_ (DC 17), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**Mystery **bones

##### Statistics
**Str** 18, **Dex** 15, **Con** —, **Int** 16, **Wis** 12, **Cha** 22
**Base Atk** +3; **CMB** +7; **CMD** 20
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Deceitful|Deceitful]]_, _Dodge_, _[[feats/Extra Revelation|Extra Revelation]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Skill Focus|Skill Focus]]_ (Disguise)
**Skills** Bluff +16, _Climb_ +10, Diplomacy +14, Disguise +27, Knowledge (religion) +11, Perception +16, Sense Motive +19, Spellcraft +11, Stealth +16; **Racial Modifiers** +8 Disguise, +8 Perception, +8 Sense Motive, +8 Stealth
**Languages** Common, Infernal, Vudrani
**SQ** _oracle_’s curse (haunted), revelations (death’s touch, undead servitude, voice of the grave)

##### Ecology

**Environment** any (Vudra)
**Organization** solitary
**Treasure** NPC gear (_[[items/Armor/Chain shirt|chain shirt]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, potions of _[[spells/Invisibility|invisibility]]_ [2], other treasure)

##### Description

While most of the Inner Sea’s vampires lust for living blood, the mysterious vetalas hunger for a more intangible force: the energy that infuses mortal minds. Referred to as consciousness or psyche by some, the academics of Vudra— from where most vetalas hail—call this fundamental vital force prana. Regardless of their desire’s name, vetalas prey upon those who show creative promise, possess _[[items/Weapon Magic Abilities/Potent|potent]]_ force of will, or seem destined for greatness, draining the most brilliant sources of mortal light to fuel their own unnatural embers. Their dark mastery of life force allows vetalas to possess corpses or even _[[feats/Overwhelm|overwhelm]]_ the minds of living creatures. With these stolen masks and the resources of abducted lives, they work their foul wills.

Vetalas are said to be the spirits of children “born evil,” who never received burial rites upon their deaths. Sometimes one of these evil spirits takes hold of a corpse— not necessarily its own—which becomes its anchor to the mortal world. Such young souls seek out experiences and life energy, becoming as wicked as any other _[[monsters/Vampire|vampire]]_ as they endlessly indulge their profane, _[[spells/Deathless|deathless]]_ desires.