---
cssclass: [monsters]
title1: Demon, Shadow Demon
desc_short: Only this shadowy bat-winged demon's teeth and claws have any sense of
  physicality to them-the rest is lost in darkness.
title2: Shadow Demon
CR: 7
sources:
- name: Pathfinder RPG Bestiary
  page: 67
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 3200
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
- incorporeal
initiative:
  bonus: 8
senses:
  darkvision: 60
AC:
  AC: 18
  touch: 18
  flat_footed: 14
  components:
    deflection: 4
    dex: 4
HP:
  HP: 59
  long: 7d10+21
saves:
  fort: 5
  ref: 11
  will: 7
defensive_abilities:
- incorporeal
DR:
- amount: 10
  weakness: cold iron or good
immunities:
- cold
- electricity
- poison
resistances:
  acid: 10
  fire: 10
SR: 17
weaknesses:
- sunlight powerlessness
speeds:
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +11 touch (1d6 plus 1d6 cold)
      entries:
      - - damage: 1d6
        - damage: 1d6
          type: cold
      count: 2
      attack: claws
      bonus:
      - 11
      touch: true
    - text: bite +11 touch (1d8 plus 1d6 cold)
      entries:
      - - damage: 1d8
        - damage: 1d6
          type: cold
      attack: bite
      bonus:
      - 11
      touch: true
  special:
  - pounce
  - sprint
  - shadow blend
spell_like_abilities:
  entries:
  - name: deeper darkness
    source: default
    freq: At will
  - name: fear
    source: default
    freq: At will
    DC: 18
  - name: greater teleport
    source: default
    freq: At will
    other: self only
  - name: telekinesis
    source: default
    freq: At will
    DC: 19
  - name: shadow conjuration
    source: default
    freq: 3/day
    DC: 18
  - name: shadow evocation
    source: default
    freq: 3/day
    DC: 19
  - name: magic jar
    source: default
    freq: 1/day
    DC: 19
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: shadow demon
      amount: 1
      chance: 50%
  sources:
  - name: default
    CL: 10
ability_scores:
  STR:
  DEX: 18
  CON: 17
  INT: 14
  WIS: 14
  CHA: 19
BAB: 7
CMB: 11
CMD: 25
feats:
- name: Blind-Fight
- name: Combat Reflexes
- name: Improved Initiative
- name: Lightning Reflexes,
skills:
  Acrobatics: 14
  Bluff: 14
  Fly: 22
  Knowledge (local): 12
  Knowledge (planes): 12
  Perception: 20
  Sense Motive: 12
  Stealth: 14
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Common
- telepathy 100 ft.
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or haunt (3-8)
  treasure_type: standard
special_abilities:
  Sprint (Ex): Once per minute, a shadow demon increase its fly speed to 240 feet
    for 1 round.
  Shadow Blend (Su): During any conditions other than bright light, a shadow demon
    can disappear into the shadows as a move-equivalent action, effectively becoming
    invisible. Artificial illumination or light spells of 2nd level or lower do not
    negate this ability.
  Sunlight Powerlessness (Ex): A shadow demon is utterly powerless in bright light
    or natural sunlight and flees from it. A shadow demon caught in such light cannot
    attack and can take only a single move or standard action. A shadow demon that
    is possessing a creature using magic jar is not harmed by sunlight, but if it
    is struck by a sunbeam or sunburst spell while possessing a creature, the shadow
    demon is driven out of its host automatically.
desc_long: |-
  Tales of demonic possession are common, used often by the ignorant to explain strange or violent behavior. While the majority of such cases are merely manifestations of madness or derangement, those that are legitimate possessions are often the work of shadow demons.

  Unlike many demons, shadow demons are incorporeal. When a particularly envious and evil mortal soul is pulled into the Abyss, it is transformed, split apart, and combined with other souls until what emerges is little more than jealous malevolence without the impediment of a physical body.

---

# Demon, Shadow Demon
Only this shadowy bat-winged demon’s teeth and claws have any sense of physicality to them—the rest is lost in _[[spells/Darkness|darkness]]_.
**Source** Pathfinder RPG Bestiary pg. 67
**XP** 3,200
CE Medium outsider (chaotic, demon, evil, extraplanar, _[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +20

##### Defense

**AC** 18, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 _[[spells/Deflection|deflection]]_, +4 Dex)
**hp** 59 (7d10+21)
**Fort** +5, **Ref** +11, **Will** +7
**Defensive Abilities** _incorporeal_; **DR** 10/cold iron or good; **Immune** cold, electricity, poison; **Resist** acid 10, fire 10; **SR** 17
**Weaknesses** _[[universal monster rules/Sunlight Powerlessness|sunlight powerlessness]]_

##### Offense
**Speed** fly 40 ft. (perfect)
**Melee** 2 claws +11 touch (1d6 plus 1d6 cold), bite +11 touch (1d8 plus 1d6 cold)
**Special Attacks** _[[universal monster rules/Pounce|pounce]]_, sprint, _[[items/Armor Magic Abilities/Shadow|shadow]]_ _[[spells/Blend|blend]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th)
At will—_[[spells/Deeper Darkness|deeper darkness]]_, _[[universal monster rules/Fear|fear]]_ (DC 18), greater teleport (self only), _[[spells/Telekinesis|telekinesis]]_ (DC 19)
3/day—_[[spells/Shadow Conjuration|shadow conjuration]]_ (DC 18), _[[spells/Shadow Evocation|shadow evocation]]_ (DC 19)
1/day—_[[spells/Magic Jar|magic jar]]_ (DC 19), _[[universal monster rules/Summon|summon]]_ (level 3, 1 _shadow_ demon 50%)

##### Statistics
**Str** —, **Dex** 18, **Con** 17, **Int** 14, **Wis** 14, **Cha** 19
**Base Atk** +7; **CMB** +11; **CMD** 25
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, 
**Skills** Acrobatics +14, Bluff +14, Fly +22, Knowledge (local) +12, Knowledge (planes) +12, Perception +20, Sense Motive +12, Stealth +14; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Common; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or haunt (3–8)
**Treasure** standard

### Special Abilities
**Sprint (Ex)** Once per minute, a _shadow_ demon increase its fly speed to 240 feet for 1 round.
**_Shadow_ _Blend_ (Su)** During any conditions other than bright light, a _shadow_ demon can disappear into the shadows as a move-equivalent action, effectively becoming _[[conditions/Invisible|invisible]]_. Artificial illumination or light spells of 2nd level or lower do not negate this ability.
**_Sunlight Powerlessness_ (Ex)** A _shadow_ demon is utterly powerless in bright light or natural sunlight and flees from it. A _shadow_ demon caught in such light cannot attack and can take only a single move or standard action. A _shadow_ demon that is possessing a creature using _magic jar_ is not harmed by sunlight, but if it is struck by a _[[spells/Sunbeam|sunbeam]]_ or _[[spells/Sunburst|sunburst]]_ spell while possessing a creature, the _shadow_ demon is driven out of its host automatically.

##### Description

Tales of _[[feats/Demonic Possession|demonic possession]]_ are common, used often by the ignorant to explain strange or violent behavior. While the majority of such cases are merely manifestations of madness or derangement, those that are legitimate possessions are often the work of _shadow_ demons.

Unlike many demons, _shadow_ demons are _incorporeal_. When a particularly envious and evil mortal soul is pulled into the Abyss, it is transformed, _[[universal monster rules/Split|split]]_ apart, and combined with other souls until what emerges is little more than jealous malevolence without the impediment of a physical body.