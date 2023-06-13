---
cssclass: [monsters]
title1: Naga, Royal Naga
desc_short: This snake-bodied creature has five necks, each with a regal, humanoid
  face in a cobralike hood.
title2: Royal Naga
CR: 11
sources:
- name: Bestiary 3
  page: 198
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: 'Pathfinder #27: What Lies in Dust'
  page: 88
  link: http://paizo.com/pathfinder/adventurePath/councilOfThieves/v5748btpy8b8h
XP: 12800
alignment: LN
size: Huge
type: aberration
subtypes:
- shapechanger
initiative:
  bonus: 7
senses:
  darkvision: 60
  see invisibility: true
AC:
  AC: 26
  touch: 11
  flat_footed: 23
  components:
    dex: 3
    natural: 15
    size: -2
HP:
  HP: 133
  long: 14d8+70
saves:
  fort: 9
  ref: 9
  will: 15
speeds:
  base: 40
attacks:
  melee:
  - - text: 5 bites +14 (2d6+6 plus bleed)
      entries:
      - - damage: 2d6+6
        - effect: bleed
      count: 5
      attack: bites
      bonus:
      - 14
  special:
  - bleed (1d6)
  - dual gaze
  - rend (3 bites, 2d6+9)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 9
    concentration: 13
spells:
  entries:
  - name: arcane eye
    source: '?'
    level: 4
  - name: charm monster
    source: '?'
    level: 4
    DC: 18
  - name: blink
    source: '?'
    level: 3
  - name: dispel magic
    source: '?'
    level: 3
  - name: suggestion
    source: '?'
    level: 3
    DC: 17
  - name: enthrall
    source: '?'
    level: 2
    DC: 16
  - name: hold person
    source: '?'
    level: 2
    DC: 16
  - name: invisibility
    source: '?'
    level: 2
  - name: scorching ray
    source: '?'
    level: 2
  - name: charm person
    source: '?'
    level: 1
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
    DC: 15
  - name: shield
    source: '?'
    level: 1
  - name: daze
    source: '?'
    level: 0
    DC: 14
  - name: detect magic
    source: '?'
    level: 0
  - name: flare
    source: '?'
    level: 0
    DC: 14
  - name: mage hand
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: open/close
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: touch of fatigue
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 9
    concentration: 13
    slots:
      4: 5
      3: 7
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 23
  DEX: 17
  CON: 21
  INT: 18
  WIS: 22
  CHA: 19
BAB: 10
CMB: 18
CMB_other: +22 grapple
CMD: 31
CMD_other: can't be tripped
feats:
- name: Alertness
- name: Blind-Fight
- name: Combat Casting
- name: Combat Reflexes
- is_bonus: true
  name: Eschew Materials
- name: Improved Initiative
- name: Lightning Reflexes
- name: Stand Still
skills:
  Acrobatics: 20
    when jumping: 24
  Bluff: 18
  Diplomacy: 18
  Knowledge (arcana): 18
  Knowledge (history): 11
  Knowledge (nobility): 11
  Perception: 27
  Sense Motive: 24
  Stealth: 12
languages:
- Celestial
- Common
- Infernal
special_qualities:
- change shape (five humanoid shapes; alter self)
ecology:
  environment: any land
  organization: solitary
  treasure_type: standard
special_abilities:
  Change Shape (Su): A royal naga can use this ability to take one of five specific
    humanoid forms. Each of these forms has a unique appearance (such as a female
    dwarf with red hair, an elderly male human, and so on) and the naga can only use
    this ability to assume these five forms. The naga can still use its dual gaze
    in humanoid form.
  Dual Gaze (Su): A royal naga has a piercing stare capable of crippling those that
    meet its gazes. The creature has two gaze attacks and can switch between them
    as a move action. One gaze causes those that succumb to it to become permanently
    blinded, while the other causes those that succumb to be permanently deafened.
    A DC 21 Fortitude save negates the effects of either gaze; otherwise, the effects
    are permanent until cured. Royal nagas generally prefer to keep their deafening
    gaze active, switching to the blindness gaze once combat begins and some of their
    foes have already been deafened, since those who are blinded can no longer be
    harmed by gaze attacks. The save DC is Charisma-based.
  Spells: A royal naga casts spells as a 9th-level sorcerer.
desc_long: |-
  Regal and proud, royal nagas haunt lost cities and forgotten kingdoms, guarding ancient treasures for their own inscrutable reasons. A royal naga's five faces are sharp and fierce, taking on a terrifying countenance when it becomes angered. Bespeaking their innate pride and vanity, royal nagas adorn their serpentine hoods and faces with elaborate and valuable piercings, crowns, or other precious accessories. Royal nagas are 18 feet long, and often weigh more than 750 pounds.

  Royal nagas tend to be stern in nature and commanding in speech. Although naturally sociable, they are distrustful of strangers and seem to have great difficulty speaking to other creatures as equals.

---

# Naga, Royal Naga
This snake-bodied creature has five necks, each with a regal, humanoid face in a cobralike hood.
**Source** Bestiary 3 pg. 198, Pathfinder #27: What Lies in Dust pg. 88
**XP** 12,800

LN Huge aberration (shapechanger)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +27

##### Defense

**AC** 26, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+3 Dex, +15 natural, –2 size)
**hp** 133 (14d8+70)
**Fort** +9, **Ref** +9, **Will** +15

##### Offense
**Speed** 40 ft.
**Melee** 5 bites +14 (2d6+6 plus _[[universal monster rules/Bleed|bleed]]_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _bleed_ (1d6), dual _[[universal monster rules/Gaze|gaze]]_, _[[universal monster rules/Rend|rend]]_ (3 bites, 2d6+9)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +13)
Constant—_see invisibility_
**Spells Known **(CL 9th; concentration +13)
4th (5/day)—_[[spells/Arcane Eye|arcane eye]]_, _[[spells/Charm Monster|charm monster]]_ (DC 18)
3rd (7/day)—_[[spells/Blink|blink]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Suggestion|suggestion]]_ (DC 17)
2nd (7/day)—_[[spells/Enthrall|enthrall]]_ (DC 16), _[[spells/Hold Person|hold person]]_ (DC 16), _[[spells/Invisibility|invisibility]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (7/day)—_[[spells/Charm Person|charm person]]_ (DC 15), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 15), _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Daze|daze]]_ (DC 14), _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 14), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, open/close, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_

##### Statistics
**Str** 23, **Dex** 17, **Con** 21, **Int** 18, **Wis** 22, **Cha** 19
**Base Atk** +10; **CMB** +18 (+22 grapple); **CMD** 31 (can’t be tripped)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Stand Still|Stand Still]]_
**Skills** Acrobatics +20 (+24 when jumping), Bluff +18, Diplomacy +18, Knowledge (arcana) +18, Knowledge (history) +11, Knowledge (nobility) +11, Perception +27, Sense Motive +24, Stealth +12
**Languages** Celestial, Common, Infernal
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (five humanoid shapes; _[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** any land
**Organization** solitary
**Treasure** standard

### Special Abilities

**_Change Shape_ (Su)** A royal naga can use this ability to take one of five specific humanoid forms. Each of these forms has a unique appearance (such as a female dwarf with red hair, an elderly male human, and so on) and the naga can only use this ability to assume these five forms. The naga can still use its dual _gaze_ in humanoid form.

**Dual _Gaze_ (Su)** A royal naga has a piercing stare capable of crippling those that meet its gazes. The creature has two _gaze_ attacks and can switch between them as a move action. One _gaze_ causes those that succumb to it to become permanently _[[conditions/Blinded|blinded]]_, while the other causes those that succumb to be permanently _[[conditions/Deafened|deafened]]_. A DC 21 Fortitude save negates the effects of either _gaze_; otherwise, the effects are permanent until cured. Royal nagas generally prefer to keep their deafening _gaze_ active, switching to the blindness _gaze_ once combat begins and some of their foes have already been _deafened_, since those who are _blinded_ can no longer be harmed by _gaze_ attacks. The save DC is Charisma-based.
**Spells **A royal naga casts spells as a 9th-level _[[classes/Sorcerer|sorcerer]]_.

##### Description

Regal and proud, royal nagas haunt lost cities and forgotten kingdoms, _[[items/Armor Magic Abilities/Guarding|guarding]]_ ancient treasures for their own inscrutable reasons. A royal naga’s five faces are sharp and fierce, taking on a terrifying countenance when it becomes angered. Bespeaking their innate pride and vanity, royal nagas adorn their serpentine hoods and faces with elaborate and valuable piercings, crowns, or other precious accessories. Royal nagas are 18 feet long, and often weigh more than 750 pounds.

Royal nagas tend to be stern in nature and commanding in speech. Although naturally _[[feats/Sociable|sociable]]_, they are distrustful of strangers and seem to have great difficulty speaking to other creatures as equals.