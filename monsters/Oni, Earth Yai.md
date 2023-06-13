---
cssclass: [monsters]
title1: Oni, Earth Yai
desc_short: Jagged cracks and pebbled growths mar the surface of this three-eyed giant's
  rocky skin, making it appear to have burst forth from rugged stone.
title2: Earth Yai
CR: 13
sources:
- name: 'Pathfinder #53: Tide of Honor'
  page: 88
  link: http://paizo.com/pathfinder/v5748btpy8mh0
XP: 25600
alignment: NE
size: Large
type: outsider
subtypes:
- giant
- native
- oni
- shapechanger
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 29
  touch: 15
  flat_footed: 23
  components:
    dex: 6
    natural: 14
    size: -1
HP:
  HP: 184
  long: 16d10+96
  regeneration: 5
  regeneration_weakness: acid or fire
saves:
  fort: 16
  ref: 11
  will: 14
SR: 24
speeds:
  base: 50
  fly: 50
  fly_maneuverability: good
attacks:
  melee:
  - - text: greatclub +23/+18/+13/+8 (2d8+12)
      entries:
      - - damage: 2d8+12
      attack: greatclub
      bonus:
      - 23
      - 18
      - 13
      - 8
  - - text: 2 slams +23 (1d10+8)
      entries:
      - - damage: 1d10+8
      count: 2
      attack: slams
      bonus:
      - 23
  ranged:
  - - text: stony missile +21 (3d6 plus awesome blow)
      entries:
      - - damage: 3d6
        - effect: awesome blow
      attack: stony missile
      bonus:
      - 21
  special:
  - spiky skin
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: darkness
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: passwall
    source: default
    freq: At will
    other: stone only
  - name: spike stones
    source: default
    freq: 3/day
    DC: 16
  - name: stone shape
    source: default
    freq: 3/day
  - name: stone tell
    source: default
    freq: 3/day
  - name: earthquake
    source: default
    freq: 1/day
  - name: repel metal or stone
    source: default
    freq: 1/day
  - name: transmute mud to rock
    source: default
    freq: 1/day
    DC: 17
  - name: transmute rock to mud
    source: default
    freq: 1/day
    DC: 17
  sources:
  - name: default
    CL: 16
    concentration: 18
ability_scores:
  STR: 27
  DEX: 22
  CON: 23
  INT: 12
  WIS: 14
  CHA: 15
BAB: 16
CMB: 25
CMD: 41
feats:
- name: Combat Reflexes
- name: Improved Precise Shot
- name: Intimidating Prowess
- name: Iron Will
- name: Pinpoint Targeting
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
skills:
  Bluff: 21
  Fly: 27
  Intimidate: 29
  Knowledge (arcana): 20
  Perception: 17
  Sense Motive: 21
  Stealth: 21
    in rocky terrain: 29
  _racial_mods:
    Stealth:
      in rocky terrain: 8
languages:
- Common
- Giant
special_qualities:
- change shape (Medium, or Large humanoid, alter self or giant form I)
ecology:
  environment: temperate mountains
  organization: solitary, band (1 plus 4-8 stone giants), or tribe (1 plus 2-3 stone
    giant elders and 10-20 stone giants)
  treasure_type: standard
special_abilities:
  Spiky Skin (Ex): An earth yai may grow spikes from its stony skin at will as a free
    action. These spikes are treated as armor spikes that deal 1d10 points of damage.
  Stony Missile (Su): As a swift action, an earth yai can fire an incredibly dense
    stone from its third eye. This attack has a range of 200 feet, with no range increment,
    and deals 3d6 points of bludgeoning damage. Upon striking the target, the stone
    immediately makes an Awesome Blow attempt against the target using the earth yai's
    CMB.
desc_long: |-
  Although they possess the rocky physiques and near indestructibility of stone giants, earth yai scorn that race's humble ambitions, and instead prove as brutal and destructive as avalanches. For them, physical force and destruction are the ultimate demonstration of power. This belief doesn't necessarily require them to be the strongest or to go on gory rampages, though. After all, what is mere strength if a soldier can fire a catapult that brings down an entire tower, or an emperor can give the decree beginning a war that ravages an entire empire, using both their tools and words to sow ruin. Such ability to cause calamity grants one power over others; those who have the potential to cause the greatest devastation have the greatest power. Earth yai endlessly seek to hold the greatest power, leading many to become brutal warlords or bandit kings, but some to embrace more subtle, longterm machinations in their pursuit of gradual and farreaching ruin.

  In its natural form, an earth yai stands 16 feet tall and weighs 3,000 pounds.

---

# Oni, Earth Yai
Jagged cracks and pebbled growths mar the surface of this three-eyed giant’s rocky skin, making it appear to have burst forth from rugged stone.
**Source** Pathfinder #53: Tide of Honor pg. 88
**XP** 25,600

NE Large outsider (giant, native, oni, shapechanger)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17

##### Defense

**AC** 29, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+6 Dex, +14 natural, –1 size)
**hp** 184 (16d10+96); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid or fire)
**Fort** +16, **Ref** +11, **Will** +14
**SR** 24

##### Offense
**Speed** 50 ft., fly 50 ft. (good)
**Melee** _[[items/Weapon/Greatclub|greatclub]]_ +23/+18/+13/+8 (2d8+12) or 2 slams +23 (1d10+8)
**Ranged** stony missile +21 (3d6 plus _[[feats/Awesome Blow|awesome blow]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** spiky skin
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +18)
Constant—fly
At will—_[[spells/Darkness|darkness]]_, _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Passwall|passwall]]_ (stone only)
3/day—_[[spells/Spike Stones|spike stones]]_ (DC 16), _[[spells/Stone Shape|stone shape]]_, _[[spells/Stone Tell|stone tell]]_
1/day—_[[spells/Earthquake|earthquake]]_, _[[spells/Repel Metal or Stone|repel metal or stone]]_, _[[spells/Transmute Mud to Rock|transmute mud to rock]]_ (DC 17), _[[spells/Transmute Rock to Mud|transmute rock to mud]]_ (DC 17)

##### Statistics
**Str** 27, **Dex** 22, **Con** 23, **Int** 12, **Wis** 14, **Cha** 15
**Base Atk** +16; **CMB** +25; **CMD** 41
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Precise Shot|Improved Precise Shot]]_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Pinpoint Targeting|Pinpoint Targeting]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_
**Skills** Bluff +21, Fly +27, Intimidate +29, Knowledge (arcana) +20, Perception +21, Sense Motive +21, Stealth +21 (+29 in rocky terrain); **Racial Modifiers** +8 Stealth in rocky terrain
**Languages** Common, Giant
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Medium, or Large humanoid, _[[spells/Alter Self|alter self]]_ or _[[spells/Giant Form I|giant form I]]_)

##### Ecology

**Environment** temperate mountains
**Organization** solitary, band (1 plus 4–8 stone giants), or tribe (1 plus 2–3 stone giant elders and 10–20 stone giants)
**Treasure** standard

### Special Abilities
**Spiky Skin (Ex) **An earth yai may grow spikes from its stony skin at will as a free action. These spikes are treated as armor spikes that deal 1d10 points of damage.
**Stony Missile (Su) **As a swift action, an earth yai can fire an incredibly dense stone from its _[[items/Wondrous Item/Third Eye|third eye]]_. This attack has a range of 200 feet, with no range increment, and deals 3d6 points of bludgeoning damage. Upon striking the target, the stone immediately makes an _Awesome Blow_ attempt against the target using the earth yai’s CMB.

##### Description

Although they possess the rocky physiques and near indestructibility of stone giants, earth yai scorn that race’s humble ambitions, and instead prove as brutal and destructive as avalanches. For them, physical force and _[[spells/Destruction|destruction]]_ are the ultimate demonstration of power. This belief doesn’t necessarily require them to be the strongest or to go on _[[items/Weapon Magic Abilities/Gory|gory]]_ rampages, though. After all, what is mere strength if a soldier can fire a catapult that brings down an entire tower, or an emperor can give the decree beginning a war that ravages an entire empire, using both their tools and words to sow ruin. Such ability to cause calamity grants one power over others; those who have the potential to cause the greatest devastation have the greatest power. Earth yai endlessly seek to hold the greatest power, leading many to become brutal warlords or bandit kings, but some to embrace more subtle, longterm machinations in their pursuit of gradual and farreaching ruin.

In its natural form, an earth yai stands 16 feet tall and weighs 3,000 pounds.