---
cssclass: [monsters]
title1: Boruta
desc_short: Piercing yellow eyes gaze from the mossy skull of this ivy-covered skeleton.
  Where bones should be, gnarled roots grow, and tangles of vines hang from its moldering
  chest like spilt viscera.
title2: Boruta
CR: 9
sources:
- name: 'Pathfinder #44: Trial of the Beast'
  page: 84
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/carrionCrown/v5748btpy8j5s
XP: 6400
alignment: N
size: Medium
type: plant
initiative:
  bonus: 6
senses:
  low-light vision: true
AC:
  AC: 23
  touch: 13
  flat_footed: 20
  components:
    dex: 2
    dodge: 1
    natural: 10
HP:
  HP: 105
  long: 14d8+42
saves:
  fort: 12
  ref: 6
  will: 7
immunities:
- electricity
- plant traits
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +13 (1d4+3 plus grounding curse)
      entries:
      - - damage: 1d4+3
        - effect: grounding curse
      count: 2
      attack: claws
      bonus:
      - 13
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: entangle
    source: default
    freq: At will
    DC: 14
  - name: command plants
    source: default
    freq: 3/day
    DC: 17
  - name: summon nature's ally V
    source: default
    freq: 1/day
    other: 1 shambling mound only
  sources:
  - name: default
    CL: 7
    concentration: 10
spells:
  entries:
  - name: spike stones
    source: '?'
    level: 4
    DC: 17
  - name: call lightning
    source: '?'
    level: 3
    count: 2
    DC: 16
  - name: plant growth
    source: '?'
    level: 3
  - name: fog cloud
    source: '?'
    level: 2
  - name: soften earth and stone
    source: '?'
    level: 2
  - name: tree shape
    source: '?'
    level: 2
  - name: wood shape
    source: '?'
    level: 2
    DC: 15
  - name: calm animals
    source: '?'
    level: 1
  - name: detect animals or plants
    source: '?'
    level: 1
  - name: goodberry
    source: '?'
    level: 1
  - name: magic fang
    source: '?'
    level: 1
  - name: speak with animals
    source: '?'
    level: 1
  - name: create water
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: detect poison
    source: '?'
    level: 0
  - name: know direction
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: prepared
    CL: 7
    concentration: 10
ability_scores:
  STR: 17
  DEX: 15
  CON: 16
  INT: 13
  WIS: 17
  CHA: 16
BAB: 10
CMB: 13
CMD: 26
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Improved Iron Will
- name: Mobility
- name: Natural Spell
skills:
  Perception: 20
  Stealth: 19
  Survival: 17
languages:
- Common
- Sylvan
special_qualities:
- treespeech
- wild shape
ecology:
  environment: any
  organization: solitary, party (2-4), or band (2-4 borutas plus 1-3 shambling mounds)
  treasure_type: none
special_abilities:
  Electric Fortitude (Ex): Borutas take no damage from electricity. Instead, any electricity
    attack used against a boruta temporarily increases its Constitution score by 1d4
    points. The boruta loses these temporary points at the rate of 1 per hour.
  Grounding Curse (Su): Any living creature that takes damage from a boruta's claws
    must make a DC 20 Fortitude save or have hundreds of tiny seed pods injected into
    its body. These seeds grow rapidly; they explode through the victim's skin on
    its next turn, dealing 1d6 points of damage and entangling it as runners and vines
    grow from its flesh and root themselves in the ground. The victim cannot move
    unless it makes a DC 10 Strength check to tear the plants from the ground, but
    doing so also deals 1d4 points of damage to the victim. This effect lasts for
    10 minutes. Remove curse, blight, diminish plants, and similar spells instantly
    end this effect. The save DC is Constitution-based.
  Treespeech (Ex): A boruta has the ability to converse with plants as if subject
    to a continual speak with plants spell, and most plants greet them with an attitude
    of friendly or helpful.
  Wild Shape (Su): A boruta can wild shape three times per day as a 7th-level druid.
    In any form a boruta takes, its appearance remains plantlike, with wooden features
    and leaves rather than fur or feathers.
desc_long: |-
  A distant cousin of shambling mounds, borutas are powerful wielders of natural magic that make their homes in marshes or wetlands, where their mysterious control over the natural environment is most useful.

  Though none are sure of the specific relationship between borutas and shambling mounds, the connection is clear when comparing the two, their powers and affinity for the marshlands being the most obvious similarities. Borutas-or “swamp lords,” as they're sometimes called- resemble mossy, skeletal humans at first glance, with bonelike wooden frames, viny covering, and vivid yellow eyes. Considerably more intelligent than their shambling mound cousins, they claim wide territories-typically swamps, forests, jungles, or other lands thick with plant-life-and brook no insult to their realm. Highly defensive of the life within their lands, especially plants and thinking plant creatures, borutas view themselves as the avengers of those that can't defend themselves, and mercilessly repay destructive invaders with verdurous force. On the rare occasions when they deal peaceably with non-plant creatures, borutas cover their frightening forms with thick veils of grass or peat moss.

  Borutas generally stand about 7 feet tall and weigh just over 200 pounds.

---

# Boruta
Piercing yellow eyes _[[universal monster rules/Gaze|gaze]]_ from the mossy skull of this ivy-covered skeleton. Where bones should be, gnarled roots grow, and tangles of vines hang from its moldering chest like spilt viscera.
**Source** Pathfinder #44: Trial of the Beast pg. 84
**XP** 6,400

N Medium plant
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +20

##### Defense

**AC** 23, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+2 Dex, +1 _[[feats/Dodge|dodge]]_, +10 natural)
**hp** 105 (14d8+42)
**Fort** +12, **Ref** +6, **Will** +7
**Immune** electricity, _[[universal monster rules/Plant Traits|plant traits]]_

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +13 (1d4+3 plus _[[items/Weapon Magic Abilities/Grounding|grounding]]_ curse)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +10)
Constant - _[[spells/Pass without Trace|pass without trace]]_
At will - _[[spells/Entangle|entangle]]_ (DC 14)
3/day - _[[spells/Command Plants|command plants]]_ (DC 17)
1/day - _[[spells/Summon Nature's Ally V|summon nature's ally V]]_ (1 _[[monsters/Shambling Mound|shambling mound]]_ only)
**Spells Prepared** (CL 7th; concentration +10)
4th — _[[spells/Spike Stones|spike stones]]_ (DC 17)
3rd — _[[spells/Call Lightning|call lightning]]_ (2, DC 16), _[[spells/Plant Growth|plant growth]]_
2nd — _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Soften Earth and Stone|soften earth and stone]]_, _[[spells/Tree Shape|tree shape]]_, _[[spells/Wood Shape|wood shape]]_ (DC 15)
1st — _[[spells/Calm Animals|calm animals]]_, _[[spells/Detect Animals or Plants|detect animals or plants]]_, _[[spells/Goodberry|goodberry]]_, _[[spells/Magic Fang|magic fang]]_, _[[spells/Speak with Animals|speak with animals]]_
0 — _[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Know Direction|know direction]]_, _[[spells/Mending|mending]]_

##### Statistics
**Str** 17, **Dex** 15, **Con** 16, **Int** 13, **Wis** 17, **Cha** 16
**Base Atk** +10; **CMB** +13; **CMD** 26
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Natural Spell|Natural Spell]]_
**Skills** Perception +20, Stealth +19, Survival +17
**Languages** Common, Sylvan
**SQ** treespeech, wild shape

##### Ecology

**Environment** any
**Organization** solitary, party (2-4), or band (2-4 borutas plus 1-3 shambling mounds)
**Treasure** none

### Special Abilities

**Electric Fortitude (Ex)** Borutas take no damage from electricity. Instead, any electricity attack used against a _[[monsters/Boruta|boruta]]_ temporarily increases its Constitution score by 1d4 points. The _boruta_ loses these temporary points at the rate of 1 per hour.

**_Grounding_ Curse (Su)** Any living creature that takes damage from a _boruta_’s claws must make a DC 20 Fortitude save or have hundreds of tiny seed pods injected into its body. These seeds grow rapidly; they explode through the victim’s skin on its next turn, dealing 1d6 points of damage and entangling it as runners and vines grow from its flesh and _[[spells/Root|root]]_ themselves in the ground. The victim cannot move unless it makes a DC 10 Strength check to tear the plants from the ground, but doing so also deals 1d4 points of damage to the victim. This effect lasts for 10 minutes. _[[spells/Remove Curse|Remove curse]]_, _[[spells/Blight|blight]]_, _[[spells/Diminish Plants|diminish plants]]_, and similar spells instantly end this effect. The save DC is Constitution-based.

**Treespeech (Ex)** A _boruta_ has the ability to converse with plants as if subject to a continual _[[spells/Speak with Plants|speak with plants]]_ spell, and most plants greet them with an attitude of friendly or helpful.

**Wild Shape (Su)** A _boruta_ can wild shape three times per day as a 7th-level _[[classes/Druid|druid]]_. In any form a _boruta_ takes, its appearance remains plantlike, with wooden features and leaves rather than fur or feathers.

##### Description

A distant cousin of shambling mounds, borutas are powerful wielders of natural magic that make their homes in marshes or wetlands, where their mysterious control over the natural environment is most useful.

Though none are sure of the specific relationship between borutas and shambling mounds, the connection is clear when comparing the two, their powers and affinity for the marshlands being the most obvious similarities. Borutas—or “swamp lords,” as they’re sometimes _[[items/Weapon Magic Abilities/Called|called]]_— resemble mossy, skeletal humans at first glance, with bonelike wooden frames, viny covering, and vivid yellow eyes. Considerably more intelligent than their _shambling mound_ cousins, they claim wide territories—typically swamps, forests, jungles, or other lands thick with plant-life—and brook no insult to their realm. Highly defensive of the life within their lands, especially plants and thinking plant creatures, borutas view themselves as the avengers of those that can’t defend themselves, and mercilessly repay destructive invaders with verdurous force. On the rare occasions when they deal peaceably with non-plant creatures, borutas cover their frightening forms with thick veils of grass or peat moss.

Borutas generally stand about 7 feet tall and weigh just over 200 pounds.