---
cssclass: [monsters]
title1: Ankou
desc_short: Cloaked by wings of darkness, this horrific, skeletal creature appears
  to burn from within.
title2: Ankou
CR: 14
sources:
- name: Bestiary 4
  page: 10
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: 'Pathfinder #36: Sound of a Thousand Screams'
  page: 80
  link: http://paizo.com/pathfinder/adventurePath/kingmaker/v5748btpy8b7x
XP: 38400
alignment: LE
size: Large
type: fey
subtypes:
- extraplanar
initiative:
  bonus: 13
senses:
  blindsense: 120
  low-light vision: true
AC:
  AC: 31
  touch: 19
  flat_footed: 21
  components:
    dex: 9
    dodge: 1
    natural: 12
    size: -1
HP:
  HP: 133
  long: 14d6+84
saves:
  fort: 10
  ref: 18
  will: 13
DR:
- amount: 10
  weakness: cold iron
speeds:
  fly: 90
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +14 (1d6+8)
      entries:
      - - damage: 1d6+8
      count: 2
      attack: claws
      bonus:
      - 14
    - text: tail slap +9 (1d8+4 plus bleed)
      entries:
      - - damage: 1d8+4
        - effect: bleed
      attack: tail slap
      bonus:
      - 9
    - text: 2 wings +9 (1d8+4 plus bleed)
      entries:
      - - damage: 1d8+4
        - effect: bleed
      count: 2
      attack: wings
      bonus:
      - 9
  special:
  - bleed (2d6)
  - cold iron killer
  - shadow doubles
  - sneak attack +3d6
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: deeper darkness
    source: default
    freq: At will
  - name: ray of exhaustion
    source: default
    freq: At will
    DC: 20
  - name: silence
    source: default
    freq: At will
    other: self only
  - name: dimensional anchor
    source: default
    freq: 3/day
  - name: greater teleport
    source: default
    freq: 3/day
  - name: true seeing
    source: default
    freq: 3/day
  - name: circle of death
    source: default
    freq: 1/day
    DC: 23
  - name: discern location
    source: default
    freq: 1/day
  - name: prismatic spray
    source: default
    freq: 1/day
    DC: 24
  sources:
  - name: default
    CL: 15
    concentration: 22
ability_scores:
  STR: 26
  DEX: 28
  CON: 22
  INT: 17
  WIS: 19
  CHA: 25
BAB: 7
CMB: 16
CMD: 36
feats:
- name: Blind-Fight
- name: Combat Reflexes
- name: Dodge
- name: Flyby Attack
- name: Improved Initiative
- name: Lightning Stance
- name: Wind Stance
skills:
  Bluff: 24
  Escape Artist: 26
  Fly: 32
  Intimidate: 21
  Knowledge (nature): 20
  Knowledge (planes): 17
  Perception: 21
  Sense Motive: 21
  Stealth: 22
languages:
- Common
- Sylvan (can't speak any language)
- telepathy 100 ft.
ecology:
  environment: any (primal land of fey)
  organization: solitary
  treasure_type: standard
special_abilities:
  Cold Iron Killer (Su): All of an ankou's natural weapons are treated as cold iron
    for the purpose of overcoming damage reduction.
  Shadow Doubles (Su): Once per day as a free action, an ankou can conjure up to four
    shadowy duplicates, which appear anywhere within 60 feet of the ankou and last
    a number of rounds equal to the ankou's Charisma modifier (typically 7 rounds).
    These shadow doubles are identical to the original in all respects except that
    when conjured they have a number of hit points equal to 20% of the true ankou's
    total hit points (26 hit points if conjured by an ankou with full hit points).
    The doubles have all of the true ankou's melee attacks and abilities, except they
    can't create more shadow doubles or use the ankou's spell-like abilities except
    for deeper darkness. Any creature that interacts with a shadow double can attempt
    a Will save to disbelieve the duplicate (DC 10 + 1/2 the ankou's Hit Dice + the
    ankou's Charisma modifier, typically DC 24). Against a creature that recognizes
    a shadow double for what it is, the double functions as a shadow conjuration (Pathfinder
    RPG Core Rulebook 340). Shadow doubles take double damage from spells with the
    light descriptor. If the true ankou is slain, is rendered unconscious, or is ever
    more than 120 feet from a shadow double, the duplicates instantly vanish.
desc_long: Ankous are assassins for powerful fey nobles, sent to kill, terrify, and
  torture. They never speak, only telepathically whisper their lord's verdict to victims.
  A typical ankou is 10 feet tall and has an 8-foot wingspan, but weighs less than
  100 pounds.

---

# Ankou
Cloaked by wings of _[[spells/Darkness|darkness]]_, this horrific, skeletal creature appears to _[[universal monster rules/Burn|burn]]_ from within.
**Source** Bestiary 4 pg. 10, Pathfinder #36: Sound of a Thousand Screams pg. 80
**XP** 38,400

LE Large fey (extraplanar)
**Init** +13; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +21

##### Defense

**AC** 31, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+9 Dex, +1 dodge, +12 natural, –1 size)
**hp** 133 (14d6+84)
**Fort** +10, **Ref** +18, **Will** +13
**DR** 10/cold iron

##### Offense
**Speed** fly 90 ft. (perfect)
**Melee** 2 claws +14 (1d6+8), tail slap +9 (1d8+4 plus _[[universal monster rules/Bleed|bleed]]_), 2 wings +9 (1d8+4 plus _bleed_)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _bleed_ (2d6), cold iron killer, _[[items/Armor Magic Abilities/Shadow|shadow]]_ doubles, sneak attack +3d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +22)
At will—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 20), _[[spells/Silence|silence]]_ (self only)
3/day—_[[spells/Dimensional Anchor|dimensional anchor]]_, greater teleport, _[[spells/True Seeing|true seeing]]_
1/day—_[[spells/Circle Of Death|circle of death]]_ (DC 23), _[[spells/Discern Location|discern location]]_, _[[spells/Prismatic Spray|prismatic spray]]_ (DC 24)

##### Statistics
**Str** 26, **Dex** 28, **Con** 22, **Int** 17, **Wis** 19, **Cha** 25
**Base Atk** +7; **CMB** +16; **CMD** 36
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Stance|Lightning Stance]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Bluff +24, Escape Artist +26, Fly +32, Intimidate +21, Knowledge (nature) +20, Knowledge (planes) +17, Perception +21, Sense Motive +21, Stealth +22
**Languages** Common, Sylvan (can’t speak any language); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (primal land of fey)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Cold Iron Killer (Su)** All of an _[[monsters/Ankou|ankou]]_’s natural weapons are treated as cold iron for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_.
**_Shadow_ Doubles (Su)** Once per day as a free action, an _ankou_ can conjure up to four shadowy duplicates, which appear anywhere within 60 feet of the _ankou_ and last a number of rounds equal to the _ankou_’s Charisma modifier (typically 7 rounds). These _shadow_ doubles are identical to the original in all respects except that when conjured they have a number of hit points equal to 20% of the true _ankou_’s total hit points (26 hit points if conjured by an _ankou_ with full hit points). The doubles have all of the true _ankou_’s melee attacks and abilities, except they can’t create more _shadow_ doubles or use the _ankou_’s _spell-like abilities_ except for _deeper darkness_. Any creature that interacts with a _shadow_ double can attempt a Will save to disbelieve the duplicate (DC 10 + 1/2 the _ankou_’s Hit Dice + the _ankou_’s Charisma modifier, typically DC 24). Against a creature that recognizes a _shadow_ double for what it is, the double functions as a _[[spells/Shadow Conjuration|shadow conjuration]]_ (Pathfinder RPG Core Rulebook 340). _Shadow_ doubles take double damage from spells with the light descriptor. If the true _ankou_ is slain, is rendered _[[conditions/Unconscious|unconscious]]_, or is ever more than 120 feet from a _shadow_ double, the duplicates instantly _[[spells/Vanish|vanish]]_.

##### Description

Ankous are assassins for powerful fey nobles, sent to kill, terrify, and torture. They never speak, only telepathically whisper their lord’s verdict to victims. A typical _ankou_ is 10 feet tall and has an 8-foot wingspan, but weighs less than 100 pounds.