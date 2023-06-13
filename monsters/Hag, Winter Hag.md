---
cssclass: [monsters]
title1: Hag, Winter Hag
desc_short: This woman has black, frostbitten skin, white hair, and a black ice staff
  decorated with bones and gems.
title2: Winter Hag
CR: 7
sources:
- name: Bestiary 4
  page: 279
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 3200
alignment: CE
size: Medium
type: monstrous humanoid
subtypes:
- cold
initiative:
  bonus: 1
senses:
  darkvision: 60
  see invisibility: true
  snow vision: true
AC:
  AC: 20
  touch: 11
  flat_footed: 19
  components:
    dex: 1
    natural: 9
HP:
  HP: 85
  long: 10d10+30
saves:
  fort: 8
  ref: 8
  will: 8
DR:
- amount: 10
  weakness: magic
immunities:
- cold
SR: 18
weaknesses:
- vulnerable to fire
speeds:
  base: 30
attacks:
  melee:
  - - text: +2 frost quarterstaff +15/+10 (1d6+6 plus 1d6 cold)
      entries:
      - - damage: 1d6+6
        - damage: 1d6
          type: cold
      attack: +2 frost quarterstaff
      bonus:
      - 15
      - 10
  - - text: 2 claws +13 (1d4+3)
      entries:
      - - damage: 1d4+3
      count: 2
      attack: claws
      bonus:
      - 13
  special:
  - breath weapon (30-ft. cone, 4d6 cold and blinded for 1d6 rounds, Reflex DC 18
    partial, usable every 1d4 round)
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: chill metal
    source: default
    freq: At will
    DC: 16
  - name: detect magic
    source: default
    freq: At will
  - name: fog cloud
    source: default
    freq: At will
  - superscripts:
    - UM
    name: frostbite
    source: default
    freq: At will
  - name: whispering wind
    source: default
    freq: At will
  - name: alter self
    source: default
    freq: 3/day
  - name: charm monster
    source: default
    freq: 3/day
    DC: 18
  - name: invisibility
    source: default
    freq: 3/day
    other: self only
  - name: major image
    source: default
    freq: 3/day
    DC: 17
  - name: cone of cold
    source: default
    freq: 1/day
    DC: 19
    other: see ice staff
  - name: control weather
    source: default
    freq: 1/day
    other: windy or cold weather only
  - name: wall of ice
    source: default
    freq: 1/day
    DC: 18
  - name: waves of fatigue
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 10
    concentration: 14
ability_scores:
  STR: 17
  DEX: 13
  CON: 16
  INT: 16
  WIS: 13
  CHA: 18
BAB: 10
CMB: 13
CMD: 24
feats:
- name: Alertness
- name: Blind-Fight
- name: Combat Casting
- name: Deceitful
- name: Great Fortitude
skills:
  Bluff: 18
  Craft (alchemy): 11
  Diplomacy: 9
  Disguise: 11
  Intimidate: 17
  Knowledge (arcana): 8
  Perception: 18
  Ride: 9
  Sense Motive: 8
  Spellcraft: 8
  Stealth: 9
    in snow: 13
  _racial_mods:
    Stealth:
      in snow: 4
languages:
- Aklo
- Common
- Giant
special_qualities:
- ice staff
- icewalking
ecology:
  environment: cold forests or plains
  organization: solitary, patrol (1 plus 1 winter wolf), or coven (3 hags of any type)
  treasure_type: standard
special_abilities:
  Breath Weapon (Su): A creature that successfully saves against the hag's breath
    weapon takes half damage and is not blinded.
  Ice Staff (Su): Once per week, a winter hag can perform an hour-long ritual to create
    a staff made of black ice that is as hard as steel and functions as a +2 frost
    quarterstaff. A winter hag holding her ice staff can use cone of cold once per
    day as a spell-like ability. The staff melts after 1 week.
  Icewalking (Ex): This ability works like the spider climb spell, but the surfaces
    the hag climbs must be icy. The hag can move across icy surfaces without penalty
    and doesn't need to make Acrobatics checks to run or charge on ice.
  Snow Vision (Ex): A winter hag can see perfectly well in snowy conditions and doesn't
    take any penalties on Perception checks while in snow.
desc_long: |-
  Winter hags are sadistic crones who haunt winter-blasted plains and rime-covered forests. They're exceptionally arrogant, and often use their magic to subjugate entire tribes of evil humanoids so they can rule over them as queens. These arrangements rarely last more than a few seasons, because no creature is truly safe from a winter hag's irrepressible appetite for warm, raw flesh. An ambitious winter hag might extort a village by causing constant snowfall until they give her children to eat or adults to become her slaves.

  A typical winter hag stands between 5 and 6 feet tall and weighs 100 pounds.

  When a winter hag joins a coven, the coven adds sculpt simulacrum and simulacrum to its spell-like abilities, and any member within 1 mile of the winter hag gains icewalking and snow vision.

---

# Hag, Winter Hag
This woman has black, frostbitten skin, white hair, and a _[[npcs/Black Ice|black ice]]_ staff decorated with bones and gems.
**Source** Bestiary 4 pg. 279
**XP** 3,200
CE Medium monstrous humanoid (cold)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_, snow _[[spells/Vision|vision]]_; Perception +18

##### Defense

**AC** 20, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+1 Dex, +9 natural)
**hp** 85 (10d10+30)
**Fort** +8, **Ref** +8, **Will** +8
**DR** 10/magic; **Immune** cold; **SR** 18
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 30 ft.
**Melee** +2 frost _[[items/Weapon/Quarterstaff|quarterstaff]]_ +15/+10 (1d6+6 plus 1d6 cold) or 2 claws +13 (1d4+3)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-ft. cone, 4d6 cold and _[[conditions/Blinded|blinded]]_ for 1d6 rounds, Reflex DC 18 partial, usable every 1d4 round)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
Constant—_[[spells/Pass without Trace|pass without trace]]_, _see invisibility_
At will—_[[spells/Chill Metal|chill metal]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Frostbite|frostbite]]_, _[[spells/Whispering Wind|whispering wind]]_
3/day—_[[spells/Alter Self|alter self]]_, _[[spells/Charm Monster|charm monster]]_ (DC 18), _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Major Image|major image]]_ (DC 17)
1/day—_[[spells/Cone of Cold|cone of cold]]_ (DC 19; see ice staff), _[[spells/Control Weather|control weather]]_ (windy or cold weather only), _[[spells/Wall Of Ice|wall of ice]]_ (DC 18), _[[spells/Waves of Fatigue|waves of fatigue]]_

##### Statistics
**Str** 17, **Dex** 13, **Con** 16, **Int** 16, **Wis** 13, **Cha** 18
**Base Atk** +10; **CMB** +13; **CMD** 24
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Deceitful|Deceitful]]_, _[[feats/Great Fortitude|Great Fortitude]]_
**Skills** Bluff +18, Craft (alchemy) +11, Diplomacy +9, Disguise +11, Intimidate +17, Knowledge (arcana) +8, Perception +18, Ride +9, Sense Motive +8, Spellcraft +8, Stealth +9 (+13 in snow); **Racial Modifiers** +4 Stealth in snow
**Languages** Aklo, Common, Giant
**SQ** ice staff, icewalking

##### Ecology

**Environment** cold forests or plains
**Organization** solitary, patrol (1 plus 1 winter _[[monsters/Wolf|wolf]]_), or coven (3 hags of any type)
**Treasure** standard

### Special Abilities

**_Breath Weapon_ (Su)** A creature that successfully saves against the hag’s _breath weapon_ takes half damage and is not _blinded_.

**Ice Staff (Su)** Once per week, a winter hag can perform an hour-long ritual to create a staff made of _black ice_ that is as hard as steel and functions as a +2 frost _quarterstaff_. A winter hag holding her ice staff can use _cone of cold_ once per day as a spell-like ability. The staff melts after 1 week.

**Icewalking (Ex)** This ability works like the _[[spells/Spider Climb|spider climb]]_ spell, but the surfaces the hag climbs must be icy. The hag can move across icy surfaces without penalty and doesn’t need to make Acrobatics checks to run or charge on ice.
**Snow _Vision_ (Ex)** A winter hag can see perfectly well in snowy conditions and doesn’t take any penalties on Perception checks while in snow.

##### Description

Winter hags are sadistic crones who haunt winter-blasted plains and rime-covered forests. They’re exceptionally arrogant, and often use their magic to subjugate entire tribes of evil humanoids so they can rule over them as queens. These arrangements rarely last more than a few seasons, because no creature is truly safe from a winter hag’s irrepressible appetite for warm, raw flesh. An ambitious winter hag might extort a village by causing constant snowfall until they give her children to eat or adults to become her slaves.

A typical winter hag stands between 5 and 6 feet tall and weighs 100 pounds.

When a winter hag joins a coven, the coven adds _[[spells/Sculpt Simulacrum|sculpt simulacrum]]_ and _[[spells/Simulacrum|simulacrum]]_ to its _spell-like abilities_, and any member within 1 mile of the winter hag gains icewalking and snow _vision_.