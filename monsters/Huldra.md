---
cssclass: [monsters]
title1: Huldra
desc_short: This woman's foxlike tail and the wood-lined hollow inside her back reveal
  her true fey nature.
title2: Huldra
CR: 4
sources:
- name: Bestiary 4
  page: 151
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: Lands of the Linnorm Kings
  page: 59
  link: http://paizo.com/products/btpy8ode?Pathfinder-Campaign-Setting-Lands-of-the-Linnorm-Kings
XP: 1200
alignment: CN
size: Medium
type: fey
initiative:
  bonus: 3
senses:
  darkvision: 60
  detect snares and pits: true
  low-light vision: true
  scent: true
AC:
  AC: 17
  touch: 14
  flat_footed: 13
  components:
    dex: 3
    dodge: 1
    natural: 3
HP:
  HP: 38
  long: 7d6+14
  regeneration: 3
  regeneration_weakness: acid or fire
saves:
  fort: 4
  ref: 8
  will: 7
immunities:
- charm effects
- compulsion effects
resistances:
  cold: 10
speeds:
  base: 30
attacks:
  melee:
  - - text: slam +7 (1d6+4)
      entries:
      - - damage: 1d6+4
      attack: slam
      bonus:
      - 7
    - text: tail slap +7 (1d6+4 plus 1d4 Cha damage)
      entries:
      - - damage: 1d6+4
        - damage: 1d4
          type: Cha damage
      attack: tail slap
      bonus:
      - 7
  special:
  - lashing tail
  - manipulate luck
spell_like_abilities:
  entries:
  - name: detect snares and pits
    source: default
    freq: Constant
  - name: endure elements
    source: default
    freq: Constant
  - name: pass without trace
    source: default
    freq: Constant
  - name: charm person
    source: default
    freq: 3/day
    DC: 15
  - name: daze monster
    source: default
    freq: 3/day
    DC: 16
  - name: wood shape
    source: default
    freq: 3/day
  - name: deep slumber
    source: default
    freq: 1/day
    DC: 17
  sources:
  - name: default
    CL: 4
    concentration: 8
ability_scores:
  STR: 19
  DEX: 17
  CON: 14
  INT: 12
  WIS: 14
  CHA: 19
BAB: 3
CMB: 7
CMD: 21
feats:
- name: Deceitful
- name: Dodge
- name: Mobility
- name: Power Attack
skills:
  Bluff: 16
  Disguise: 16
  Escape Artist: 13
  Knowledge (nature): 11
  Perception: 12
  Stealth: 13
  Use Magic Device: 14
languages:
- Common
- Giant
- Sylvan
ecology:
  environment: cold forests or mountains
  organization: solitary, pair, or family (3-9)
  treasure_type: standard
special_abilities:
  Lashing Tail (Su): A huldra's tail slap is a primary attack. In addition, each time
    a huldra damages a creature with her tail slap, she deals 1d4 points of Charisma
    damage, causing her target to grow progressively more deformed and ugly with each
    strike. A successful DC 15 Fortitude save negates the Charisma damage. The save
    DC is Constitution-based.
  Manipulate Luck (Su): Once per day, a huldra can manipulate another creature's luck
    by spending a full-round action, during which the huldra must remain in physical
    contact with the target creature. When the huldra uses this ability, she must
    choose whether she is imparting good luck or bad luck. A creature granted good
    luck gains a +2 luck bonus on all saving throws, attack rolls, and skill checks,
    while a creature afflicted with bad luck takes a -4 penalty on all saving throws,
    attack rolls, and skill checks. A successful DC 17 Will save negates the effect.
    Huldras cannot be the target of this ability. This effect lasts for 24 hours and
    is a curse effect. The save DC is Charisma-based.
desc_long: |-
  Huldras are fey creatures that legend claims were originally created by troll witches to lure humans into their clutches. Every huldra is aware of this tale, finds it insulting, and denies it at length-yet the legend persists. There's no greater way to inf lame a huldra to anger than to speak about this myth (especially while expressing distrust or contempt for the huldra), and the huldras' hatred of all things trollish is well known among scholars of the fey and those who regularly encounter the less common fey creatures.

  From the front, a huldra appears to be a beautiful human woman, yet two distinctive features mark the huldra as something supernatural: her long, foxlike tail, and the fact that she doesn't have a solid back-merely a hole that reveals her body to be a hollow, bark-lined shell. Most huldras wear their hair long to mask the hole in their backs, and they prefer long gowns to hide their tails when interacting with humanoids. Though huldras are not ashamed of their status as fey, they react rather negatively when someone points out their tails. So long as humanoids are respectful, however, huldras tend to be curious about other races, and may aid those who pass through their territories by telling them the best places for hunting or fishing.

  Huldras sometimes become enamored of woodcutters or others who adventure outdoors, and invite these paramours to share their beds, but such romances usually end in disappointment and misunderstanding on both sides. Despite their relatively lithe frames, huldras are deceptively strong, and stories abound of them performing astonishing feats of strength such as straightening horseshoes and tossing aside attackers, and their natural weapons are quite potent.

---

# Huldra
This woman’s foxlike tail and the wood-lined hollow inside her back reveal her true fey nature.
**Source** Bestiary 4 pg. 151, Lands of the Linnorm Kings pg. 59
**XP** 1,200

CN Medium fey
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Snares and Pits|detect snares and pits]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +12

##### Defense

**AC** 17, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 Dex, +1 _[[feats/Dodge|dodge]]_, +3 natural)
**hp** 38 (7d6+14); _[[universal monster rules/Regeneration|regeneration]]_ 3 (acid or fire)
**Fort** +4, **Ref** +8, **Will** +7
**Immune** charm effects, compulsion effects; **Resist** cold 10

##### Offense
**Speed** 30 ft.
**Melee** slam +7 (1d6+4), tail slap +7 (1d6+4 plus 1d4 Cha damage)
**Special Attacks** _[[feats/Lashing Tail|lashing tail]]_, manipulate luck
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +8)
Constant—_detect snares and pits_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Pass without Trace|pass without trace]]_
3/day—_[[spells/Charm Person|charm person]]_ (DC 15), _[[spells/Daze Monster|daze monster]]_ (DC 16), _[[spells/Wood Shape|wood shape]]_
1/day—_[[spells/Deep Slumber|deep slumber]]_ (DC 17)

##### Statistics
**Str** 19, **Dex** 17, **Con** 14, **Int** 12, **Wis** 14, **Cha** 19
**Base Atk** +3; **CMB** +7; **CMD** 21
**Feats** _[[feats/Deceitful|Deceitful]]_, _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Bluff +16, Disguise +16, Escape Artist +13, Knowledge (nature) +11, Perception +12, Stealth +13, Use Magic Device +14
**Languages** Common, Giant, Sylvan

##### Ecology

**Environment** cold forests or mountains
**Organization** solitary, pair, or family (3–9)
**Treasure** standard

### Special Abilities

**_Lashing Tail_ (Su)** A _[[monsters/Huldra|huldra]]_’s tail slap is a primary attack. In addition, each time a _huldra_ damages a creature with her tail slap, she deals 1d4 points of Charisma damage, causing her target to grow progressively more deformed and ugly with each strike. A successful DC 15 Fortitude save negates the Charisma damage. The save DC is Constitution-based.

**Manipulate Luck (Su)** Once per day, a _huldra_ can manipulate another creature’s luck by spending a full-round action, during which the _huldra_ must remain in physical contact with the target creature. When the _huldra_ uses this ability, she must choose whether she is imparting good luck or bad luck. A creature granted good luck gains a +2 luck bonus on all saving throws, attack rolls, and skill checks, while a creature afflicted with bad luck takes a –4 penalty on all saving throws, attack rolls, and skill checks. A successful DC 17 Will save negates the effect. Huldras cannot be the target of this ability. This effect lasts for 24 hours and is a curse effect. The save DC is Charisma-based.

##### Description

Huldras are fey creatures that legend claims were originally created by _[[monsters/Troll|troll]]_ witches to lure humans into their clutches. Every _huldra_ is aware of this tale, finds it insulting, and denies it at length—yet the legend persists. There’s no greater way to inf lame a _huldra_ to anger than to speak about this myth (especially while expressing distrust or contempt for the _huldra_), and the huldras’ hatred of all things trollish is well known among scholars of the fey and those who regularly encounter the less common fey creatures.

From the front, a _huldra_ appears to be a beautiful human woman, yet two distinctive features mark the _huldra_ as something supernatural: her long, foxlike tail, and the fact that she doesn’t have a solid back—merely a hole that reveals her body to be a hollow, bark-lined shell. Most huldras wear their hair long to _[[items/Mundane/Mask|mask]]_ the hole in their backs, and they prefer long gowns to hide their tails when interacting with humanoids. Though huldras are not ashamed of their _[[spells/Status|status]]_ as fey, they react rather negatively when someone points out their tails. So long as humanoids are respectful, however, huldras tend to be curious about other races, and may aid those who pass through their territories by telling them the best places for hunting or fishing.

Huldras sometimes become enamored of woodcutters or others who adventure outdoors, and invite these paramours to share their beds, but such romances usually end in disappointment and misunderstanding on both sides. Despite their relatively lithe frames, huldras are deceptively strong, and stories abound of them performing astonishing feats of strength such as straightening horseshoes and tossing aside attackers, and their natural weapons are quite _[[items/Weapon Magic Abilities/Potent|potent]]_.