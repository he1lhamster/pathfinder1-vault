---
cssclass: [monsters]
title1: Oni, Ice Yai
desc_short: This blue-skinned giant has three eyes, fangs, and claws. Its hair seems
  to be formed of delicate strands of ice.
title2: Ice Yai
CR: 14
sources:
- name: Bestiary 3
  page: 207
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 38400
alignment: CE
size: Large
type: outsider
subtypes:
- cold
- oni
- giant
- native
- shapechanger
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 27
  touch: 12
  flat_footed: 24
  components:
    armor: 4
    dex: 2
    dodge: 1
    natural: 11
    size: -1
HP:
  HP: 200
  long: 16d10+112
  regeneration: 5
  regeneration_weakness: fire or acid
saves:
  fort: 17
  ref: 7
  will: 12
immunities:
- cold
SR: 25
weaknesses:
- vulnerability to fire
speeds:
  base: 50
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 4 slams +24 (2d8+9)
      entries:
      - - damage: 2d8+9
      count: 4
      attack: slams
      bonus:
      - 24
  ranged:
  - - text: icy missile +17 touch (4d6 cold)
      entries:
      - - damage: 4d6
          type: cold
      attack: icy missile
      bonus:
      - 17
      touch: true
  special:
  - staggering strikes
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: mage armor
    source: default
    freq: Constant
  - name: darkness
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: charm monster
    source: default
    freq: 3/day
    DC: 18
  - name: cone of cold
    source: default
    freq: 3/day
    DC: 19
  - name: deep slumber
    source: default
    freq: 3/day
    DC: 17
  - name: gaseous form
    source: default
    freq: 3/day
    other: self only
  - name: polar ray
    source: default
    freq: 1/day
  - name: solid fog
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 18
    concentration: 22
ability_scores:
  STR: 29
  DEX: 14
  CON: 25
  INT: 12
  WIS: 15
  CHA: 18
BAB: 16
CMB: 26
CMD: 39
feats:
- name: Cleave
- name: Combat Reflexes
- name: Dodge
- name: Great Cleave
- name: Mobility
- name: Power Attack
- name: Spring Attack
- name: Vital Strike
skills:
  Bluff: 23
  Disguise: 14
  Fly: 25
  Intimidate: 23
  Knowledge (arcana): 11
  Perception: 22
  Sense Motive: 13
  Spellcraft: 8
  Stealth: 17
    in snow: 21
  Use Magic Device: 14
  _racial_mods:
    Stealth:
      in snow: 4
languages:
- Common
- Giant
special_qualities:
- change shape (Medium or Large humanoid; alter self or giant form I)
ecology:
  environment: cold mountains
  organization: solitary or gang (1 plus 4-16 frost giants)
  treasure_type: standard
special_abilities:
  Icy Missile (Su): As a swift action, the ice yai can fire a dart of ice from its
    third eye. This dart is a ranged touch attack (+20 attack bonus), dealing 4d6
    points of cold damage on a hit. This attack has a range of 180 feet with no range
    increment.
  Staggering Strikes (Ex): An ice yai can strike twice per round with its two slam
    attacks. A creature struck by more than two of these slam attacks in a round must
    make a DC 27 Fortitude save or be staggered for 1 round. The save DC is Strength-based.
desc_long: |-
  The ice yai is a sinister creature that combines the brutality of a frost giant with the grace and style of a skilled martial artist. Although its magical powers are formidable, it prefers to fight in melee using its slam attacks, leading its minions in merciless combat. It uses its mobility to cast combat spells or launch shards of ice from its third eye.

  An ice yai is a natural leader among frost giants, tempering their savagery with its own wisdom. A tribe led by an ice yai may still raid settlements of neighboring humanoids, but the tribe soon learns the value of establishing regular tributes and willing sacrifices-the ice yai teach that methods that rely upon the threat of violence are often even more effective than actual violence. Despite this strangely enlightened philosophy, an ice yai never passes up an opportunity to reinforce its capacity for slaughter, and will often demand that its subjects take part in show battles, both for the entertainment of the tribe and to nurture the ice yai's insatiable ego and sense of dominion over its subjects.

---

# Oni, Ice Yai
This blue-skinned giant has three eyes, fangs, and claws. Its hair seems to be formed of delicate strands of ice.
**Source** Bestiary 3 pg. 207
**XP** 38,400
CE Large outsider (cold, oni, giant, native, shapechanger)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +22

##### Defense

**AC** 27, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+4 armor, +2 Dex, +1 dodge, +11 natural, –1 size)
**hp** 200 (16d10+112); _[[universal monster rules/Regeneration|regeneration]]_ 5 (fire or acid)
**Fort** +17, **Ref** +7, **Will** +12
**Immune** cold; **SR** 25
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to fire

##### Offense
**Speed** 50 ft., fly 60 ft. (good)
**Melee** 4 slams +24 (2d8+9)
**Ranged** icy missile +17 touch (4d6 cold)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** staggering strikes
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +22)
Constant—fly, _[[spells/Mage Armor|mage armor]]_
At will—_[[spells/Darkness|darkness]]_, _[[spells/Invisibility|invisibility]]_ (self only)
3/day— _[[spells/Charm Monster|charm monster]]_ (DC 18), _[[spells/Cone of Cold|cone of cold]]_ (DC 19), _[[spells/Deep Slumber|deep slumber]]_ (DC 17), _[[spells/Gaseous Form|gaseous form]]_ (self only)
1/day—_[[spells/Polar Ray|polar ray]]_, _[[spells/Solid Fog|solid fog]]_

##### Statistics
**Str** 29, **Dex** 14, **Con** 25, **Int** 12, **Wis** 15, **Cha** 18
**Base Atk** +16; **CMB** +26; **CMD** 39
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +23, Disguise +14, Fly +25, Intimidate +23, Knowledge (arcana) +11, Perception +22, Sense Motive +13, Spellcraft +8, Stealth +17 (+21 in snow), Use Magic Device +14; **Racial Modifiers** +4 Stealth in snow
**Languages** Common, Giant
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_[[classes/Medium|Medium]]_ or Large humanoid; _[[spells/Alter Self|alter self]]_ or _[[spells/Giant Form I|giant form I]]_)

##### Ecology

**Environment** cold mountains
**Organization** solitary or gang (1 plus 4–16 frost giants)
**Treasure** standard

### Special Abilities

**Icy Missile (Su)** As a swift action, the ice yai can fire a _[[items/Weapon/Dart|dart]]_ of ice from its _[[items/Wondrous Item/Third Eye|third eye]]_. This _dart_ is a ranged touch attack (+20 attack bonus), dealing 4d6 points of cold damage on a hit. This attack has a range of 180 feet with no range increment.
**Staggering Strikes (Ex) **An ice yai can strike twice per round with its two slam attacks. A creature struck by more than two of these slam attacks in a round must make a DC 27 Fortitude save or be _[[conditions/Staggered|staggered]]_ for 1 round. The save DC is Strength-based.

##### Description

The ice yai is a sinister creature that combines the brutality of a frost giant with the _[[spells/Grace|grace]]_ and style of a skilled martial artist. Although its magical powers are formidable, it prefers to fight in melee using its slam attacks, leading its minions in merciless combat. It uses its _mobility_ to cast combat spells or launch shards of ice from its _third eye_.

An ice yai is a natural leader among frost giants, tempering their savagery with its own wisdom. A tribe led by an ice yai may still raid settlements of neighboring humanoids, but the tribe soon learns the value of establishing regular tributes and willing sacrifices—the ice yai teach that methods that rely upon the threat of violence are often even more effective than actual violence. Despite this strangely enlightened philosophy, an ice yai never passes up an opportunity to reinforce its capacity for slaughter, and will often _[[spells/Demand|demand]]_ that its subjects take part in show battles, both for the entertainment of the tribe and to nurture the ice yai’s insatiable ego and sense of dominion over its subjects.