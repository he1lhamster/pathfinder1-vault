---
cssclass: [monsters]
title1: Egophage
desc_short: Eight tentacles ending in claws grow from the base of this glistening
  and gruesome floating brain.
title2: Egophage
CR: 10
sources:
- name: Occult Bestiary
  page: 26
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 9600
alignment: CE
size: Small
type: aberration
initiative:
  bonus: 11
senses:
  analyze aura: true
  darkvision: 60
AC:
  AC: 25
  touch: 19
  flat_footed: 17
  components:
    dex: 7
    dodge: 1
    natural: 6
    size: 1
HP:
  HP: 123
  long: 13d8+65
saves:
  fort: 9
  ref: 11
  will: 12
DR:
- amount: 10
  weakness: adamantine and magic
immunities:
- fire
- mind-affecting effects
resistances:
  cold: 20
  electricity: 20
  sonic: 20
SR: 25
weaknesses:
- vulnerable to protection from evil
speeds:
  base: 10
  fly: 50
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 8 claws +18 (1d4+2 plus attach [once per round if two or more claws hit
        the same creature])
      entries:
      - - damage: 1d4+2
        - effect: attach [once per round if two or more claws hit the same creature]
      count: 8
      attack: claws
      bonus:
      - 18
  special:
  - body thief
spell_like_abilities:
  entries:
  - superscripts:
    - OA
    name: analyze aura
    source: default
    freq: Constant
  - name: invisibility
    source: default
    freq: At will
  - name: reduce size
    source: default
    freq: At will
    other: as reduce person but self only and affects aberrations
  sources:
  - name: default
    CL: 10
psychic_magic:
  entries:
  - superscripts:
    - OA
    name: anticipate thoughts
    PE: 2
    DC: 16
  - superscripts:
    - OA
    name: ego whip IV
    PE: 6
    DC: 20
  - name: globe of invulnerability
    PE: 4
  - superscripts:
    - OA
    name: id insinuation III
    PE: 4
    DC: 17
  sources:
  - name: default
    CL: 10
    concentration: 14
  PE: 24
ability_scores:
  STR: 15
  DEX: 25
  CON: 21
  INT: 16
  WIS: 14
  CHA: 18
BAB: 9
CMB: 15
CMD: 28
feats:
- name: Agile Maneuvers
- name: Dodge
- name: Improved Initiative
- name: Iron Will
- name: Mobility
- name: Weapon Finesse
- name: Weapon Focus (claw)
skills:
  Bluff: 25
  Diplomacy: 24
  Disguise: 25
  Fly: 23
  Knowledge (local): 19
  Perception: 23
  Sense Motive: 15
  Stealth: 35
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 8
    Stealth:
      _: 8
languages:
- Aklo (can't speak)
- Common (can't speak)
- Undercommon (can't speak)
- telepathy 100 ft.
ecology:
  environment: any underground
  organization: solitary, brood (4-8), or tribe (10-30)
  treasure_type: double
special_abilities:
  Body Thief (Su): As a full-round action that provokes attacks of opportunity, an
    egophage can attempt to psychically force its way into a helpless, dead, or grappled
    creature. If successful, it attempts a psychically channeled coup de grace that
    inflicts 16d4+16 points of damage. If the victim is slain (or already dead), the
    egophage usurps control of the body as per greater possessionOA cast on a living
    body, with an unlimited duration. A host body may not have been dead for longer
    than 1 day for this ability to function, and even successfully inhabited bodies
    decay to uselessness in 7 days (unless this time is extended via a gentle repose
    spell). As long as the egophage occupies the body, it knows and can speak any
    language known by the victim, and also knows basic information about the victim's
    identity and personality, though it has none of the victim's specific memories
    or knowledge. Once possessed, the host regains its full hit points-despite the
    fact that it's technically a corpse, it appears, detects, and acts as a living
    creature of its type. Damage done to a host does not harm the egophage, and if
    the host body is slain, the egophage emerges and is dazed for 1 round. Raise dead
    cannot restore a victim of body theft, but resurrection or more powerful magic
    can.
  Vulnerable to Protection from Evil (Ex): An egophage is treated as a summoned creature
    for the purpose of determining how it is affected by a protection from evil spell.
desc_long: 'When an intellect devourer gorges heavily on midnight milk (Pathfinder
  Campaign Setting: Lost Cities of Golarion 11), it sometimes develops increased psychic
  abilities, including the ability to fly, and has its stubby clawed legs stretch
  into tentacles. These sinister aberrations are called egophages, and delight in
  wearing other creatures like suits to fulfill their demented whims and schemes.'

---

# Egophage
Eight tentacles ending in claws grow from the base of this glistening and gruesome floating brain.
**Source** Occult Bestiary pg. 26
**XP** 9,600
CE Small aberration
**Init** +11; **Senses** _[[spells/Analyze Aura|analyze aura]]_, _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +23

##### Defense

**AC** 25, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+7 Dex, +1 dodge, +6 natural, +1 size)
**hp** 123 (13d8+65)
**Fort** +9, **Ref** +11, **Will** +12
**DR** 10/adamantine and magic; **Immune** fire, mind-affecting effects; **Resist** cold 20, electricity 20, sonic 20; **SR** 25
**Weaknesses** vulnerable to _[[spells/Protection From Evil|protection from evil]]_

##### Offense
**Speed** 10 ft., fly 50 ft. (perfect)
**Melee** 8 claws +18 (1d4+2 plus _[[universal monster rules/Attach|attach]]_ [once per round if two or more claws hit the same creature])
**Special Attacks** body thief
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th)
Constant—_analyze aura_
At will—_[[spells/Invisibility|invisibility]]_, reduce size (as _[[spells/Reduce Person|reduce person]]_ but self only and affects aberrations)
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_ **(CL 10th, concentration +14)
24 PE—_[[spells/Anticipate Thoughts|anticipate thoughts]]_ (2 PE, DC 16), _[[spells/Ego _[[items/Weapon/Whip|Whip]]_ IV|ego _whip_ IV]]_ (6 PE, DC 20), _[[spells/Globe Of Invulnerability|globe of invulnerability]]_ (4 PE), _[[spells/Id Insinuation III|id insinuation III]]_ (4 PE, DC 17)

##### Statistics
**Str** 15, **Dex** 25, **Con** 21, **Int** 16, **Wis** 14, **Cha** 18
**Base Atk** +9; **CMB** +15; **CMD** 28
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Bluff +25, Diplomacy +24, Disguise +25, Fly +23, Knowledge (local) +19, Perception +26, Sense Motive +15, Stealth +35; **Racial Modifiers** +8 Bluff, +8 Perception, +8 Stealth
**Languages** Aklo (can’t speak), Common (can’t speak), Undercommon (can’t speak); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any underground
**Organization** solitary, brood (4–8), or tribe (10–30)
**Treasure** double

### Special Abilities

**Body Thief (Su)** As a full-round action that provokes attacks of opportunity, an _[[monsters/Egophage|egophage]]_ can attempt to psychically force its way into a _[[conditions/Helpless|helpless]]_, dead, or _[[conditions/Grappled|grappled]]_ creature. If successful, it attempts a psychically channeled coup de _[[spells/Grace|grace]]_ that inflicts 16d4+16 points of damage. If the victim is slain (or already dead), the _egophage_ usurps control of the body as per greater _[[spells/Possession|possession]]_ cast on a living body, with an unlimited duration. A host body may not have been dead for longer than 1 day for this ability to function, and even successfully inhabited bodies decay to uselessness in 7 days (unless this time is extended via a _[[spells/Gentle Repose|gentle repose]]_ spell). As long as the _egophage_ occupies the body, it knows and can speak any language known by the victim, and also knows basic information about the victim’s identity and personality, though it has none of the victim’s specific memories or knowledge. Once possessed, the host regains its full hit points—despite the fact that it’s technically a corpse, it appears, detects, and acts as a living creature of its type. Damage done to a host does not _[[spells/Harm|harm]]_ the _egophage_, and if the host body is slain, the _egophage_ emerges and is _[[conditions/Dazed|dazed]]_ for 1 round. _[[spells/Raise Dead|Raise dead]]_ cannot restore a victim of body theft, but _[[spells/Resurrection|resurrection]]_ or more powerful magic can.

**Vulnerable to _Protection from Evil_ (Ex)** An _egophage_ is treated as a summoned creature for the purpose of determining how it is affected by a _protection from evil_ spell.

##### Description

When an _[[monsters/Intellect Devourer|intellect devourer]]_ gorges heavily on midnight milk (Pathfinder Campaign Setting: Lost Cities of Golarion 11), it sometimes develops increased _[[classes/Psychic|psychic]]_ abilities, including the ability to fly, and has its stubby clawed legs stretch into tentacles. These sinister aberrations are _[[items/Weapon Magic Abilities/Called|called]]_ egophages, and delight in wearing other creatures like suits to fulfill their demented whims and schemes.